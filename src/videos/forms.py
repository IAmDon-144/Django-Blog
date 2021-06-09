from django import forms
from .models import Video

class Video_Model_From(forms.ModelForm):
    class Meta:
        model = Video
        fields=['title','content','video']