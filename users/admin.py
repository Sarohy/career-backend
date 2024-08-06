from django.contrib import admin
from .models import Student, School, User, Counselor


class StudentAdminDisplay(admin.ModelAdmin):
    list_display = ['__str__', 'firstname_and_lastname', 'school', 'dob', 'profile_image', 'cv_completed']

    def firstname_and_lastname(self, obj):
        return "%s %s" % (obj.first_name, obj.last_name)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_counselor:
            counselor = Counselor.objects.get(user=request.user)
            return qs.filter(school=counselor.school)
        return qs


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserCreationForm, UserChangeForm

class UserAdmin(BaseUserAdmin):
    model = User
    add_form = UserCreationForm
    form = UserChangeForm
    list_display = ('email', 'is_staff', 'is_active', 'is_counselor')
    list_filter = ('is_staff', 'is_active', 'is_counselor')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'is_counselor')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'username', 'is_counselor'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


class CounselorAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'school']
    search_fields = ['user__email', 'school__school']
    list_filter = ['school']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['user'].queryset = User.objects.order_by('email')
        form.base_fields['school'].queryset = School.objects.order_by('school')
        return form


admin.site.register(Counselor, CounselorAdmin)
admin.site.register(Student,StudentAdminDisplay)
admin.site.register(School)
admin.site.register(User, UserAdmin)

