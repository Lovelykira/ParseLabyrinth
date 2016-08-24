from django.shortcuts import render
from django.views.generic import TemplateView


class JinxView(TemplateView):
    template_name = "Jinx.html"


class AatroxView(TemplateView):
    template_name = "Aatrox.html"


class AnnieView(TemplateView):
    template_name = "Annie.html"


class EvelynView(TemplateView):
    template_name = "Evelyn.html"


class MalphitView(TemplateView):
    template_name = "Malphit.html"


class RyzeView(TemplateView):
    template_name = "Ryze.html"


class ShacoView(TemplateView):
    template_name = "Shaco.html"


class TristanaView(TemplateView):
    template_name = "Tristana.html"


class ViView(TemplateView):
    template_name = "Vi.html"


class ZyraView(TemplateView):
    template_name = "Zyra.html"