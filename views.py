from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

def index(request):
    return render(request, 'presentation/points.html', {
        'title': 'Why?',
        'points': [
            {'title': 'I want a nice media player'},
            {'title': 'XBMC is HUGE'},
            {'title': 'XBMC is C++', 'subtitle': '(plugins in python not good enough)'},
            {'title': 'XBMC has bugs'},
            {'title': 'I don\'t ever want to write C++ again'},
        ],
        'next': '/presentation/2/',
    })

def part_2(request):
    return render(request, 'presentation/points.html', {
        'title': 'CMi Architecture',
        'points': [
            {'title': 'Django Backend'},
            {'title': 'Objective-C Frontend'},
            {'title': 'Video playing via VLCKit'},
        ],
        'next': '/presentation/3/',
    })

def part_3(request):
    return render(request, 'presentation/points.html', {
        'title': 'CMi Features',
        'points': [
            {'title': 'AVI, MKV, H.264, etc', 'subtitle': '(everything VLC supports)'},
            {'title': 'Apple Remote, Keyboard and Mouse navigation'},
            {'title': 'Automatically discovers files in ~/Downloads'},
            {'title': 'Episode names from thetvdb.com'},
            {'title': 'Remembers position', 'subtitle': '(even if you lose power)'},
            {'title': 'Retina/HiDPI'},
            {'title': 'Doctor Who!'},
            {'title': 'Tiny code base', 'subtitle': '(937 lines python, 961 lines js, 815 lines ObjC)'},
            {'title': 'Weather :P'},
        ],
        'next': '/presentation/4/',
    })

def part_4(request):
    return render(request, 'presentation/screenshot.html', {
        'title': 'This presentation is a CMi plugin!',
        'image': '/presentation/static/screenshot.png',
        'next': '/presentation/5/',
    })

def part_5(request):
    return render(request, 'presentation/points.html', {
        'title': 'CMi: Getting Involved',
        'points': [
            {'title': 'github.com/boxed/cmi'},
            {'title': 'MIT License'},
            {'title': 'boxed@killingar.net'},
        ],
    })