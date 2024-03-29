from django import forms
from django.core import validators
from first_app.models import User



# #custom validation
# def check_for_z(value):
#     if value[0].lower() != 'z':
#         raise forms.ValidationError("NAME NEEDS TO START WITH Z")

#nomal forms
# class FormName(forms.Form):
#     name = forms.CharField()
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label='Enter your email again')
#     text = forms.CharField(widget=forms.Textarea)
#     botcatcher = forms.CharField(required=False,widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         verify_email = all_clean_data['verify_email']
#
#         if email != verify_email:
#             raise forms.ValidationError('your email dosen\'t match!')

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('GOTCHA BOT!')
    #     return botcatcher

#Model forms
class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'
