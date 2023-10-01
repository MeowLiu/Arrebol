from django.shortcuts import render


def hero(request):
    """
    Go to the page hero
    :param request:
    :return: renden
    """
    return render(request, "hero.html")
