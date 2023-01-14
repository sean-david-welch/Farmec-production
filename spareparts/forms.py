from django.db.models.base import Model
from django import forms
from django.forms import ModelForm, widgets, forms, formsets, inlineformset_factory
from . models import WarrantyClaim, PartsRequired, MachineRegistration, SupplierPage, PartsPage

class WarrantyClaimForm(ModelForm):
    class Meta:
        model = WarrantyClaim
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(WarrantyClaimForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class PartsRequiredForm(ModelForm):
    class Meta:
        model = PartsRequired
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartsRequiredForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

PartsRequiredFormSet = inlineformset_factory(WarrantyClaim, PartsRequired, form=PartsRequiredForm, extra=2)

class SupplierPageForm(ModelForm):
    class Meta:
        model = SupplierPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SupplierPageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

class PartsPageForm(ModelForm):
    class Meta:
        model = PartsPage
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PartsPageForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


    