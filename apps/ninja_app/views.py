from django.shortcuts import render, redirect
import random
from datetime import datetime
from json import dumps

# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'ninja_app/index.html')

def chance():
    chance = random.randrange(0,2)
    if chance == 1:
        return True
    else:
        return False




def giveGold(request):
    request.session['somedate'] = str( datetime.now() )
    print request.session['somedate'], 'im time'
    if request.POST['action'] == 'farm':
        request.session['action'] = request.POST['action']
        randomNum = random.randrange(10,21)
        request.session['gold'] += randomNum
        request.session['activities'].insert(0, (randomNum, request.session['action'], request.session['somedate']))
    elif request.POST['action'] == 'cave':
        randomNum = random.randrange(5,11)
        request.session['gold'] += randomNum
        request.session['activities'].insert(0, (randomNum, request.POST['action'], request.session['somedate']))
    elif request.POST['action'] == 'house':
        randomNum = random.randrange(2,6)
        request.session['gold'] += randomNum
        request.session['activities'].insert(0, (randomNum, request.POST['action'], request.session['somedate']))
    elif request.POST['action'] == 'casino':
        if chance() == True:
            randomNum = random.randrange(0,51)
            request.session['gold'] += randomNum
            bet = 'won'
        else:
            randomNum = random.randrange(0,51)
            request.session['gold'] -= randomNum
            if request.session['gold'] < 0:
                request.session['gold'] = 0
            bet = 'lost'
        request.session['activities'].insert(0, (randomNum, request.POST['action'], request.session['somedate'], bet))
    return redirect('/')

def reset(request):
    request.session.clear() #this will clear the dic
    return redirect('/')
