from django.http import HttpResponse

# Create your views here.

# Podemos enviar archivos html

### request es una respuesta http
def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")

