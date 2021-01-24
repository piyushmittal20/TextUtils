from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params = {'name': 'piyush'}
    return render(request, "index.html")


def contact(request):
    return render(request, "contact.html")


def analyze(request):
    text = request.GET.get("text", "default")

    removepunc = request.GET.get("removepunc", "off")
    uppercase = request.GET.get("uppercase", "off")
    newlineremover = request.GET.get("newlineremover", "off")
    numremover = request.GET.get("numremover", "off")

    if uppercase == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper()
        params = {"analyzed_text": analyzed}
        text = analyzed

    if removepunc == "on":
        analyzed = ""
        punctuations = """!()-[]{};:'",<>./?@#$%^&*_~"""
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        text = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        text = analyzed

    if numremover == "on":
        analyzed = ""
        numbers = "0123456789"
        for char in text:
            if char not in numbers:
                analyzed = analyzed + char
        params = {"analyzed_text": analyzed}
        text = analyzed

    if (
        removepunc != "on"
        and uppercase != "on"
        and newlineremover != "on"
        and numremover != "on"
    ):
        return HttpResponse(
            "<h4>Please Select at least on command or if you don't want to make your text beautiful, so why would you come on textutils.com</h4>"
        )

    return render(request, "analyze.html", params)
