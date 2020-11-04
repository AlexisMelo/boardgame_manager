from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from party_manager.forms import RejoindrePartyForm


def party(request, nom_party):
    return render(request, 'party_manager/party.html', {
        'nom_party': nom_party
    })

def rejoindre_party(request):

    if request.method == 'POST':

        form = RejoindrePartyForm(request.POST)

        if form.is_valid():

            return redirect(reverse("party", args=(form.cleaned_data["nom_party"],)))

    else:
        form = RejoindrePartyForm()

    return redirect(reverse("index"), {'form': form})