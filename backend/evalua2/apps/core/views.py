# -*- coding: utf-8 -*-
from django.http import HttpResponse


def project_info(request):
    return HttpResponse("Hello, world. You're at Pablo Fuentes PFC REST API")
