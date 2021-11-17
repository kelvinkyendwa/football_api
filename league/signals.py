from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *


@receiver(post_save, sender=Game)
def add_points(sender, instance, created, **kwargs):
    print('adding points')

    if instance.winner is None:
        print('result is a draw')
        team1 = Team.objects.get(name=instance.team_1.name)
        team2 = Team.objects.get(name=instance.team_2.name)
        team1.draw()
        team2.draw()
        team1.save()
        team2.save()

    # find winner add 3 Points
    else:
        team = Team.objects.get(name=instance.winner)
        print(team, 'has won the fixture')
        team.win()
        team.save()
