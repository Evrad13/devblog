from django import forms

#classe pour le formulaire de connexion

class LoginForm(forms.Form):

    username = forms.CharField(max_length=63, label="Nom d'utilisateur")
    
    password = forms.CharField(max_length=63, widget=forms.PasswordInput, label="mot de passe")