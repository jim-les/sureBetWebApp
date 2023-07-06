# Register your models here.
from django.contrib import admin
from .models import Competition, Game, GameWinner, GameOverUnder15, AdminGame, user, FixedMatchGame, BetikaJackpotGame, SportPesaJackpotGame, SubscriptionGame

class CompetitionAdmin(admin.ModelAdmin):
    list_display = ('competition_name','competition_image')

admin.site.register(Competition, CompetitionAdmin)

class GameAdmin(admin.ModelAdmin):
    list_display = ('home_team_name','away_team_name','home_odd','draw_odd','away_odd', 'game_date','game_month','game_year', 'game_url')
#admin.site.register(Game, GameAdmin)

#admin.site.register(GameWinner)
#admin.site.register(GameOverUnder15)

class AdminGameAdmin(admin.ModelAdmin):
    list_display = ('game_competition', 'winning_game_odd', 'home_team', 'away_team', 'prediction', 'result')

admin.site.register(AdminGame, AdminGameAdmin)
admin.site.register(user)

class FixedMatchGameAdmin(admin.ModelAdmin):
    list_display = ('game_competition', 'winning_game_odd', 'home_team', 'away_team', 'prediction', 'result')

admin.site.register(FixedMatchGame, AdminGameAdmin)

class BetikaJackpotGameAdmin(admin.ModelAdmin):
    list_display = ('game_competition', 'winning_game_odd', 'home_team', 'away_team', 'prediction', 'result')

admin.site.register(BetikaJackpotGame, BetikaJackpotGameAdmin)

class SportPesaJackpotGameAdmin(admin.ModelAdmin):
    list_display = ('game_competition', 'winning_game_odd', 'home_team', 'away_team', 'prediction', 'result')

admin.site.register(SportPesaJackpotGame, SportPesaJackpotGameAdmin)

class SubscriptionGameAdmin(admin.ModelAdmin):
    list_display = ('game_competition', 'winning_game_odd', 'home_team', 'away_team', 'prediction', 'result')

admin.site.register(SubscriptionGame, SubscriptionGameAdmin)