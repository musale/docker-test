import re

from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.views.generic import TemplateView
from django_tables2 import RequestConfig
from django.http import *

from core.forms import *
from core.tables import *
from django.views.generic import UpdateView, View, ListView
import xlwt
import dateutil.parser
from django.utils import formats


class CollectionsView(ListView):
    template_name = 'account/dashboard.html'
    table_class = CollectionsTable

    def get_queryset(self):
        queryset = Collection.objects.all()
        return queryset

    def dispatch(self, request, *args, **kwargs):
        self.params = dict(request.GET.items())
        self.daterange = self.params.get('daterange', '')
        return super(CollectionsView, self).dispatch(request, *args, **kwargs)

    def get_filtered_queryset(self):
        qs = self.get_queryset()

        if self.daterange:
            pattern = re.compile(
                "^([0]?[1-9]|[1][0-2])[/]([0]?[1-9]|[1|2][0-9]|[3][0|1])[/]([0-9]{4}|[0-9]{2})\s*-\s*([0]?[1-9]|[1][0-2])[/]([0]?[1-9]|[1|2][0-9]|[3][0|1])[/]([0-9]{4}|[0-9]{2})$")
            if pattern.match(self.daterange):
                dates = self.daterange.split('-')
                start = dateutil.parser.parse(dates[0].strip())
                end = dateutil.parser.parse(dates[1].strip())
                end = end.replace(hour=23, minute=59, second=59)
                qs = qs.filter(created_at__range=(start, end))
        return qs

    def post(self, request):
        context = {}
        form = CollectionForm(request.POST or None)
        collection = Collection.objects.all()
        table = CollectionsTable(collection)
        RequestConfig(request).configure(table)
        context['collection_table'] = table
        context['collection_form'] = form

        if form.is_valid():
            form.save()
            return render(request, 'account/dashboard.html', context)

        if request.POST.get("selection", False):
            pks = request.POST.getlist("selection")
            selected_collections = Collection.objects.filter(pk__in=pks)
            download = request.POST.get("download", False)
            if download:
                book = xlwt.Workbook(encoding='utf8')
                # Adding style for cell
                # Create Alignment
                alignment = xlwt.Alignment()

                # horz May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT,
                # HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL,
                # HORZ_DISTRIBUTED
                alignment.horz = xlwt.Alignment.HORZ_LEFT
                # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED,
                # VERT_DISTRIBUTED
                alignment.vert = xlwt.Alignment.VERT_TOP
                style = xlwt.XFStyle()  # Create Style
                style.alignment = alignment  # Add Alignment to Style

                sheet = book.add_sheet('Garbage Collections')
                sheet.write(0, 0, 'Collection Area')
                sheet.write(0, 1, 'Type of Location')
                sheet.write(0, 2, 'Person In Charge')
                sheet.write(0, 3, 'Contacts')
                sheet.write(0, 4, 'Broker')
                sheet.write(0, 5, 'Payment Status')
                sheet.write(0, 6, 'Amount')
                sheet.write(0, 7, 'Creation Date')
                sheet.write(0, 8, 'Update Date')
                initial = 0
                for collection in selected_collections:
                    initial += 1
                    sheet.write(initial, 0, collection.collection_area.location)
                    sheet.write(initial, 1, collection.collection_area.type_of_location)
                    sheet.write(initial, 2, collection.collection_area.person_in_charge)
                    sheet.write(initial, 3, collection.collection_area.contacts)
                    sheet.write(initial, 4, collection.broker.name)
                    sheet.write(initial, 5, collection.payment_status)
                    sheet.write(initial, 6, collection.amount)
                    sheet.write(initial, 7, formats.date_format(collection.created_at, "SHORT_DATETIME_FORMAT"))
                    sheet.write(initial, 8, formats.date_format(collection.updated_at, "SHORT_DATETIME_FORMAT"))
                response = HttpResponse(content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename=collection_areas.xls'
                book.save(response)
                return response
        return render(request, 'account/dashboard.html', context)

    def get(self, request, *args, **kwargs):
        return super(CollectionsView, self).get(request, args, kwargs)

    def get_context_data(self, **kwargs):
        context = super(CollectionsView, self).get_context_data(**kwargs)
        collection = Collection.objects.all()
        table = CollectionsTable(collection)
        # table.paginate(page=self.request.GET.get('page', 1), per_page=self.paginate_by)
        # self.table_to_report = RequestConfig(self.request).configure(table)
        form = CollectionForm()
        RequestConfig(self.request).configure(table)
        context['collection_table'] = table
        context['collection_form'] = form
        return context


class UpdateCollectionView(UpdateView):
    model = Collection
    form_class = CollectionUpdateForm
    success_url = '/collections'
    template_name = 'account/update-collection.html'

    def get(self, request, *args, **kwargs):
        """
        Overriding this method to get only the groups that are associated with the logged in user
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(self.get_context_data(form=form))

    def get_queryset(self):
        queryset = super(UpdateCollectionView, self).get_queryset()
        return queryset


class AddCollectionsView(View):
    def post(self, request):
        form = CreateCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dashboard'))
        return render(request, 'account/add-collection.html', {'form': form})

    def get(self, request):
        form = CreateCollectionForm()
        return render(request, 'account/add-collection.html', {'form': form})


class CustomLoginView(TemplateView):
    template_name = 'registration/login.html'

    def get(self, request, *args, **kwargs):
        # display dashboard if user is authenticated
        if request.user.is_authenticated():
            return (CollectionsView, self).get(request, args, kwargs)
        return super(CustomLoginView, self).get(request, args, kwargs)


class BrokersView(TemplateView):
    template_name = 'account/brokers.html'

    def get(self, request, *args, **kwargs):
        return super(BrokersView, self).get(request, args, kwargs)


class CostsView(TemplateView):
    template_name = 'account/costs.html'

    def get(self, request, *args, **kwargs):
        return super(CostsView, self).get(request, args, kwargs)


class AreasView(TemplateView):
    template_name = 'account/areas.html'

    def get(self, request, *args, **kwargs):
        return super(AreasView, self).get(request, args, kwargs)
