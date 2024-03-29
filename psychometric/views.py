from django.shortcuts import render
from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from .serializers import PsychometricTestSerializer, PsychometricStatusSerializer, PsychometricResultDetailSerializer,TypeSerializer, TestResultDetailSerializer, CareerIdeaSerializer, ChoiceIdeaSerializer, StudyTipsSerializer
from .models import PsychometricTest,Answer,Question,TestType,TestResult,TestResultDetail, CareerIdea, ChoiceIdea, StudyTips
from users.models import Student
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.


class PsychometricViewRelated(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset=PsychometricTest.objects.all()

    
    def get(self, request):
        """Fetch All Tests By User"""
        try:
            tests=PsychometricTest.objects.all()
            serializer = PsychometricTestSerializer(tests, many=True)
            return Response(serializer.data)
    
        except Exception as e:
           return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

    def post(self, request):
        try:
            TOTAL_POINT=0
            user_obj=request.user
            questions=request.data.get('question')
            std_obj= Student.objects.get(user=user_obj.id)
            for quest in questions:
                ques_obj=Question.objects.filter(question=quest['question']).first()
                test_obj=PsychometricTest.objects.filter(name=request.data.get('name')).first()
                if ques_obj:
                    answer=quest['answer']
                    ans=Answer.objects.filter(answer=answer).filter(question=ques_obj).first()
                    weightage= ans.weightage
                    TOTAL_POINT=TOTAL_POINT+weightage
                    score= TOTAL_POINT
                    

                else:
                    return Response("Question doesnt exist") 
                
            result_obj=TestResult.objects.get_or_create(user=std_obj,score=score,test=test_obj)
            return Response(data={'success': True, 'Total Point': TOTAL_POINT}, status=status.HTTP_200_OK) 
        
        except Exception as e:
           return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PsychometricDetails(CreateAPIView):

    permission_classes = [IsAuthenticated]
    queryset = Question.objects.all()
    serializer_class = PsychometricTestSerializer

    lookup_field = 'id'

    def get_test(self, id):
        try:
            return PsychometricTest.objects.get(id = id)
        except Exception as e:
           return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        print("workkk")
        test = self.get_test(id)
        print(test)
        serializer = PsychometricTestSerializer(test)
        # print(serializer.data)
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, id):
        test = self.get_object(id)
        test.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class CalculatePoints(CreateAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Fetch score by test type"""
        try:
            user_obj = request.user
            std_obj = Student.objects.get(user=user_obj.id)
            test_results = TestResult.objects.filter(user=std_obj).select_related('test')
            res = []

            for test_result in test_results:
                test_data = {
                    "id": test_result.test.id,
                    "test_name": test_result.test.name,
                    "scores": []
                }

                test_result_details = TestResultDetail.objects.filter(result=test_result).select_related('question__type')
                question_type_scores = test_result_details.values('question__type__type').annotate(total_score=Sum('answer__weightage'))

                for score in question_type_scores:
                    score_data = {
                        "name": score['question__type__type'],
                        "score": score['total_score']
                    }
                    test_data["scores"].append(score_data)
                res.append(test_data)

            return Response(res)
    
        except Exception as e:
           return Response({'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class PsychometricTestView(ListAPIView):
    queryset = PsychometricTest.objects.all()
    serializer_class = PsychometricStatusSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context
    


class TakeTestView(CreateAPIView):
    serializer_class = PsychometricResultDetailSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # Get the test, student, and their answers from the request data
        if request and request.user.is_authenticated:
            try:
                test_id = request.data.get('test')
                answers = request.data.get('answers')

                # Delete the previous test result for the student, if any
                TestResult.objects.filter(user=request.user.student).filter(test_id=test_id).delete()

                # Save the test result for the student
                test_result = TestResult.objects.create(
                    user=request.user.student, test_id=test_id, score=0
                )

                # Calculate the score for the test
                total_score = 0
                for answer in answers:
                    question_id = answer.get('question_id')
                    answer_id = answer.get('answer_id')

                    # Get the weightage of the selected answer for the question
                    weightage = Answer.objects.get(id=answer_id).weightage

                    # Add the weightage to the total score
                    total_score += weightage

                    # Save the test result detail
                    result_detail = TestResultDetail(
                        result=test_result,
                        question_id=question_id,
                        answer_id=answer_id
                    )
                    result_detail.save()

                # Update the score for the test result
                test_result.score = total_score
                test_result.save()

                response_data = {
                    'message': 'Quiz taken successfully',
                    'status': True,
                    'test_id': test_result.id
                }
                return Response(response_data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'message': str(e), 'status': False}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Please login'}, status=status.HTTP_400_BAD_REQUEST)


class TestTypeView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset= TestType.objects.all()
    serializer_class=TypeSerializer

    
class TestResultDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TestResultDetailSerializer

    def get(self, request, format=None):
        try:
            user = request.user.student
            test_name = request.query_params.get('name')
            test = PsychometricTest.objects.get(name=test_name)
            test_result = TestResult.objects.filter(test=test, user=user).first()
            
            if test_result:
                result_details = TestResultDetail.objects.filter(result=test_result)
                question_type_scores = result_details.values('question__type__type').annotate(total_score=Sum('answer__weightage'))
                
                serialized_data = []
                for score in question_type_scores:
                    question_type = score['question__type__type']
                    total_score = score['total_score']
                    
                    # Get the description and test name from the related models
                    description = result_details.filter(question__type__type=question_type).first().question.type.description
                    test_name = test_result.test.name
                    test_type_id = result_details.filter(question__type__type=question_type).first().question.type.pk
                    
                    data = {
                        'id': test_type_id,
                        'test_name': test_name,
                        'question_type': question_type,
                        'score': total_score,
                        'description': description
                    }
                    serialized_data.append(data)

                return Response(serialized_data)
            else:
                return Response({'message': 'No result found'})
        
        except Exception as e:
            return Response({'message': str(e), 'status': False}, status=status.HTTP_400_BAD_REQUEST)

        
class ResultDetailAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TestResultDetailSerializer

    def retrieve(self, request, id):
        result_id = id  # Get the test result ID from the URL parameter

        try:
            result_details = TestResultDetail.objects.filter(result_id=result_id).values('result__test__name', 'question__type__type', 'question__type__description').annotate(total_score=Sum('answer__weightage'))

            # Create a dictionary with question type as key and total score as value
            result_data = {result['question__type__type']: result for result in result_details}

            # Create a list of serialized data for each question type, including the test name, question type, score, and description
            serialized_data = []
            for question_type, result in result_data.items():
                question_type_id = TestType.objects.filter(type=question_type).first().pk
                data = {
                    'id': question_type_id,
                    'test_name': result['result__test__name'],
                    'question_type': question_type,
                    'score': result['total_score'],
                    'description': result['question__type__description']
                }
                serialized_data.append(data)

            return Response(serialized_data)
        except TestResultDetail.DoesNotExist:
            return Response({'message': 'Test result not found'}, status=status.HTTP_404_NOT_FOUND)
        

class CareerIdeaView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CareerIdeaSerializer

    def get(self, request, type_id):
        try:
            career_idea = CareerIdea.objects.get(type=type_id)
            serialized_data = self.serializer_class(career_idea).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'message': 'type ID not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e), 'status': False}, status=status.HTTP_400_BAD_REQUEST)

    
class ChoiceIdeaView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ChoiceIdeaSerializer

    def get(self, request, type_id):
        try:
            career_idea = ChoiceIdea.objects.get(type=type_id)
            serialized_data = self.serializer_class(career_idea).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        except ObjectDoesNotExist:
            return Response({'message': 'type ID not found'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'message': str(e), 'status': False}, status=status.HTTP_400_BAD_REQUEST)


class StudyTipsView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StudyTipsSerializer

    def get(self, request, type_id):
        try:
            study_tips = StudyTips.objects.filter(type=type_id).order_by('id')[:5]

            if not study_tips.exists():
                return Response({'message': 'type ID not found'}, status=status.HTTP_400_BAD_REQUEST)

            serialized_data = self.serializer_class(study_tips, many=True).data
            return Response(serialized_data, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response({'message': str(e), 'status': False}, status=status.HTTP_400_BAD_REQUEST)
