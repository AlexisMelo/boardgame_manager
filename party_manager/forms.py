from django import forms


class RejoindrePartyForm(forms.Form):
    nom_party = forms.CharField(label="Nom de la partie", max_length=20)
