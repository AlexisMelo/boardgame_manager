from django.shortcuts import render

from party_manager.forms import RejoindrePartyForm


def index(request):

    form = RejoindrePartyForm()

    return render(request, "index.html", locals())
