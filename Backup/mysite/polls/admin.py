from django.contrib import admin
from polls.models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [ 
				(None,               {'fields': ['question_text']}),
				('Date Information', {'fields': ['pub_date'], 'classes': ['collapse']}),
		]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# Register your models here.
