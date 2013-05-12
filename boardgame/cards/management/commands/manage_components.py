import argparse

from distutils.util import strtobool
from django.core.management.base import BaseCommand

from cards.models import Modifier, Profession, Trait
from game.models import Attribute


COMPONENT_TYPES = {
    'profession': Profession,
    'trait': Trait
}

ATTRIBUTES = {a.abbreviation.lower(): a for a in Attribute.objects.all()}

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
        self.stdout.write('')
        self.stdout.write('  {}'.format(self.describe_component(component)))
        edited = False

        response = raw_input('    Edit special rules (y/N): ')
        if response and strtobool(response):
            component = self.edit_component_special_rules(component)
            component.save()

        modifiers = component.modifiers.all()
        if modifiers:
            response = raw_input('    Edit existing modifiers (y/N): ')
            if response and strtobool(response):
                for modifier in modifiers:
                    self.handle_modifier(modifier)

        while True:
            response = raw_input('    Add modifiers (y/N): ')
            if response and strtobool(response):
                self.add_modifier(component)
            else:
                break


    def describe_component(self, component):
        modifiers = ' '.join(
            [m.short_form for m in component.modifiers.all()]
        )
        if component.special_rules:
            rules = '{}. "{}"'.format(modifiers, component.special_rules)
        else:
            rules = modifiers
        return '{}: {}'.format(
            unicode(component),
            rules
        )

    def edit_component_special_rules(self, component):
        new_special_rules = raw_input('    New special rules: ')
        component.special_rules = new_special_rules
        return component

    def handle_modifier(self, modifier):
        self.stdout.write('    {}'.format(modifier.short_form))
        response = raw_input('    Edit this modifier (y/N): ')
        if response and strtobool(response):
            self.edit_modifier(modifier)

    def set_operator(self, modifier):
        while True:
            operator = raw_input('    Operator (+,-,*,/): ')
            if operator in ['+','-','*','/']:
                modifier.operator = operator
                return modifier

    def set_magnitude(self, modifier):
        while True:
            magnitude = raw_input('    Magnitude: ')
            try:
                modifier.magnitude = float(magnitude)
            except ValueError:
                pass
            else:
                return modifier

    def set_attribute(self, modifier):
        while True:
            attribute_abbr = raw_input('    Attribute (a/s/c/i): ').lower()
            try:
                attribute = ATTRIBUTES[attribute_abbr]
            except KeyError:
                pass
            else:
                modifier.attribute = attribute
                return modifier

    def edit_modifier(self, modifier):
        response = raw_input('    Delete this modifier (y/N): ')
        if response and strtobool(response):
            modifier.delete()
            self.stdout.write('    Modifier deleted')
            return None
        modifier = self.set_operator(modifier)
        modifier = self.set_magnitude(modifier)
        modifier.save()

    def add_modifier(self, component):
        modifier = Modifier(component=component)
        modifier = self.set_attribute(modifier)
        modifier = self.set_operator(modifier)
        modifier = self.set_magnitude(modifier)
        modifier.save()
        return modifier
