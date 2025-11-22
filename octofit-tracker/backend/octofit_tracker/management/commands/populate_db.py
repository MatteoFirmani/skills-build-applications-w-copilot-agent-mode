from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data (delete one by one for ObjectIdField compatibility)
        Leaderboard.objects.filter(pk__isnull=False).delete()
        Activity.objects.filter(pk__isnull=False).delete()
        Workout.objects.filter(pk__isnull=False).delete()
        User.objects.filter(pk__isnull=False).delete()
        Team.objects.filter(pk__isnull=False).delete()

        # Teams
        marvel = Team.objects.create(name='marvel', description='Marvel Team')
        dc = Team.objects.create(name='dc', description='DC Team')

        # Users
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Workouts
        pushups = Workout.objects.create(name='Pushups', description='Upper body', difficulty='easy')
        running = Workout.objects.create(name='Running', description='Cardio', difficulty='medium')

        # Activities
        Activity.objects.create(user=tony, type='run', duration=30, date=timezone.now().date())
        Activity.objects.create(user=steve, type='pushup', duration=15, date=timezone.now().date())
        Activity.objects.create(user=bruce, type='run', duration=45, date=timezone.now().date())
        Activity.objects.create(user=clark, type='pushup', duration=20, date=timezone.now().date())

        # Leaderboard
        Leaderboard.objects.create(user=tony, score=100, rank=1)
        Leaderboard.objects.create(user=steve, score=90, rank=2)
        Leaderboard.objects.create(user=bruce, score=80, rank=3)
        Leaderboard.objects.create(user=clark, score=70, rank=4)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data'))
