from django.core.management.base import BaseCommand
from app.models import Testimonial


class Command(BaseCommand):
    help = 'Add sample testimonials to the database'

    def handle(self, *args, **options):
        testimonials_data = [
            {
                'name': 'Ulonnaya Aham',
                'title': 'Community Member',
                'content': 'When I first arrived in Ireland, I was completely lost. I didn\'t know where to start. But connecting with the Umuahia Community Ireland changed everything. They guided me through the challenges of settling in, offered support, and showed me the right path. Today, I am proud to say I\'m working and building a life here. I\'ll always be grateful for the community that believed in me when I didn\'t know where to turn.',
                'order': 1
            },
            {
                'name': 'Ms. Eberechukwu Igwe',
                'title': 'Community Member',
                'content': 'Umuahia Community Ireland played a vital role in helping me integrate into Irish society. Through their support, events, and mentoring, I found a sense of belonging, made lasting connections, and now feel truly at home here. Their work extends beyond mere assistance; they empower and uplift.',
                'order': 2
            },
            {
                'name': 'Mazi Ugo Okeh',
                'title': 'Community Member',
                'content': 'Before I met Umuahia Community Ireland, I felt isolated and unsure of my direction. But joining this community gave me more than support. It gave me purpose. I was encouraged to participate in cultural events, volunteer, and connect with others who shared similar experiences. Today, I am actively involved in my local community and proud of the progress I have made.',
                'order': 3
            },
            {
                'name': 'Michael Nwachukwu',
                'title': 'Community Member',
                'content': 'Relocating to Ireland was not easy. I faced many challenges, from accommodation issues to navigating a new system. Umuahia Community Ireland stood by me every step of the way. With their help, I secured stable housing, gained access to key services, and eventually found employment. I now support others going through what I once did. This organisation changed my life.',
                'order': 4
            },
            {
                'name': 'Work Programmes Graduate',
                'title': 'Now working full-time with a law firm',
                'content': 'From being taken under until now, I have learned and grown so much. I thank each and every one of you for teaching and inspiring me. I\'m excited about the future while I continue to be excited about all the things we will continue to accomplish here. Please remember that the work you all do here is very special. Every day you all help others. It has been an absolute honour!',
                'order': 5
            }
        ]

        for data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=data['name'],
                defaults=data
            )
            if created:
                self.stdout.write(
                    self.style.SUCCESS(f'Successfully created testimonial for {data["name"]}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Testimonial for {data["name"]} already exists')
                )

        self.stdout.write(
            self.style.SUCCESS('Testimonials setup completed!')
        ) 