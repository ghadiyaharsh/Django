from django import forms
import random

class CaptchaForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    QUESTION_ANSWER_PAIRS = [
        ("What is 2 + 3?", 5),
        ("What is 5 - 2?", 3),
        ("What is 4 + 4?", 8),
        ("What is 6 - 1?", 5),
        ("What is 3 + 4?", 7),
        ("What is 10 - 3?", 7),
        ("What is 2 * 3?", 6),
        ("What is 9 - 5?", 4),
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        question, answer = random.choice(self.QUESTION_ANSWER_PAIRS)
        self.fields['captcha'] = forms.IntegerField(
            label=question,
            help_text='Please answer the question to prove you are not a robot.'
        )
        self._captcha_answer = answer

    def clean_captcha(self):
        captcha_value = self.cleaned_data.get('captcha')
        if captcha_value != getattr(self, '_captcha_answer', None):
            raise forms.ValidationError("Incorrect answer. Please try again.")
        return captcha_value
