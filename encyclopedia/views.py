from django import forms
from django.shortcuts import redirect, render 
from django.http import HttpResponseRedirect
from markdown import markdown
from . import util
from django import forms
import re
from . import forms
from django.forms.widgets import Textarea


def index(request):
    if request.GET.get('q') != None:
        return display_content(request, request.GET.get('q'))
    else:
        return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries(), })

def display_content(request, title):
    if util.get_entry(title):
        if request.method == 'POST':
            return HttpResponseRedirect(f'{title}/edit')
        content = markdown(util.get_entry(title))
        return render(request, 'encyclopedia/content.html', {
            'title':title, 'content': content})
    else:
        request_pattern = re.compile(request.GET.get('q'), re.IGNORECASE)
        item_list = util.list_entries()
        item_list = list(filter(request_pattern.search, item_list))
        if item_list:
            return render(request, 'encyclopedia/search.html', {
                'entries': item_list})
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
            else:
                exist = False
        return render(request, 'encyclopedia/createnewpage.html', {'form': form.as_p(), 'exist': exist})        
        
    return render(request, 'encyclopedia/createnewpage.html', {'form': forms.CreateNewPage().as_p(), 'exist': exist})

def editpage(request, title):
    exist = True
    return render(request, 'encyclopedia/createnewpage.html', {'form': forms.CreateNewPage().as_p(), 'exist': exist})