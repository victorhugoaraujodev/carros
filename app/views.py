from cars.views import CarsListView


class HomeView(CarsListView):
    login_url = 'login'
