from django.views.generic import TemplateView


class Homepage(TemplateView):
    template_name = 'home.html'


class Aboutpage(TemplateView):
    template_name = 'about.html'