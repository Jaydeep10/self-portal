# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView
from django.views.generic.base import View
from django.http import HttpResponse
import os
##os.environ.setdefault('DJANGO_SETTINGS_MODULE','myself.settings')

class Welcome(TemplateView):
    template_name = "about.html"

class Resume(TemplateView):
    template_name = "resume.html"

class About(TemplateView):
    template_name = "self.html"

class Contact(TemplateView):
    template_name = "contact.html"
