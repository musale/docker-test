from django.contrib import admin

from core.models import Broker, GarbagePoint, Cost, Collection


class BrokerAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'contact', 'payment_status', 'amount')


class GarbagePointAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = (
        'location', 'type_of_location', 'person_in_charge', 'contacts', 'paper_size', 'created_at', 'updated_at')


class CostAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'description', 'amount', 'created_at', 'updated_at')


class CollectionAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('collection_area', 'broker', 'created_at', 'updated_at')


admin.site.register(Broker, BrokerAdmin)
admin.site.register(GarbagePoint, GarbagePointAdmin)
admin.site.register(Cost, CostAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.site_header = 'Garbage Collection Demo'
admin.site.index_title = 'Garbage Demo Features'
admin.site.site_title = 'Garbage Demo'
