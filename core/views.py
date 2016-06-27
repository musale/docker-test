from django.shortcuts import render
from django.views.generic import TemplateView

from core.models import Broker, GarbagePoint, Cost, Collection


def dashboard(request):
    context = {}
    brokers = Broker.objects.all()
    garbage_points = GarbagePoint.objects.all()
    cost = Cost.objects.all()
    collection = Collection.objects.all()
    context['brokers'] = brokers
    context['garbage_points'] = garbage_points
    context['cost'] = cost
    context['collection'] = collection

    return render(request, 'account/dashboard.html', context)


class CustomLoginView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        # display dashboard if user is authenticated
        if request.user.is_authenticated():
            return dashboard(request)
        return super(CustomLoginView, self).get(request, args, kwargs)
