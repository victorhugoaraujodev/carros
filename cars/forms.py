from django import forms
from django.core.exceptions import ValidationError
from cars.models import Car


class CarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


    def clean_value(self):
        value = self.cleaned_data.get('value')
        if value is not None and value < 20000:
            raise ValidationError('Valor mínimo do carro deve ser de R$20.000')
        return value

    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year is not None and factory_year < 1975:
            raise ValidationError('Não é possível cadastrar carros fabricados antes de 1975')
        return factory_year
