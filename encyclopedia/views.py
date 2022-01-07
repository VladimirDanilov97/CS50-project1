from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from markdown import markdown
from . import util
from django import forms
import re
def index(request):
    
    if request.GET.get('q') != None:
        return content(request, request.GET.get('q'))
    else:
        return render(request, "encyclopedia/index.html", {
    "entries": util.list_entries(), })

def content(request, title):
    if util.get_entry(title):
        content = markdown(util.get_entry(title))
        
        return render(request, 'encyclopedia/content.html', {
            'title':title, 'content': content})
    
    else:
        request_pattern = re.compile(request.GET.get('q'))
        item_list = util.list_entries()
        print(item_list)
        
        for item in item_list:
            print(item, request_pattern.search(item))
            if request_pattern.search(item) == None:
                item_list.remove(item)

        if item_list:
            return render(request, 'encyclopedia/search.html', {
                'entries': item_list})
    
    return render(request, 'encyclopedia/error404.html', {
        'title':title})