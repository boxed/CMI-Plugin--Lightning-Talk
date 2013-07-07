from django.template.loader import render_to_string
from django.conf.urls import patterns, url

def tiles():
    tiles = [
        (0, render_to_string('tile.html', {
            'url': '/presentation/',
            'image': '/site-media/tv.svg',
            'title': 'Lightning Talk',
            'content': 'Only 5 mins? Waaaaahhh!',
        })),
    ]

    return tiles

def urls():
    return patterns('presentation.views',
        (r'^presentation/$', 'index'),
        (r'^presentation/2/$', 'part_2'),
        (r'^presentation/3/$', 'part_3'),
        (r'^presentation/4/$', 'part_4'),
        (r'^presentation/5/$', 'part_5'),
        )+patterns('',
        url(r'^presentation/static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': __file__.rsplit('/', 1)[0]+'/static/'}),
    )