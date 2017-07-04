from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from restfulAPI.models import *


class Command(BaseCommand):
    help = 'Engagement Report'

    def handle(self, *args, **options):
        print 'Hello world :)'
