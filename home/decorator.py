from time import time


def measure_execution_time(func):
    def time_measurer(*args, **kwargs):
        start = time()
        return func(*args, **kwargs), time() - start

    return time_measurer
