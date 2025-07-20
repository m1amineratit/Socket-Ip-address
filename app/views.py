from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    import socket

    # Create a dummy socket connection to an external address (doesn't actually connect)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))  # Google's public DNS IP
    local_ip = s.getsockname()[0]
    s.close()
    print(f"Your local IP address is: {local_ip}")
    if local_ip:
        return JsonResponse({'message' : f"Your local IP address is: {local_ip}"})
    else:
        return JsonResponse({'error' : "Your local IP address is"}, status=500)
