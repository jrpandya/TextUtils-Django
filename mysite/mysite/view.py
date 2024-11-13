# I have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    spaceremover = request.POST.get('spaceremover','off')
    if removepunc == "on":
        Punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=''
        for char in djtext:
            if char not in Punctuations:
                analyzed = analyzed + char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed

    if fullcaps == "on" :
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Change to uppercase','analyzed_text':analyzed}
        djtext=analyzed

    if newlineremover == "on" :
        analyzed = ""
        for char in djtext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params = {'purpose':'Remove New Lines','analyzed_text':analyzed}
        djtext=analyzed

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            # Check if the current character is not a space or if it's the last character
            if not (char == " " and (index + 1 < len(djtext) and djtext[index + 1] == " ")):
                analyzed += char
        params = {'purpose': 'Remove Extra Spaces', 'analyzed_text': analyzed}
        
    if(removepunc!="on" and newlineremover!="on" and fullcaps !="on" and spaceremover !="on"):
        return HttpResponse("please select any operation and try again")
        #Analyze the text
    return render(request,'analyze.html',params)
   