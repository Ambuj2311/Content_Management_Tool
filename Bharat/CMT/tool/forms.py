from django import forms
from .models import content

class contentform(forms.ModelForm):
    
    class Meta:
        model = content
        fields=['name','Image','video','Article'
            
        ]
widgets = {
            'name':forms.TextInput(attrs={
                'class': 'form-control',
                }),
            #'DOB':forms.TextInput(attrs={'class':'form-control'}),
            #'Email':forms.TextInput(attrs={'class':'form-control'}),
            #'Gender':forms.TextInput(attrs={'class':'form-control'}),
            #'Contact_no':forms.TextInput(attrs={'class':'form-control'}),
            'Image':forms.ImageField(required=True),
            'video':forms.FileField(required=True),
            #'Document':forms.TextInput(attrs={'class':'form-control'}),
            'Article':forms.Textarea(attrs={'class':'form-control'}),
          
        }
          
        