from .decorator import measure_execution_time
from django.contrib import messages


class Algorithm:

    @measure_execution_time
    def bubble(self, array_to_sort):
        for i in range(len(array_to_sort)):
            for j in range(len(array_to_sort) - 1):
                if array_to_sort[j] > array_to_sort[j+1]:
                    array_to_sort[j], array_to_sort[j+1] = array_to_sort[j+1], array_to_sort[j]
        return array_to_sort

    @measure_execution_time
    def insertion(self, array_to_sort):  
        for i in range(1, len(array_to_sort)):  
            key = array_to_sort[i] 
            j = i-1
            while j >= 0 and key < array_to_sort[j] : 
                    array_to_sort[j + 1] = array_to_sort[j] 
                    j -= 1
            array_to_sort[j + 1] = key 
        return array_to_sort
       
    @measure_execution_time
    def merge(self, array_to_sort):
        def mergeSort(array_to_sort):
            if len(array_to_sort) > 1:
                mid = len(array_to_sort) // 2
                left = array_to_sort[:mid]
                right = array_to_sort[mid:]
                mergeSort(left)
                mergeSort(right)
                i, j, k = 0, 0, 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        array_to_sort[k] = left[i]
                        i += 1
                    else:
                        array_to_sort[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    array_to_sort[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    array_to_sort[k]=right[j]
                    j += 1
                    k += 1
            return array_to_sort
        return mergeSort(array_to_sort)
    
    