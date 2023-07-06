from django.urls import path
from . import views

urlpatterns = [
    #path('', views.home, name='homePage'),
    #path('', views.thepage, name='homePage'),
    path('signup/',views.signUp, name='signUp'),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('competitions/', views.competitions, name="competitions"),
    path('games/', views.games, name="games"),
    path('game/', views.game, name="game"),
    path('addgame/', views.addNewGame, name="addgame"),
    path('incompletegames/', views.checkExistingGames, name="incompletegame"),
    path('updategame/', views.updateGame, name="updategame"),
    path('getgames/', views.gameList, name="getgames"),
    path('adminupdate/', views.getAdminInfo, name="adminupdate"),
    path('test/', views.thepage, name="newHomePage"),
    path('', views.mainpage, name="newpage")
]