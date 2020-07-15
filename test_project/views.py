from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    gettext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ''
        for char in gettext:
            if char not in punctuations:
                analyzed += char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        gettext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        analyzed = ''
        for char in gettext:
            analyzed += char.upper()
        params = {'purpose': 'Changed to Upper Case',
                  'analyzed_text': analyzed}
        gettext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == 'on':
        analyzed = ''
        for char in gettext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'Removed New line Character',
                  'analyzed_text': analyzed}
        gettext = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == 'on':
        analyzed = ''
        for index, char in enumerate(gettext):
            if not(gettext[index] == ' ' and gettext[index+1] == ' '):
                analyzed += char
        params = {'purpose': 'Removed extra space',
                  'analyzed_text': analyzed}
        gettext = analyzed

    if removepunc != 'on' and fullcaps != 'on' and extraspaceremover != 'on' and charcount != 'on' and newlineremover != 'on':
        return HttpResponse('<h1>Error!!Please select any option.</h1>')
    return render(request, 'analyze.html', params)
