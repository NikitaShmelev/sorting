from .decorator import measure_execution_time
from django.contrib import messages


class Algorithm:


    @measure_execution_time
    def bubble(self, list_to_sort):
        for i in range(len(list_to_sort)):
            for j in range(len(list_to_sort) - 1):
                if list_to_sort[j] > list_to_sort[j+1]:
                    list_to_sort[j], list_to_sort[j+1] = list_to_sort[j+1], list_to_sort[j]
        return list_to_sort


    @measure_execution_time
    def insertion(self, list_to_sort):  
        for i in range(1, len(list_to_sort)):  
            key = list_to_sort[i] 
            j = i-1
            while j >= 0 and key < list_to_sort[j] : 
                    list_to_sort[j + 1] = list_to_sort[j] 
                    j -= 1
            list_to_sort[j + 1] = key 
        return list_to_sort
       

    @measure_execution_time
    def merge(self, list_to_sort):
        def mergeSort(list_to_sort):
            if len(list_to_sort) > 1:
                mid = len(list_to_sort) // 2
                left = list_to_sort[:mid]
                right = list_to_sort[mid:]
                mergeSort(left)
                mergeSort(right)
                i, j, k = 0, 0, 0
                while i < len(left) and j < len(right):
                    if left[i] < right[j]:
                        list_to_sort[k] = left[i]
                        i += 1
                    else:
                        list_to_sort[k] = right[j]
                        j += 1
                    k += 1

                while i < len(left):
                    list_to_sort[k] = left[i]
                    i += 1
                    k += 1

                while j < len(right):
                    list_to_sort[k]=right[j]
                    j += 1
                    k += 1
            return list_to_sort
        return mergeSort(list_to_sort)
