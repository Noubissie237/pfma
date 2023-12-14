from django import forms
from .models import Users

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = [
            "nom",
            "email",
            "genre",
            "pwd"
        ]

        labels = {
            "nom" : "Nom",
            "email" : "E-mail",
            "genre" : "Genre",
            "pwd" : "Mot de passe"
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'class': 'form-control text-primary mt-2 mb-2',})
        self.fields['email'].widget.attrs.update({'class': 'form-control text-primary mt-2 mb-2 col-4',})
        self.fields['genre'].widget.attrs.update({'class': 'form-control mt-2 mb-2 col-4',})
        self.fields['pwd'].widget.attrs.update({'class': 'form-control',})
      