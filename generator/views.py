from django.shortcuts import render

import random

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

def passwd(request):
    # a~z
    pw_word = [chr(i) for i in range(97, 123)] # ASCII CODE
    # A~Z (大寫)
    if request.GET.get('uppercase'):
        pw_word += [chr(i) for i in range(65, 91)]
    # 數字
    if request.GET.get('number'):
        pw_word += [chr(i) for i in range(48, 58)]
    # 符號
    if request.GET.get('special'):
        pw_word += [chr(i) for i in range(33, 48)]

    length = request.GET['length']
    input_length = request.GET.get('input_length')
    uppercase = request.GET.get('uppercase')

    length = input_length if input_length else length

    password = ''.join([random.choice(pw_word) for i in range(eval(length))])

    return render(request, 'passwd.html', {'password': password})