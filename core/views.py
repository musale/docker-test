from django.shortcuts import render
from django.views.generic import TemplateView


def dashboard(request):
    return render(request, 'account/dashboard.html', {'welcome': 'welcome'})


class CustomLoginView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        # display dashboard if user is authenticated
        if request.user.is_authenticated():
            return dashboard(request)
        return super(CustomLoginView, self).get(request, args, kwargs)

