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
        component_class = COMPONENT_TYPES[args.component]
        self.handle_components(component_class)

    def handle_components(self, component_class):
        self.stdout.write(
            'Adding modifiers to {} objects.'.format(component_class.__name__)
        )
        components = component_class.objects.all()
        self.stdout.write(
            '{} {} objects found.'.format(
                components.count(),
                component_class.__name__)
        )
        for component in components:
            self.handle_component(component)

    def handle_component(self, component):
        self.stdout.write(
            '  {}'.format(component)
        )
