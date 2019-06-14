from django.shortcuts import render, HttpResponse, redirect
import random

def index(request):
    if 'totalgold' not in request.session:
        request.session['totalgold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'totalgold' : request.session['totalgold'],
        'activities' : request.session['activities']
    }
    return render(request, 'appGold/index.html', context)
def processMoney(request):
    if request.POST['location'] == 'farm':
        gold = random.randint(10,20)
    if request.POST['location'] == 'cave':
        gold = random.randint(5, 10)
    if request.POST['location'] == 'house':
        gold = random.randint(2, 5)
    if request.POST['location'] == 'casino':
        gold = random.randint(-50, 50)
    request.session['totalgold'] += gold

    if gold < 0:
        message = (f'Entered a {request.POST["location"]} and lost {-1*gold}')
        color = 'red'
    else:
        message = (f'Earned {gold} gold from the {request.POST["location"]}!')
        color = 'green'

    activities = {
        'message': message,
        'color' : color
    }
    request.session['activities'].append(activities)
    return redirect('/')

def reset(request):
    del request.session['totalgold']
    del request.session['activities']
    return redirect('/')
