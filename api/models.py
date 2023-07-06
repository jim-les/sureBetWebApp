from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class user(models.Model):
    user_data = models.ForeignKey(User, on_delete=models.CASCADE)
    user_paid = models.BooleanField(default=False)
    user_paid_vip = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user_data.username}'s data."

class Competition(models.Model):
    competition_name = models.CharField(max_length=255)
    competition_image = models.ImageField(upload_to="tournamentLogo", default='tournamentLogo/default.png')
    def __str__(self):
        return self.competition_name
        
class AdminGame(models.Model):
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null = True)
    winning_game_odd = models.FloatField(default=0.0, null=True, blank=True)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_odd = models.FloatField(default=0, null=True, blank=True)
    draw_odd = models.FloatField(default=0, null=True, blank=True)
    away_odd = models.FloatField(default=0, null=True, blank=True)
    prediction = models.CharField(max_length=255, default="")
    game_year = models.IntegerField(default=2023, null=True)
    game_month = models.IntegerField(default=5, null=True)
    game_date = models.IntegerField(default=26, null=True)
    game_hour = models.IntegerField(default=22, null=True)
    game_minute = models.IntegerField(default=18, null=True)
    game_first_half_result = models.CharField(max_length=255, default="-")
    game_second_half_result = models.CharField(max_length=255, default="-")
    #result = models.IntegerField(choices=GAME_RESULT_CHOICES, default=2)
    GAME_WON = 'won'
    GAME_LOST = 'lost'
    GAME_WAITING = 'waiting'
    CATEGORY_CHOICES = (
        (GAME_WON, 'won'),
        (GAME_LOST, 'lost'),
        (GAME_WAITING, 'waiting')
    )
    result = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=GAME_WON)
    game_paid = models.BooleanField(default=False, null=True)
    comments = models.CharField(max_length=255, default="", null=True)
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} and the prediction being {self.prediction}"

class FixedMatchGame(models.Model):
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null = True)
    winning_game_odd = models.FloatField(default=0.0, null=True, blank=True)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_odd = models.FloatField(default=0, null=True, blank=True)
    draw_odd = models.FloatField(default=0, null=True, blank=True)
    away_odd = models.FloatField(default=0, null=True, blank=True)
    prediction = models.CharField(max_length=255, default="")
    game_year = models.IntegerField(default=2023, null=True)
    game_month = models.IntegerField(default=5, null=True)
    game_date = models.IntegerField(default=26, null=True)
    game_hour = models.IntegerField(default=22, null=True)
    game_minute = models.IntegerField(default=18, null=True)
    game_first_half_result = models.CharField(max_length=255, default="-")
    game_second_half_result = models.CharField(max_length=255, default="-")
    #result = models.IntegerField(choices=GAME_RESULT_CHOICES, default=2)
    GAME_WON = 'won'
    GAME_LOST = 'lost'
    GAME_WAITING = 'waiting'
    CATEGORY_CHOICES = (
        (GAME_WON, 'won'),
        (GAME_LOST, 'lost'),
        (GAME_WAITING, 'waiting')
    )
    result = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=GAME_WON)
    game_paid = models.BooleanField(default=False, null=True)
    comments = models.CharField(max_length=255, default="", null=True)
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} and the prediction being {self.prediction}"

class BetikaJackpotGame(models.Model):
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null = True)
    winning_game_odd = models.FloatField(default=0.0, null=True, blank=True)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_odd = models.FloatField(default=0, null=True, blank=True)
    draw_odd = models.FloatField(default=0, null=True, blank=True)
    away_odd = models.FloatField(default=0, null=True, blank=True)
    prediction = models.CharField(max_length=255, default="")
    game_year = models.IntegerField(default=2023, null=True)
    game_month = models.IntegerField(default=5, null=True)
    game_date = models.IntegerField(default=26, null=True)
    game_hour = models.IntegerField(default=22, null=True)
    game_minute = models.IntegerField(default=18, null=True)
    game_first_half_result = models.CharField(max_length=255, default="-")
    game_second_half_result = models.CharField(max_length=255, default="-")
    #result = models.IntegerField(choices=GAME_RESULT_CHOICES, default=2)
    GAME_WON = 'won'
    GAME_LOST = 'lost'
    GAME_WAITING = 'waiting'
    CATEGORY_CHOICES = (
        (GAME_WON, 'won'),
        (GAME_LOST, 'lost'),
        (GAME_WAITING, 'waiting')
    )
    result = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=GAME_WON)
    game_paid = models.BooleanField(default=False, null=True)
    comments = models.CharField(max_length=255, default="", null=True)
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} and the prediction being {self.prediction}"
  
class SportPesaJackpotGame(models.Model):
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null = True)
    winning_game_odd = models.FloatField(default=0.0, null=True, blank=True)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_odd = models.FloatField(default=0, null=True, blank=True)
    draw_odd = models.FloatField(default=0, null=True, blank=True)
    away_odd = models.FloatField(default=0, null=True, blank=True)
    prediction = models.CharField(max_length=255, default="")
    game_year = models.IntegerField(default=2023, null=True)
    game_month = models.IntegerField(default=5, null=True)
    game_date = models.IntegerField(default=26, null=True)
    game_hour = models.IntegerField(default=22, null=True)
    game_minute = models.IntegerField(default=18, null=True)
    game_first_half_result = models.CharField(max_length=255, default="-")
    game_second_half_result = models.CharField(max_length=255, default="-")
    #result = models.IntegerField(choices=GAME_RESULT_CHOICES, default=2)
    GAME_WON = 'won'
    GAME_LOST = 'lost'
    GAME_WAITING = 'waiting'
    CATEGORY_CHOICES = (
        (GAME_WON, 'won'),
        (GAME_LOST, 'lost'),
        (GAME_WAITING, 'waiting')
    )
    result = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=GAME_WON)
    game_paid = models.BooleanField(default=False, null=True)
    comments = models.CharField(max_length=255, default="", null=True)
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} and the prediction being {self.prediction}"

class SubscriptionGame(models.Model):
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null = True)
    winning_game_odd = models.FloatField(default=0.0, null=True, blank=True)
    home_team = models.CharField(max_length=255)
    away_team = models.CharField(max_length=255)
    home_odd = models.FloatField(default=0, null=True, blank=True)
    draw_odd = models.FloatField(default=0, null=True, blank=True)
    away_odd = models.FloatField(default=0, null=True, blank=True)
    prediction = models.CharField(max_length=255, default="")
    game_year = models.IntegerField(default=2023, null=True)
    game_month = models.IntegerField(default=5, null=True)
    game_date = models.IntegerField(default=26, null=True)
    game_hour = models.IntegerField(default=22, null=True)
    game_minute = models.IntegerField(default=18, null=True)
    game_first_half_result = models.CharField(max_length=255, default="-")
    game_second_half_result = models.CharField(max_length=255, default="-")
    #result = models.IntegerField(choices=GAME_RESULT_CHOICES, default=2)
    GAME_WON = 'won'
    GAME_LOST = 'lost'
    GAME_WAITING = 'waiting'
    CATEGORY_CHOICES = (
        (GAME_WON, 'won'),
        (GAME_LOST, 'lost'),
        (GAME_WAITING, 'waiting')
    )
    result = models.CharField(max_length=200, choices=CATEGORY_CHOICES, default=GAME_WON)
    game_paid = models.BooleanField(default=False, null=True)
    comments = models.CharField(max_length=255, default="", null=True)
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} and the prediction being {self.prediction}"
        
class Game(models.Model):
    home_team_name = models.CharField(max_length=255)
    away_team_name = models.CharField(max_length=255)
    home_odd = models.DecimalField(max_digits=5, decimal_places=2)
    draw_odd = models.DecimalField(max_digits=5, decimal_places=2)
    away_odd = models.DecimalField(max_digits=5, decimal_places=2)
    game_date = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(32)], default=0)
    game_month = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(13)], default = 0)
    game_year = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(5000)], default = 0)
    game_competition = models.ForeignKey(Competition, on_delete=models.CASCADE, null=True)
    game_url = models.CharField(max_length=2000, null=True)
    game_complete = models.BooleanField(default=False)
    game_winner = models.CharField(max_length=255, null=True)
    admin_winner_choice = models.CharField(max_length=255, null=True)
    game_paid = models.BooleanField(default=False)
    game_vip = models.BooleanField(default=False)

class GameWinner(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    winning_team = models.CharField(max_length=255)

GAME_OVER_UNDER = 0 #Neither over nor under value given
GAME_OVER = 1
GAME_UNDER = 2
GAME_OVER_UNDER_CHOICES = (
    (GAME_OVER_UNDER, 'null'),
    (GAME_OVER, 'Over'),
    (GAME_UNDER, 'Under')
)
class GameOverUnder15(models.Model):
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    value = models.IntegerField(choices=GAME_OVER_UNDER_CHOICES)