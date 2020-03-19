import requests

from django.core.management.base import BaseCommand
from requests import RequestException

from core.models import LocationModel


class Command(BaseCommand):
    """Pulls the latest statistics from an api and puts it into the DB
    the command should run few hours using crontab or any simmilar utility
    """

    help = 'Gets the latest statistics for COVID-19'
    URL = 'https://coronavirus-tracker-api.herokuapp.com/v2/locations'

    def handle(self, *args, **options):
        """handles the command"""
        try:
            res = requests.get(self.URL)
            if res.status_code != 200:
                print(res.status_code)
                raise RequestException

            data = res.json()

            LocationModel.objects.all().delete()  # renews data because some countries like china have multiple regions in the db

            for location in data['locations']:

                unique_data = {'country': location.get('country'),
                               'country_code': location.get('country_code')}

                confirmed = location.get('latest').get('confirmed')
                deaths = location.get('latest').get('deaths')
                recovered = location.get('latest').get('recovered')

                try:
                    loc = LocationModel.objects.get(**unique_data)
                    loc.confirmed = loc.confirmed + confirmed
                    loc.deaths = loc.deaths + deaths
                    loc.recovered = loc.recovered + recovered
                    loc.save()

                except LocationModel.DoesNotExist:
                    loc = LocationModel(**unique_data, confirmed=confirmed, deaths=deaths,
                                        recovered=recovered,
                                        latitude=location.get('coordinates').get('latitude'),
                                        longitude=location.get('coordinates').get('longitude'))
                    loc.save()

        except RequestException:
            self.stderr.write('Error connecting to tracker api')
