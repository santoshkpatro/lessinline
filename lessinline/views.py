from rest_framework.decorators import api_view
from django.http import JsonResponse


@api_view(['GET'])
def health(request):
    return JsonResponse({'health': 'ok'})
