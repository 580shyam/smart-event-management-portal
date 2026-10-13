from datetime import timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from events.models import Event


class Command(BaseCommand):
    help = "Add six sample upcoming events for local development."

    def handle(self, *args, **options):
        now = timezone.localtime(timezone.now()).replace(minute=0, second=0, microsecond=0)
        samples = [
            {
                "title": "Future Makers Meetup",
                "category": "technology",
                "venue": "Innovation Hub, Bhagalpur",
                "days": 7,
                "hour": 11,
                "capacity": 80,
                "description": "A friendly meetup for people curious about software, AI, and the ideas shaping tomorrow.\n\nShare what you are building, learn from other makers, and leave with a few new connections and practical ideas.",
            },
            {
                "title": "The Creative Learning Lab",
                "category": "education",
                "venue": "Community Learning Centre",
                "days": 12,
                "hour": 10,
                "capacity": 45,
                "description": "A hands-on learning session designed for curious beginners. Explore new skills, try small activities, and learn together in a relaxed environment.\n\nBring your questions and an open mind. No previous experience is needed.",
            },
            {
                "title": "Ideas Into Action Forum",
                "category": "business",
                "venue": "The Riverside Conference Hall",
                "days": 17,
                "hour": 14,
                "capacity": 100,
                "description": "An open forum for students, founders, freelancers, and professionals who want to turn useful ideas into real projects.\n\nMeet collaborators, exchange practical lessons, and build momentum on your next big idea.",
            },
            {
                "title": "Art, Stories & Chai",
                "category": "culture",
                "venue": "The Courtyard Arts Space",
                "days": 21,
                "hour": 16,
                "capacity": 35,
                "description": "An easy-going community afternoon celebrating art, stories, and local creativity. Meet artists, share stories, and enjoy a welcoming space for new conversations.\n\nCome as you are and bring a friend who loves discovering something new.",
            },
            {
                "title": "Weekend Move Together",
                "category": "sports",
                "venue": "City Sports Ground",
                "days": 25,
                "hour": 8,
                "capacity": 60,
                "description": "A friendly, beginner-welcoming morning for movement, teamwork, and positive energy. Choose a light activity, meet neighbours, and enjoy time outdoors.\n\nComfortable clothes and a water bottle are recommended.",
            },
            {
                "title": "Community Connect Day",
                "category": "other",
                "venue": "Town Hall Community Room",
                "days": 30,
                "hour": 12,
                "capacity": 120,
                "description": "A community gathering for meeting new people, sharing useful resources, and finding ways to support local ideas.\n\nThere will be short introductions, small group conversations, and plenty of room to make meaningful connections.",
            },
        ]
        created = 0
        for item in samples:
            event_date = (now + timedelta(days=item.pop("days"))).replace(hour=item.pop("hour"), minute=0)
            _event, was_created = Event.objects.get_or_create(
                title=item["title"],
                defaults={**item, "event_date": event_date},
            )
            if was_created:
                created += 1
        self.stdout.write(self.style.SUCCESS(f"Added {created} sample event(s)."))
