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
