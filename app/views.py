from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If behind a proxy, the real IP is the first in the list
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    import socket

    # Create a dummy socket connection to an external address (doesn't actually connect)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Google's public DNS IP
    ip = get_client_ip(request)
    s.close()
    print(f"Your local IP address is: {ip}")
    if ip:
        return JsonResponse({'message' : f"Your local IP address is: {ip}"})
    else:
        return JsonResponse({'error' : "Error "}, status=500)
