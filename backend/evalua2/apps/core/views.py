# -*- coding: utf-8 -*-
from django.http import HttpResponse


def project_info(request):
    return HttpResponse("""Hello, world! Bienvenido al PFC de Pablo Fuentes <br />
                           Siento decirte que estas en el sitio equivocado esto es el backend de la REST API!""")
