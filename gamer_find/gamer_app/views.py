from __future__ import print_function
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import bcrypt
from django.contrib import messages 
from .models import *
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
# Create your views here.
def index(request):
    return render(request, 'login.html')

def homepage(request, user_id):
    context = {
        'all_games' : Game.objects.all(),
        'all_stores' : Merchant.objects.all()
    }
    return render(request, 'homepage.html', context)
# def main(request, store_id):
#     # """Shows basic usage of the Google Calendar API.
#     # Prints the start and name of the next 10 events on the user's calendar.
#     # """
#     creds = None
#     # The file token.pickle stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.pickle'):
#         with open('token.pickle', 'rb') as token:
#             creds = pickle.load(token)
#     # If there are no (valid) credentials available, let the user log in.
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
#         # Save the credentials for the next run
#         with open('token.pickle', 'wb') as token:
#             pickle.dump(creds, token)

#     service = build('calendar', 'v3', credentials=creds)

#     # Call the Calendar API
#     now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
#     print('Getting the upcoming 10 events')
#     events_result = service.events().list(calendarId='primary', timeMin=now,
#                                         maxResults=10, singleEvents=True,
#                                         orderBy='startTime').execute()
#     events = events_result.get('items', [])

#     if not events:
#         print('No upcoming events found.')
#     for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])
#     if __name__ == '__main__':
#         main()
    # return redirect('/store/'+str(store_id))

    
def storelogin(request):
    return render(request, 'storelogin.html')

def storepage(request, store_id):
    context = {
        'all_stock' : Stock.objects.all(),
        'store' : Merchant.objects.get(id=store_id)
    }
   
    return render(request, 'storepage.html', context)

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
    return redirect('/')

def regstore(request):
    errors = Merchant.objects.validator(request.POST)
    if len(errors) > 0:
        for key, v in errors.items():
            messages.error(request, v)
        return redirect('/store')
    if request.method == 'POST':
        hashed_pw = bcrypt.hashpw(request.POST['pw'].encode(), bcrypt.gensalt()).decode()
        new_store = Merchant.objects.create(store = request.POST['store'], email = request.POST['email'], zipcode = request.POST['zip'], pw = hashed_pw)
        print(new_store)
        request.session['store'] = new_store.store
        request.session['id'] = new_store.id 
        return redirect('/store/' + str(new_store.id))
    return redirect('/store')

def logstore(request):
    logged_store = Merchant.objects.filter(email = request.POST['email'])
    if len(logged_store) > 0:
        logged_store = logged_store[0]
        if bcrypt.checkpw(request.POST['pw'].encode(), logged_store.pw.encode()):
            request.session['store'] = logged_store.store
            request.session['id'] = logged_store.id
        return redirect('/store/' + str(logged_store.id))
    return redirect('/store')

def addgame(request, user_id):
    if request.method == 'POST':
        new_cover = request.FILES['cover']
        fs = FileSystemStorage()
        game_cover = fs.save(new_cover.name, new_cover)
        new_game = Game.objects.create(title=request.POST['title'], player=request.POST['player'], gametype=request.POST['type'], desc=request.POST['desc'], cover=game_cover, poster=User.objects.get(id=user_id))
        print(new_game)
    
    return redirect('/user/' + str(user_id))

def logout(request):
    request.session.clear()
    return redirect('/')

def deletegame(request, game_id, user_id):
    delete_game = Game.objects.get(id=game_id)
    delete_game.delete()
    return redirect('/user/' + str(user_id))

def deletestock(request, stock_id, store_id):
    delete_stock = Stock.objects.get(id=stock_id)
    delete_stock.delete()
    return redirect('/store/' + str(store_id))

def addfeatured(request, store_id):
    if request.method == 'POST':
        new_cover = request.FILES['cover']
        fs = FileSystemStorage()
        game_cover = fs.save(new_cover.name, new_cover)
        new_game = Stock.objects.create(title=request.POST['title'], player=request.POST['player'], gametype=request.POST['type'], desc=request.POST['desc'], cover=game_cover, vendor=Merchant.objects.get(id=store_id))
        print(new_game)
    return redirect('/store/' + str(store_id))

def search(request, user_id):
    if request.method == 'POST':
        zipcode_search = request.POST['zipcode']
        request.session['results'] = zipcode_search
    return redirect('/user/' + str(user_id))

def gotostore(request, store_id, user_id):
    request.session['user'] = user_id
    # request.session['store'] = store_id
    return redirect('/store/' + str(store_id))

def faves(request, store_id):
    patroner = User.objects.get(id=request.session['id'])
    store_faved = Merchant.objects.get(id=store_id)
    store_faved.patron.add(patroner)
    return redirect('/store/' + str(store_id))

def favgame(request, stock_id, store_id):
    gamer = User.objects.get(id=request.session['id'])
    favgame = Stock.objects.get(id=stock_id)
    favgame.fav.add(gamer)
    return redirect('/store/' + str(store_id))


