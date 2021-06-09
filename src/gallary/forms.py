from django import forms
from django.forms import fields
from .models import images,Comment,Catagory
from djrichtextfield.widgets import RichTextWidget


class Post_Model_From(forms.ModelForm):
    class Meta:
        model = images
        fields=['title','content','image','image1','image2','image3','category','subCat']
        content = forms.CharField(widget=RichTextWidget())





class CommentModelForm(forms.ModelForm):
    # obj = images.objects.all()
    # print(obj)
    # lst = []
    # for i in obj:
    #     lst.append(i.id)
    # print(lst)

    body = forms.CharField(label='',
                widget=forms.TextInput(attrs={'placeholder':'Add a comment...','class':'bodyvalueComm',}))


    class Meta:
        model = Comment
        fields = ('body',)

class CategoryModelform(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ['name','image']