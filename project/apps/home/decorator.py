from time import time


def measure_execution_time(func):
    def time_measurer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        execution_time = time() - start
        print(f"\n\nExecution time is {execution_time}\n\n")
        return result, execution_time
    return time_measurer   
  