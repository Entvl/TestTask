from django.forms import ModelForm, TextInput, Textarea, NumberInput, FileInput, SelectDateWidget, HiddenInput

from .models import Course

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            "user",
            "icon",
            "name",
            "description",
            "price",
            "start_date",
            "end_date"
        ]
        widgets = {
            "user" : HiddenInput(),
            "name" : TextInput(attrs={
                'class': "form-control",
                'placeholder': "Enter name of course"
            }),
            "description": Textarea(attrs={
                'class': "form-control",
                'placeholder': "Enter descritions of course"
            }),
            "price": NumberInput(attrs={
                'class': "form-input",
            }),
            "start_date": SelectDateWidget(attrs={
                'class': "form-input",
            }),
            "end_date": SelectDateWidget(attrs={
                'class': "form-input",
            }),
            "icon": FileInput(attrs={
                'class': "form-input",
            }),

        }
