# I have created this file
# from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # get the text
    global params
    txt = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    capslock = request.POST.get('capslock', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # check which mode of text analyze is on
    if removepunc == "on":
        punctuations = ''' !()-{}[]:;'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'REMOVE PUNCTUATION', 'analyzed_text': analyzed}
        txt = analyzed

    if capslock == 'on':
        analyzed = ""
        for char in txt:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'CHANGE TO UPPERCASE', 'analyzed_text': analyzed}
        txt = analyzed

    if newlineremover == 'on':
        analyzed = ""
        for char in txt:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'NEW LINE REMOVING', 'analyzed_text': analyzed}
        txt = analyzed

    if extraspaceremover == 'on':
        analyzed = ""
        for index, char in enumerate(txt):
            if not (txt[index] == " " and txt[index + 1]) == " ":
                analyzed = analyzed + char
        params = {'purpose': 'EXTRA SPACE REMOVING', 'analyzed_text': analyzed}
        txt = analyzed

    if charcount == 'on':
        analyzed = ""
        count = 0
        for char in txt:
            count = count + 1
        params = {'purpose': 'CHARACTER COUNTING', 'analyzed_text': count}

    if ( removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and capslock != "on" and charcount != "on"):
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)
