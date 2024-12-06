from django.core.management import BaseCommand, CommandError
from forms.models import Form


class Command(BaseCommand):
    help = 'Creating data for a database'

    def handle(self, *args, **options):
        # Creating forms
        forms = [
            {
                'name': 'ShortForm',
                'email': 'first@mail.hop',
                'phone': '+7 999 111 11 111'
            },
            {
                'name': 'MediumForm',
                'email': 'second@mail.hop',
                'phone': '+7 999 222 22 22',
                'data': '2022-02-02'
            },
            {
                'name': 'LongForm',
                'email': 'third@mail.hop',
                'phone': '+7 999 333 33 33',
                'data': '2023-03-03',
                'text': 'Простота — высшая степень искусства.'
            }
        ]
        for form in forms:
            try:
                new_form, _ = Form.objects.get_or_create(**form)
                self.stdout.write(self.style.SUCCESS(f'{new_form} created successfully!'))
            except:
                raise CommandError('Can\'t create form!')

        self.stdout.write(self.style.SUCCESS('Database entries have been created successfully!'))