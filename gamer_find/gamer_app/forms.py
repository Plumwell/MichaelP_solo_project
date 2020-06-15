from django import forms 
from .models import *
  
class GameForm(forms.ModelForm): 
  
    class Meta: 
        model = Cover 
        fields = ['title', 'player', 'gametype', 'desc', 'fav', 'cover'] 
