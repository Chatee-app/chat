from .models import IPLog

class LogIPMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Get the IP address from the request
        ip_address = request.META.get('REMOTE_ADDR', None)
        
        # Save the IP address and timestamp to the database
        if ip_address:
            IPLog.objects.create(ip_address=ip_address)
        
        response = self.get_response(request)
        return response
