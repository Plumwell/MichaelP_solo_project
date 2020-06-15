from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import bcrypt
from django.contrib import messages 
from .models import *

# Create your views here.
def index(request):
    return render(request, 'login.html')

def homepage(request, user_id):
    context = {
        'all_games' : Game.objects.all()
    }
    return render(request, 'homepage.html', context)

def storelogin(request):
    return render(request, 'storelogin.html')

def storepage(request, store_id):
    return render(request, 'storepage.html')

def reguser(request):
    errors = User.objects.validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    if request.method == 'POST':
        hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(username = request.POST['username'], name = request.POST['name'], email = request.POST['email'], zipcode = request.POST['zip'],pw = hashed_pw)
        print(new_user)
        request.session['username'] = new_user.username
        request.session['name'] = new_user.name
        request.session['id'] = new_user.id 
        return redirect('/user/' + str(new_user.id))

def loguser(request):
    logged_user = User.objects.filter(email = request.POST['email'])
    if len(logged_user) > 0:
        logged_user = logged_user[0]
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_user.pw.encode()):
            request.session['username'] = logged_user.username
            request.session['name'] = logged_user.name
            request.session['id'] = logged_user.id
        return redirect('/user/' + str(logged_user.id))

def regstore(request):
    errors = Merchant.objects.validator(request.POST)
    if len(errors) > 0:
        for k, v in errors.items():
            messages.error(request, v)
        return redirect('/store')
    if request.method == 'POST':
        hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_store = Merchant.objects.create(store = request.POST['store'], email = request.POST['email'], zipcode = request.POST['zip'], pw = hashed_pw)
        print(new_store)
        request.session['store'] = new_store.store
        request.session['id'] = new_store.id 
        return redirect('/store/' + str(new_store.id))

def logstore(request):
    logged_store = Merchant.objects.filter(email = request.POST['email'])
    if len(logged_store) > 0:
        logged_store = logged_store[0]
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_store.pw.encode()):
            request.session['store'] = logged_store.store
            request.session['id'] = logged_store.id
        return redirect('/store/' + str(logged_store.id))

def addgame(request, user_id):
    if request.method == 'POST':
        new_cover = request.FILES['cover']
        fs = FileSystemStorage()
        game_cover = fs.save(new_cover.name, new_cover)
        new_game = Game.objects.create(title=request.POST['title'], player=request.POST["player"], gametype=request.POST['type'], desc=request.POST['desc'], cover=game_cover)
        print(new_game)
    
    return redirect('/user/' + str(user_id))

def logout(request):
    request.session.clear()
    return redirect('/')

def deletegame(request, game_id, user_id):
    delete_game = Game.objects.get(id=game_id)
    delete_game.delete()
    return redirect('/user/' + str(user_id))

def addfeatured(request, store_id):
    if request.method == 'POST':
        new_game = Game.objects.create(title=request.POST['title'], player=request.POST["player"], gametype=request.POST['type'], desc=request.POST['desc'], poster=request.POST['request.session.id    '])
        print(new_game)
    return redirect('/user/' + str(store_id))