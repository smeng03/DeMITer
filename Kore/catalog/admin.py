from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(User)
#admin.site.register(Psolved)
#admin.site.register(UnsolvedP)

class studentAdmin(admin.ModelAdmin):
    list_display = ('name', 'kerb', 'grad_year')
    list_filter = ('name', 'kerb', 'grad_year')

class solvedProblemAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'assign_name', 'question_number') #'displayStudent')
    list_filter = ('class_name',)

class unsolvedProblemAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'assign_name', 'question_number') #'displayStudent')
    list_filter = ('class_name',)

admin.site.register(student, studentAdmin)
admin.site.register(solvedProblem, solvedProblemAdmin)
admin.site.register(unsolvedProblem, unsolvedProblemAdmin)