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
