from django.contrib import admin
from .models import CV,Education,JuniorCertTest,Experience,Reference,Qualities,Skills,JobTitle,LeavingCertTest, Interests, AdditionalInfo
from users.models import Counselor
# Register your models here.
class CVAdminSite(admin.ModelAdmin):
    list_display=['user','is_juniorcert_test']
    search_fields = ("user__full_name",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_counselor:
            counselor = Counselor.objects.get(user=request.user)
            return qs.filter(user__school=counselor.school)
        return qs


class EducationAdminSite(admin.ModelAdmin):
    list_display=['user','year','school','examtaken']
class JuniorCertTestAdminSite(admin.ModelAdmin):
    list_display=['user','subject','level','result']
class LeavingCertTestAdminSite(admin.ModelAdmin):
    list_display=['user','subject','level','result']
class ExperienceTestAdminSite(admin.ModelAdmin):
    list_display=['user','startdate','enddate','job_title','company','city','country','description']

class ReferenceAdminSite(admin.ModelAdmin):
    list_display=['user_title','name','job_title','contact_number','organization_address','area_code','email']

class SkillsAdminSite(admin.ModelAdmin):
    list_display=['user','skill','skill_dropdown','description']

class QualitiesAdminSite(admin.ModelAdmin):
    list_display=['user','quality','interest','description']

class JobTitleAdmin(admin.ModelAdmin):
    list_display=['title']

class InterestAdmin(admin.ModelAdmin):
    list_display=['user','interests']

class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'additional_info']

admin.site.register(CV,CVAdminSite)
admin.site.register(Education,EducationAdminSite)
admin.site.register(JuniorCertTest,JuniorCertTestAdminSite)
admin.site.register(LeavingCertTest,LeavingCertTestAdminSite)
admin.site.register(Experience,ExperienceTestAdminSite)
admin.site.register(Reference,ReferenceAdminSite)
admin.site.register(Skills)
admin.site.register(Qualities,QualitiesAdminSite)
admin.site.register(JobTitle,JobTitleAdmin)
admin.site.register(Interests,InterestAdmin)
admin.site.register(AdditionalInfo, AdditionalInfoAdmin)
