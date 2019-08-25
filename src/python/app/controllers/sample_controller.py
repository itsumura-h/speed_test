from django.http.response import JsonResponse
from ..services.domain_services.sample_service import SampleService

class SampleController:
    def fib(self, num):
        new_num = int(num)
        data = SampleService().fib(new_num)
        return JsonResponse(data)
