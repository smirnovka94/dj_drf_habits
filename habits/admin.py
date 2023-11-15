from django.contrib import admin

from habits.models import Habit

admin.site.register(Habit)

class HabitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','id_user','is_pleasant_habit','award','is_public')
    list_filter = ('id_user',)
