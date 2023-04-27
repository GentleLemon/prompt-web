from django.forms import ModelForm

from .models import Prompt


class PromptForm(ModelForm):
    class Meta:
        model = Prompt
        fields = (
            'category', 
            'title', 
            'description', 
            'position_salary', 
            'position_location', 
            'company_name',
            'company_location',
            'company_email',
        )
