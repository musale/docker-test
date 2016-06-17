from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Command(BaseCommand):

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument('--username',
            dest='username',
            default='admin',
            help=('super user admin'))
        parser.add_argument('--password',
                help=("enter username"),
            )


    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options.get('email', 'admin@example.com')

        if not User.objects.filter(username=username).exists():
            admin = User.objects.create_superuser(username, email, password)
        if not User.objects.filter(username="promotional_user").exists():
            """
            password asdgrfitvnv
            """
            user = User.objects.create_superuser(username='promotional_user', email='info@tumacredo.com', password='asdgrfitvnv')
