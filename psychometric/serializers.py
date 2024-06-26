from rest_framework import serializers
from .models import PsychometricTest, TestType, Question, Answer, TestResult, TestResultDetail, CareerIdea, ChoiceIdea, StudyTips
from django.db.models import Sum
from users.models import Student

class StudentSerializer(serializers.ModelSerializer):
    model=Student
    fields=['first_name','last_name','address','eircode']

class TypeSerializer(serializers.ModelSerializer):
    score = serializers.SerializerMethodField()
    class Meta:
        model=TestType
        fields=['id','type', 'score']
        extra_kwargs={'required':False}

    def get_score(self,obj):
        """Fetch score by test type"""
        type=TestType.objects.get(id=obj.id)
        user_obj=self.context["request"].user
        std_obj= Student.objects.get(user=user_obj.id)
        ques_obj= Question.objects.filter(type=type)
        res=TestResultDetail.objects.filter(result__user=std_obj).filter(question__type__type=type.type).aggregate(total=Sum("answer__weightage"))

        return res
    

class AnswerSerializer(serializers.ModelSerializer):
    answer_id = serializers.IntegerField(source='id', read_only=True)
    class Meta:
        model=Answer
        fields=['answer_id', 'answer', 'weightage']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, source='answer')
    question_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model=Question
        fields=['question_id', 'type', 'question', 'answers']


class PsychometricTestSerializer(serializers.ModelSerializer):
    questions = serializers.SerializerMethodField()
    test_id = serializers.IntegerField(source='id', read_only=True)

    class Meta:
        model = PsychometricTest
        fields = ['test_id', 'name', 'intro', 'questions']

    def get_questions(self, obj):
        print("work")
        def sort_answers(answer):
            return -answer.weightage

        sorted_questions = []
        for question in obj.question.all():
            answers = question.answer.all()  # Use 'answer' instead of 'answers'
            sorted_answers = sorted(answers, key=sort_answers)

            # Serialize the answers using AnswerSerializer
            serialized_answers = AnswerSerializer(sorted_answers, many=True).data

            sorted_question = {
                'question_id': question.id,
                'type': question.type.id,
                'question': question.question,
                'answers': serialized_answers,  # Use serialized answers
            }
            sorted_questions.append(sorted_question)

        return sorted_questions


class PsychometricResultDetailSerializer(serializers.ModelSerializer):
    result = serializers.IntegerField(required=False)
    question = QuestionSerializer(read_only=True)
    answer = AnswerSerializer(read_only=True)

    class Meta:
        model = TestResultDetail
        fields = ['id','result', 'question', 'answer']


class PsychometricStatusSerializer(serializers.ModelSerializer):
    complete = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    total_score = serializers.SerializerMethodField()
    test_results = serializers.SerializerMethodField()

    class Meta:
        model = PsychometricTest
        fields = ['id', 'name','intro', 'complete', 'score', 'total_score','test_results']

    def get_complete(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Check if the user has completed the quiz
            result = TestResult.objects.filter(user__user__email=request.user.email, test=obj).last()
            if result:
                return True
        return False

    def get_score(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Get the user's score for the quiz
            result = TestResult.objects.filter(user__user__email=request.user.email, test=obj).last()
            if result:
                return result.score
        return None

    def get_total_score(self, obj):
        questions = obj.question.all()
        total_score = sum([max(question.answer.all(), key=lambda x: x.weightage).weightage for question in questions])
        return total_score
    
    def get_test_results(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            # Get all test results for the user
            results = TestResult.objects.filter(user__user__email=request.user.email, test=obj)
            if results:
                test_results = []
                for result in results:
                    question_type_scores = TestResultDetail.objects.filter(result=result).values('question__type__type').annotate(total_score=Sum('answer__weightage'))

                    question_scores = []
                    for score in question_type_scores:
                        score_data = {
                            'question': score['question__type__type'],
                            'score': score['total_score']
                        }
                        question_scores.append(score_data)

                    test_result = {
                        'test_name': obj.name,
                        'score': result.score,
                        'question_scores': question_scores
                    }
                    test_results.append(test_result)
                return test_results
            else:
                questions = Question.objects.filter(test=obj)
                question_types = set()
                question_scores=[]
                test_results=[]
                for question in questions:
                    question_types.add(question.type.type)
                ques_list=list(question_types)
                for item in ques_list:
                    score_data={
                        'question':item,
                        'score':0
                    }
                    question_scores.append(score_data)
                test_result = {
                        'test_name': obj.name,
                        'score': 0,
                        'question_scores': question_scores
                    }
                test_results.append(test_result)
                return test_results
        return []


class TestResultDetailSerializer(serializers.ModelSerializer):
    test_name = serializers.CharField(source='result.test.name')
    question_type = serializers.CharField(source='question.type.type')
    score = serializers.IntegerField(source='answer.weightage')
    description = serializers.CharField(source='question.type.description')

    class Meta:
        model = TestResultDetail
        fields = ['test_name', 'question_type', 'score', 'description']


class CareerIdeaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CareerIdea
        fields = ['id', 'type', 'idea']


class ChoiceIdeaSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ChoiceIdea
        fields = ['id', 'type', 'idea']


class StudyTipsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = StudyTips
        fields = ['id', 'type', 'description']
