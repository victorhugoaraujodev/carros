from cars.models import Car
from cars.forms import CarModelForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView


class CarsListView(LoginRequiredMixin, ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    login_url = 'login'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search)
        return cars


class CarDetailView(LoginRequiredMixin, DetailView):
    model = Car
    template_name = 'car_detail.html'
    login_url = 'login'


class NewCarCreateView(LoginRequiredMixin, CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = reverse_lazy('cars_list')
    login_url = 'login'


class CarUpdateView(LoginRequiredMixin, UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'
    login_url = 'login'

    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(LoginRequiredMixin, DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = reverse_lazy('cars_list')
    login_url = 'login'
