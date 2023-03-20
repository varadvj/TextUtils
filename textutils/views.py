#newly created file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name' : 'Varad', 'place' : 'USA'}
    return render(request, 'index.html', params)
    #return HttpResponse('<h1>Hello</h1> <a href = "https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Code with harry</a>')

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    #check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    #check which checkbox is on
    #logic for remove punctuations
    if removepunc == "on" :
        punctautions = '''"!{}[]()!@#$*_%^&'''

        analyzed = ""
        for char in djtext:
            if char not in punctautions:
                analyzed = analyzed + char
        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #logic for changing to Uppercase
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char !="\n" and char !="\r":
                analyzed = analyzed + char

        params = {'purpose': 'New line remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index + 1] == " ":
                pass
            else:
                analyzed = analyzed + char

        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(removepunc != "on" and fullcaps != "on" and newlineremover != "on" and spaceremover != "on") :
        return HttpResponse("Oopss ! Error.. Please select the option")

    return render(request, 'analyze.html', params)