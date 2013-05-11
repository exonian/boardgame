import argparse

from django.core.management.base import BaseCommand

from cards.models import Modifier, Profession, Trait
from game.models import Attribute


COMPONENT_TYPES = {
    'profession': Profession,
    'trait': Trait
}

class Command(BaseCommand):
    def handle(self, *args, **options):
        parser = argparse.ArgumentParser(
            description='Create modifiers for a component type'
        )
        parser.add_argument('function')
        parser.add_argument(
            'component',
            type=str,
            choices=COMPONENT_TYPES.keys(),
            help='the hero component to add modifiers for'
        )
        
        args = parser.parse_args()
        self.component = COMPONENT_TYPES[args.component]
        self.stdout.write(str(self.component))
