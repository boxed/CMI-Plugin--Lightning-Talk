from django.shortcuts import render


def index(request, page='0'):
    page = int(page)
    slides = [
        ('Why?', [
            'I want a nice media player',
            'XBMC is HUGE',
            ('XBMC is C++', '(plugins in python not good enough)'),
            'XBMC has bugs',
            "I don't ever want to write C++ again",
        ]),
        ('CMi Architecture', [
            'Django Backend',
            'Objective-C Frontend',
            'Video playing via VLCKit',
        ]),
        ('CMi Features', [
            ('AVI, MKV, H.264, etc', '(everything VLC supports)'),
            'Apple Remote, Keyboard and Mouse navigation',
            'Automatically discovers files in ~/Downloads',
            'Episode names from thetvdb.com',
            ('Remembers position', '(even if you lose power)'),
            'Retina/HiDPI',
            'Doctor Who!',
            ('Tiny code base', '(937 lines python, 961 lines js, 815 lines ObjC)'),
            'Weather :P',
        ]),
        ('This presentation is a CMi plugin!', [
            ('', '', '/presentation/static/screenshot.png'),
        ]),
        ('CMi: Getting Involved', [
            'github.com/boxed/cmi',
            'MIT License',
            'boxed@killingar.net',
        ]),
    ]

    title, points = slides[page]

    def prepare_point(point):
        if type(point) == tuple:
            if len(point) > 2:
                return {'title': point[0], 'subtitle': point[1], 'image': point[2]}
            else:
                return {'title': point[0], 'subtitle': point[1]}
        else:
            return {'title': point}

    slide = {
        'title': title,
        'points': [prepare_point(x) for x in points],
        'next': '/presentation/%s/' % (page + 1),
    }

    return render(request, 'presentation/points.html', slide)
