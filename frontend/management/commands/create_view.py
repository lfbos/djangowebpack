from django.core.management import BaseCommand

from frontend.utils import NewViewBuilder


class Command(BaseCommand):
    help = 'Create new template view with all settings'

    def add_arguments(self, parser):
        parser.add_argument(
            'view_name', type=str, help='Name of the new view to create'
        )

        parser.add_argument('-t', '--title', type=str, help='View title', )

    def handle(self, *args, **kwargs):
        view_name = kwargs.get('view_name').lower()
        title = kwargs.get('title')

        if '-' in view_name:
            raise Exception(
                'Error the view name should not contains any special character besides underscore, pe: my_app'
            )

        if title is None:
            title = view_name.title().replace('_', ' ')

        builder = NewViewBuilder(view_name, title)
        builder.run()
