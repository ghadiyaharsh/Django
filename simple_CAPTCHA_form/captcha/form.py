from django import forms

class CaptchaForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    captcha = forms.IntegerField(label='what is 3 + 4?', help_text='Please answer the question to prove you are not a robot.')
    
    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if captcha_value != 7:
            raise forms.ValidationError("Incorrect answer. Please try again.")
        return captcha_value
