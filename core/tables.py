import django_tables2 as tables
from core.models import *


class CollectionsTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk",
                                      orderable=False,
                                      attrs={"th__input": {"onclick": "toggle(this)"}},
                                      )

    edit = tables.LinkColumn('update-collection', kwargs={"pk": tables.A("pk")}, orderable=False, empty_values=())

    class Meta:
        model = Collection
        attrs = {"class": "table table-striped table-bordered table-sm"}
        sequence = ("selection",)
        exclude = ['id']


class CostTable(tables.Table):
    selection = tables.CheckBoxColumn(accessor="pk",
                                      orderable=False,
                                      attrs={"th__input": {"onclick": "toggle(this)"}},
                                      )

    edit = tables.LinkColumn('update-cost', kwargs={"pk": tables.A("pk")}, orderable=False, empty_values=())

    class Meta:
        model = Cost
        attrs = {"class": "table table-striped table-bordered table-sm"}
        sequence = ("selection",)
        exclude = ['id']


class AreasTable(tables.Table):
    edit = tables.LinkColumn('update-area', kwargs={"pk": tables.A("pk")}, orderable=False, empty_values=())
    class Meta:
        model = GarbagePoint
        attrs = {"class": "table table-striped table-bordered table-sm"}
        exclude = ['id']
