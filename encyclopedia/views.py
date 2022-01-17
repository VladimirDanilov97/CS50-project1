from django import forms
from django.shortcuts import redirect, render 
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 
from markdown import markdown
from . import util
from django import forms
import re
from . import forms
from django.forms.widgets import Textarea
from random import choice

def index(request):
    if request.GET.get('q') != None:
        return display_content(request, request.GET.get('q'))
    else:
        return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries(), })

def display_content(request, title):
    print(536464654464564564564664564645464)
    if util.get_entry(title):
        if request.method == 'POST':
            return HttpResponseRedirect(reverse(editpage, args=(title,)))
        content = markdown(util.get_entry(title))
        return render(request, 'encyclopedia/content.html', {
            'title':title, 'content': content})
    else:
        try:
            request_pattern = re.compile(request.GET.get('q'), re.IGNORECASE)
            item_list = list(filter(request_pattern.search, util.list_entries()))
            if item_list:
                return render(request, 'encyclopedia/search.html', {
                    'entries': item_list})
        except:
            return render(request, 'encyclopedia/error404.html', {
                'title':title})

def create_new_page(request):
    exist = True
    if request.method == 'POST':
        form = forms.CreateNewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            if not util.get_entry(title):
                content = form.cleaned_data.get('content')
                with open(f'./entries/{title}.md', 'w') as entry:
                    entry.write(f'#{title} \n')
                    entry.write(content)
                return HttpResponseRedirect(f'../{title}')
            exist = False
        return render(request, 'encyclopedia/createnewpage.html', {'form': form.as_p(), 'exist': exist})        
        
    return render(request, 'encyclopedia/createnewpage.html', {'form': forms.CreateNewPage().as_p(), 'exist': exist})

def editpage(request, title):
    print(121212121212121212121212)
    exist = True
    content = util.get_entry(title)
    if request.method == 'POST':
        form = forms.CreateNewPage(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content').replace('\n','') 
            with open(f'./entries/{title}.md', 'w') as entry:
                entry.write(content)
        return HttpResponseRedirect(reverse('content', args=(title,)))
    return render(request, 'encyclopedia/createnewpage.html', 
    {'form': forms.CreateNewPage(initial={'title': title, 'content': content}).as_p(), 'exist': exist})

def randompage(request):
    title = choice(util.list_entries())
    return HttpResponseRedirect(reverse('content', args=(title,)))
