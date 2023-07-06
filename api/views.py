from .models import Competition, Game, user, AdminGame, FixedMatchGame, BetikaJackpotGame, SportPesaJackpotGame, SubscriptionGame
from .serializers import GameSerializer, CompetitionSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
import json

# Create your views here.
@api_view(['GET'])
def getData(request):
    person = {'name':'Dennis', 'age': 28}
    return Response(person)

def signUp(request):
    context = {}
    if request.method == "POST":
        #username, email, phone, password
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        #print(f"Username is {username}, email is {email}, phone number is {phone} and password is {password}")

        # Create user
        try:
            new_user = User.objects.create_user(username, email, password)
            new_user_data = user(user_data=new_user)
            new_user_data.save()
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect(home)
            return render(request, 'api/game.html')
        except Exception as e:
            context['error'] = e
            print("error - ",e)
            # return JsonResponse({'error': str(e)})
        
        
    return render(request, 'api/authentication/signup.html', context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user, "after passing through authentication")
        if user is not None:
            # login user
            login(request, user)
            messages.success(request, 'Your account has been created successfully.')
            return redirect(home)
        # print(username, password)
        pass 
    return render(request, 'api/authentication/login.html')

def logoutUser(request):
    logout(request)
    return redirect(loginUser) 

# @login_required
def home(request):
    games = Game.objects.all()
    context = { 'games' : games }
    return render(request, 'api/homepage.html', context)

def homeTest(request):
    '''
    {
        "id": 44,
        "home_team_name": "EC Guarani",
        "away_team_name": "Santa Cruz RS",
        "home_odd": "5.17",
        "draw_odd": "3.51",
        "away_odd": "1.57",
        "game_date": 10,
        "game_month": 5,
        "game_year": 2023,
        "game_url": "https://www.betexplorer.com/soccer/brazil/campeonato-gaucho-2/ec-guarani-santa-cruz-rs/fopdb9xt/",
        "game_complete": true,
        "game_winner": "Santa Cruz RS",
        "admin_winner_choice": null,
        "game_paid": false,
        "game_vip": false,
        "game_competition": 5,
        "competition_name": "XYZ",
        "competition_image_url": "xxyyzyxhjzb",
        "game_won": "mkcdxk"
    }

    '''
    games = Game.objects.all()
    context = { 'games' : games }
    return render(request, 'api/newhomepage.html', context)

@login_required
def competitions(request):
    all_competitions = Competition.objects.all()
    context = { 'competitions': all_competitions}
    return render(request, 'api/admincompetitions.html', context)

def games(request):
    return render(request, 'api/games.html')

def game(request):
    games = Game.objects.all()
    context = { 'games' : games }

    return render(request, 'api/game.html', context)

@csrf_exempt
def addNewGame(request):
    if request.method == "POST":

        homeTeam = request.POST.get('homeTeam')
        awayTeam = request.POST.get('awayTeam')
        homeOdd = request.POST.get('homeOdd')
        drawOdd = request.POST.get('drawOdd')
        awayOdd = request.POST.get('awayOdd')
        gameDate = request.POST.get('gameDate')
        gameMonth = request.POST.get('gameMonth')
        gameYear = request.POST.get('gameYear')
        gameUrl = request.POST.get('gameUrl')
        tournament = request.POST.get('competition')

        matching_tournament = Competition.objects.filter(competition_name=tournament)
        if matching_tournament.exists():
            # Value already exists in the model
            matching_game = Game.objects.filter(game_url=gameUrl)
            if matching_game.exists():
                print("Game already exists")
            else:
                the_tournament = matching_tournament.first()
                newGame = Game(home_team_name= homeTeam, away_team_name= awayTeam, home_odd=homeOdd,
                draw_odd=drawOdd, away_odd=awayOdd, game_date=int(gameDate), game_month=int(gameMonth),
                game_year=gameYear, game_url=gameUrl, game_complete=False, game_winner="", game_competition = the_tournament)
                newGame.save()
                print(f"post request made for an existing tournament - {the_tournament.competition_name} with the teams - {homeTeam} vs {awayTeam}.")

        else:
            # Value does not exist in the model
            matching_game = Game.objects.filter(game_url=gameUrl)
            if matching_game.exists():
                print("Game already exists")
            else:
                new_tournament = Competition(competition_name= tournament)
                new_tournament.save()
                newGame = Game(home_team_name= homeTeam, away_team_name= awayTeam, home_odd=homeOdd,
                draw_odd=drawOdd, away_odd=awayOdd, game_date=int(gameDate), game_month=int(gameMonth),
                game_year=gameYear, game_url=gameUrl, game_complete=False, game_winner="", game_competition = new_tournament)
                newGame.save()
                print(f"post request made for a new tournament - {new_tournament.competition_name} with the teams - {homeTeam} vs {awayTeam}.")



    return render(request, 'api/game.html')

@csrf_exempt
@api_view(['GET'])
def checkExistingGames(request):
    all_incomplete_games = Game.objects.filter(game_complete=False)
    serialized_incomplete_games = GameSerializer(all_incomplete_games, many=True)
    return Response(serialized_incomplete_games.data)


@csrf_exempt
@api_view(['GET'])
def gameList(request):
    all_games = Game.objects.all()
    gameslist = []
    for game in all_games:
        game_dict = {}

        # Add values to the dictionary
        game_dict["id"] = game.id
        game_dict["home_team_name"] = game.home_team_name
        game_dict["away_team_name"] = game.away_team_name
        game_dict["home_odd"] = game.home_odd
        game_dict["draw_odd"] = game.draw_odd
        game_dict["away_odd"] = game.away_odd
        game_dict["game_date"] = game.game_date
        game_dict["game_month"] = game.game_month
        game_dict["game_year"] = game.game_year
        game_dict["game_url"] = game.game_url
        game_dict["game_complete"] = game.game_complete
        game_dict["game_winner"] = game.game_winner
        game_dict["admin_winner_choice"] = game.admin_winner_choice
        game_dict["game_paid"] = game.game_paid
        game_dict["game_vip"] = game.game_vip
        game_dict["game_competition"] = game.game_competition
        game_dict["competition_name"] = game.game_competition.competition_name
        game_dict["competition_image_url"] = game.game_competition.competition_image
        
        
        is_game_won = False
        game_dict["game_won"] = is_game_won
        
        gameslist.append(game_dict)
        

    context = { 'games' : game_dict }
    #return HttpResponse(json.dumps(game_dict), content_type = 'application/javascript; charset=utf8' )
    #serialized_data = serializers.serialize('json', [data])
    serialized_games = GameSerializer(all_games, many=True)

    #return Response(serialized_data)
    return Response(serialized_games.data)

@api_view(['POST'])
def getAdminInfo(request):
    if request.method == "POST":
        homeWin = request.POST.get('homeWin')
        draw = request.POST.get('draw')
        awayWin = request.POST.get('awayWin')
        gameId = request.POST.get('gameId')
        gamePaid = request.POST.get('paid')
        the_game = Game.objects.filter(pk=int(gameId)).first()
        if the_game.game_complete == False:
            if homeWin:
                the_game.admin_winner_choice = the_game.home_team_name
            if draw:
                the_game.admin_winner_choice = "draw"
            if awayWin:
                the_game.admin_winner_choice = the_game.away_team_name
            if gamePaid:
                the_game.game_paid = True
            the_game.save()
            print(f"{the_game.admin_winner_choice} added as the predicted winner for {the_game.home_team_name} vs {the_game.away_team_name}")
        else:
            print("The game is already complete")

        print(f"Post request {homeWin} - {draw} - {awayWin}. With the game id {gameId}.")

    serialized_game = GameSerializer(the_game, many=False)
    return Response(serialized_game.data)

@csrf_exempt
def updateGame(request):
    if request.method == "POST":
        gameId = request.POST.get('gameid')
        winner = request.POST.get('winner')
        # print(winner)
        the_game = Game.objects.filter(id=int(gameId)).first()
        # print(the_game.game_winner)
    
        if winner == "home team":
            the_game.game_winner = the_game.home_team_name
            the_game.game_complete = True
            print(f"The winner is the home team", winner)
        elif winner == "away team":
            the_game.game_winner = the_game.away_team_name
            the_game.game_complete = True
            print(f"The winner is the away team", winner)
        else:
            the_game.game_winner = 'draw'
            the_game.game_complete = True
            print(f"The winner is neither the home team {the_game.home_team_name} nor the away team {the_game.away_team_name}. It is {winner}.")
        the_game.save()
        # print(the_game.game_winner)
        # print(" ")
        # print(the_game.home_team_name)

    return render(request, 'api/game.html')


def thepage(request):
    all_games = AdminGame.objects.all()
    all_won_game = AdminGame.objects.filter(result="won")
    the_user = request.user 
    show_paid_games = False
    # for game in all_games:
    #     print(game.result, "game result")
    if request.user.is_authenticated:
        the_user_data = user.objects.filter(user_data=the_user).first()
        if the_user_data:
            if the_user_data.user_paid:
                #don't filter to only free
                show_paid_games = True
    
    print("show paid games is", show_paid_games)
    if show_paid_games == True:
        all_games = AdminGame.objects.all()
    else:
        all_games = AdminGame.objects.filter(game_paid=False)

    context = { 'games': all_games, 'showing_paid' : show_paid_games, 'wongames': all_won_game}
    return render(request, 'api/thepage.html', context)
    
def mainpage(request):
    #check if user is authenticated.
    #check if they have paid for games.
    #check if they have paid for either of the subscriptions.
    #FixedMatchGame, BetikaJackpotGame, SportPesaJackpotGame, SubscriptionGame
    games = AdminGame.objects.all()
    betikagames = BetikaJackpotGame.objects.all()
    sportpesagames = SportPesaJackpotGame.objects.all()
    subscriptiongames = SubscriptionGame.objects.all()
    context = { 'games' : games, 'betikagames' : betikagames, 'sportpesagames' : sportpesagames, 'subscriptiongames' : subscriptiongames }
    return render(request, 'api/main/index.html', context)