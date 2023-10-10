from django.http import HttpResponse
import environ

env = environ.Env()
environ.Env.read_env()

def my_view(request):
    secret = env('PASSWORD')
    return HttpResponse(f"The secret key is: {secret}")
