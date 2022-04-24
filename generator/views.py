from django.shortcuts import render
from django.http import HttpResponse
import random 

def cc (text):
    return 'generator/' + text + '.html'

# Create your views here.

def home (req):
    return render(req, cc('home'))

def about (req):
    return render(req, cc('about'))

def password (req):
    chars = list('abcdefghijklmñnopqrstuvwxyz')
    generator = ''
    try:
        length = int(req.GET.get('length'))
    except:
        length = 'Error: longitud introducida no correcta.'

    if req.GET.get('upper'):
        chars.extend(list('ABCDEFGHIJKLMÑOPQRSTUWXYZ'))

    if req.GET.get('numbers'):
        chars.extend(list('1234567890'))

    if req.GET.get('sc'):
        chars.extend(list('-_#@&$%<>'))

    if type(length) == str:
        generator = length
    else:
        if length > 10000:
            generator = 'Error: longitud muy grande.'
        else:
            for i in range(length):
                generator += random.choice(chars)

    return render(req, cc('password'), {'password': generator})

