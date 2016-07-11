"""dockertestproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin

from core.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^brokers', login_required(BrokersView.as_view()), name='brokers'),
    url(r'^areas', login_required(AreasView.as_view()), name='areas'),
    url(r'^costs/$', login_required(CostsView.as_view()), name='costs'),
    url(r'^costs/add/$', login_required(AddCostsView.as_view()), name='add-cost'),
    url(r'^costs/(?P<pk>[\w-]+)/update-cost/$', login_required(UpdateCostView.as_view()), name='update-cost'),
    url(r'^collections/$', login_required(CollectionsView.as_view()), name='dashboard'),
    url(r'^collections/add/$', login_required(AddCollectionsView.as_view()), name='add-collection'),
    url(r'^collections/(?P<pk>[\w-]+)/update-collection/$', login_required(UpdateCollectionView.as_view()), name='update-collection'),
    url(r'^accounts/', include('registration.backends.default.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
