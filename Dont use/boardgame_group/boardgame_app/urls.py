from django.urls import path
from . import views

urlpatterns =[
    path('', views.index),
    path('reguser', views.reguser),
    path('loguser', views.loguser),
    path('regstore', views.regstore),
    path('logstore', views.logstore),
    path('user/<int:user_id>', views.homepage),
    path('store/<int:store_id>', views.storepage),
    path('store', views.storelogin),
    path('user/<int:user_id>/addgame', views.addgame),
    path('store/<int:user_id>/addgame', views.addfeatured),
    path('logout', views.logout),
    path('deletegame/<int:user_id>/<int:game_id>', views.deletegame),
]