#  I have Created This File - Amey
from django.http import HttpResponse
from  django.shortcuts import render

# def index(request):
#     return HttpResponse('<h1><i>Hello Amey Welcome To Django...</i></h1>')
#
# def about(request):
#     return HttpResponse('''<h1><i>Click Here To Go To Google Web Page...</i></h1><a
# href="https://www.google.co.in/">Google Web Page</a>''')

def index(request):
    # return HttpResponse('<h1><i>Home</i></h1>')
    # dict1 ={'name' :'Amey', 'palce' :'Pune' }
    # return render(request, 'index.html', dict1)
    return render(request, 'index.html')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    print(djtext)
    capitalizerfirst = (request.POST.get('capitalizerfirst', 'off'))
    newlineremove = (request.POST.get('newlineremove', 'off'))
    spaceremove = (request.POST.get('spaceremove', 'off'))
    charcount = (request.POST.get('charcount', 'off'))

    print(capitalizerfirst)
    if capitalizerfirst =='on':
        analyzed =""
        for char in djtext:
            analyzed = analyzed + char.upper()
        param = {'purpose':'Capitalizer ALL','analysed_text':analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', param)

    if newlineremove == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n' and char!='\r':
                analyzed = analyzed + char
        param = {'purpose': 'Remove New Lines', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', param)

    if spaceremove == 'on':
        analyzed = ""
        for index ,char in enumerate(djtext):
            if djtext[index]== " "and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        param = {'purpose': 'Space Removed', 'analysed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', param)

    if charcount == 'on':
        count = 0
        for char in djtext:
            if char != " " and char!= '\n':
                count += 1
        param = {'purpose': 'Char Count', 'analysed_text': count}

    if (capitalizerfirst !='on' and newlineremove != 'on' and spaceremove != 'on' and charcount != 'on'):
        param = {'purpose': 'Sorry...', 'analysed_text': "Please On Any Switch To Analysis Your's Text..."}


    return render(request, 'analyze.html', param)

