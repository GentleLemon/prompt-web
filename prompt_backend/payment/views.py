from django.http import JsonResponse
from .models import Package

def get_packages(request):
    packages = Package.objects.all()
    data = [{"id": package.id, "name": package.name, "price": float(package.price)} for package in packages]
    return JsonResponse(data, safe=False)
