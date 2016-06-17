from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.sites.models import Site


class Command(BaseCommand):

    def handle(self, *args, **options):

        self.delete_the_existing_sites()

        our_sites = ("localhost:8080", "localhost:8003", "localhost:4000", "192.168.99.100:8080", "www.tumacredo.com", "tumacredo.com", "lb.tumacredo-stag.a087b769.svc.dockerapp.io:9000")

        for site in our_sites:
            try:
                Site.objects.create(
                    name=site,
                    domain=site
                )
            except:
                pass

    def delete_the_existing_sites(self):

        sites = Site.objects.all()

        for site in sites:
            site.delete()
