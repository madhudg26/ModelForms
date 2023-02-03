from django import forms
from app.models import *

class ModelTopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'




class ModelWebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['topic_name','name']
        #help={'name':'should not an integer'}
        #labels={'topic_name':'TN'}
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea}


class AccessModeForm(forms.ModelForm):
    class Meta:
        model=AccessRecords
        fields='__all__'
            

