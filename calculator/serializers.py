from rest_framework import serializers
from .models import Subject,Level,SubjectGrade, UserPoints
from rest_framework.exceptions import  ValidationError


        
class  SubjectSerializer(serializers.ModelSerializer):
    level=serializers.SerializerMethodField(read_only=True)
    def get_level(self, obj):
        temp=Subject.objects.filter(id=obj.id).values('level__subjectlevel','level__id')
        return (temp)

    class Meta:
        model=Subject
        fields=['id','name','level']
        


class SubjectGradeSerializer(serializers.ModelSerializer):
    total_points = serializers.SerializerMethodField()
    bonus_points = serializers.SerializerMethodField()

    class Meta:
        model = SubjectGrade
        fields = ['grade', 'pk', 'point', 'total_points', 'bonus_points']

    def get_total_points(self, obj):
        subject = obj.subject
        grade = obj.grade
        if grade in ['H7', 'H8'] or grade in ['h7', 'h8'] :  # Exclude additional points for H7 and H8 grades
            total_points = obj.point
        else:
            total_points = obj.point
            if subject.is_additional_marks_allowed and subject.additional_marks:
                total_points += subject.additional_marks
        return total_points

    def get_bonus_points(self, obj):
        subject = obj.subject
        grade = obj.grade
        bonus_points = 0
        if grade in ['H7', 'H8'] or grade in ['h7', 'h8'] :  # Exclude additional points for H7 and H8 grades
            bonus_points = 0
        else:
            if subject.is_additional_marks_allowed and subject.additional_marks:
                bonus_points = subject.additional_marks
        return bonus_points

class SubjectGradesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubjectGrade
        fields = ['id', 'grade', 'level','subject']

class SubjectsSerializer(serializers.ModelSerializer):
    level = SubjectGradesSerializer(many=True, read_only=True)

    class Meta:
        model = Subject
        fields = ['name', 'level']

class UserPointsSerializer(serializers.ModelSerializer):
    grades = SubjectGradesSerializer(many=True, read_only=True)

    class Meta:
        model = UserPoints
        fields = ['id', 'grades','total_points']

    