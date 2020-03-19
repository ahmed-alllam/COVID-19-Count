from django.db.models import Sum
from django.shortcuts import render

from core.models import LocationModel


def get_view(request):
    """view from home page"""

    queryset = LocationModel.objects.all()

    confirmed = queryset.aggregate(Sum('confirmed'))['confirmed__sum']
    deaths = queryset.aggregate(Sum('deaths'))['deaths__sum']
    recovered = queryset.aggregate(Sum('recovered'))['recovered__sum']
    active = confirmed - (deaths + recovered)

    return render(request, 'index.html', context={'locations': queryset[:50],
                                                  'confirmed': confirmed,
                                                  'active': active,
                                                  'deaths': deaths,
                                                  'recovered': recovered})
