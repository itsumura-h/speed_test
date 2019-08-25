# from datetime import datetime
from time import time
import sys
from ..application_service import ApplicationService

class SampleService:
    def fib(self, num):
        start_time = time()
        results = [
            ApplicationService().fib(i)
            for i in range(num)
        ]
        end_time = time() - start_time

        data = {
            'version': sys.version,
            'time': "{0:.4f}".format(end_time),
            'fib': results
        }
        return data
