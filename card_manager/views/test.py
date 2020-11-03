from django.shortcuts import render


def test_page(request):
    return render(request, 'card_manager/test.html', locals())