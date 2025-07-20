from django.http import JsonResponse
import socket

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        # If there are multiple IPs, get the first one
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def home(request):
    client_ip = get_client_ip(request)
    print(f"🔍 Client IP address is: {client_ip}")
    
    if client_ip:
        return JsonResponse({'ip': client_ip})
    else:
        return JsonResponse({'error': "Unable to determine client IP"}, status=500)
