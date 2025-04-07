from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = "Populate the database with test data"

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Add test users
        user1 = User.objects.create(email="john.doe@example.com", name="John Doe", password="password123")
        user2 = User.objects.create(email="jane.smith@example.com", name="Jane Smith", password="password456")

        # Add test teams
        team1 = Team.objects.create(name="Team Alpha", members=[user1.id, user2.id])

        # Add test activities
        Activity.objects.create(activity_id="activity1", user=user1, description="Running 5km")
        Activity.objects.create(activity_id="activity2", user=user2, description="Cycling 10km")

        # Add test leaderboard
        Leaderboard.objects.create(leaderboard_id="leaderboard1", team=team1, score=100)

        # Add test workouts
        Workout.objects.create(workout_id="workout1", user=user1, details={"type": "Cardio", "duration": "30 mins"})
        Workout.objects.create(workout_id="workout2", user=user2, details={"type": "Strength", "duration": "45 mins"})

        self.stdout.write(self.style.SUCCESS("Database populated with test data."))