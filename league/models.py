from django.db import models
import uuid
from django.conf import settings
from django.utils import timezone


# League Model
class League(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Team Model
class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    points = models.IntegerField(default=0)


    def win(self):
        print('points have been added to', self.name)
        self.points += 3

    def draw(self):
        print('points have been added to', self.name)
        self.points += 1

    def __str__(self):
        return self.name


# Players Model
class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='players')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


# Game Model
class Game(models.Model):
    # id
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # team_1
    team_1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_1')
    # team_2
    team_2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_2')
    # date
    date = models.DateTimeField(default=timezone.now)
    # team_1_score
    team_1_score = models.IntegerField(default=0)
    # team_2_score
    team_2_score = models.IntegerField(default=0)
    # result
    result = models.CharField(max_length=200, default='-')
    # winner
    winner = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.team_1.name + ' vs ' + self.team_2.name

    def save(self, *args, **kwargs):
        if self.team_1_score > self.team_2_score:
            self.winner = self.team_1.name
            self.result = f'{self.team_1.name} - wins'
            super(Game, self).save()
        elif self.team_1_score < self.team_2_score:
            self.winner = self.team_2.name
            self.result = f'{self.team_2.name} - wins'
            super(Game, self).save()
        else:
            self.winner = None
            self.result = f'{self.team_1.name} - {self.team_2.name} - draw'
            super(Game, self).save(*args, **kwargs)
