from django.forms import ModelForm
from django.forms.utils import ErrorList

from core.models import *


class CollectionForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'


class CollectionUpdateForm(ModelForm):
    class Meta:
        model = Collection
        fields = '__all__'

    def _get_validation_exclusions(self):
        exclude = super(CollectionUpdateForm, self)._get_validation_exclusions()
        return exclude


class CreateCollectionForm(ModelForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, user=None):
        self.user = user
        super(CreateCollectionForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                                          empty_permitted, instance)

    class Meta:
        model = Collection
        fields = ('__all__')

    def clean(self):
        cleaned_data = super(CreateCollectionForm, self).clean()
        return cleaned_data


class CostForm(ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'


class CostUpdateForm(ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'

    def _get_validation_exclusions(self):
        exclude = super(CostUpdateForm, self)._get_validation_exclusions()
        return exclude


class CreateCostForm(ModelForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, user=None):
        self.user = user
        super(CreateCostForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                                          empty_permitted, instance)

    class Meta:
        model = Cost
        fields = '__all__'

    def clean(self):
        cleaned_data = super(CreateCostForm, self).clean()
        return cleaned_data


class AreasForm(ModelForm):
    class Meta:
        model = GarbagePoint
        fields = '__all__'


class AreaUpdateForm(ModelForm):
    class Meta:
        model = GarbagePoint
        fields = '__all__'

    def _get_validation_exclusions(self):
        exclude = super(AreaUpdateForm, self)._get_validation_exclusions()
        return exclude


class CreateAreaForm(ModelForm):
    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None, user=None):
        self.user = user
        super(CreateAreaForm, self).__init__(data, files, auto_id, prefix, initial, error_class, label_suffix,
                                          empty_permitted, instance)

    class Meta:
        model = GarbagePoint
        fields = '__all__'

    def clean(self):
        cleaned_data = super(CreateAreaForm, self).clean()
        return cleaned_data

