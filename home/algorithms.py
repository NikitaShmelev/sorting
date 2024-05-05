from os import listdir

from django.contrib import messages
from django.http import FileResponse

from .decorator import measure_execution_time


def create_file(list_to_sort):
    file = open("home/static/files/sorted_file.txt", "w")
    file.write(",".join([str(i) for i in list_to_sort]))
    file.close()


class Algorithm:

    @measure_execution_time
    def bubble(list_to_sort):
        for i in range(len(list_to_sort)):
            for j in range(len(list_to_sort) - 1):
                if list_to_sort[j] > list_to_sort[j + 1]:
                    list_to_sort[j], list_to_sort[j + 1] = (
                        list_to_sort[j + 1],
                        list_to_sort[j],
                    )
        create_file(list_to_sort)
        return list_to_sort

    @measure_execution_time
    def insertion(list_to_sort):
        for i in range(1, len(list_to_sort)):
            key = list_to_sort[i]
            j = i - 1
            while j >= 0 and key < list_to_sort[j]:
                list_to_sort[j + 1] = list_to_sort[j]
                j -= 1
            list_to_sort[j + 1] = key
        create_file(list_to_sort)
        return list_to_sort

    @measure_execution_time
    def merge(list_to_sort):
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
                    list_to_sort[k] = right[j]
                    j += 1
                    k += 1
            return list_to_sort

        list_to_sort = mergeSort(list_to_sort)
        create_file(list_to_sort)
        return list_to_sort

    @measure_execution_time
    def shell(list_to_sort):
        def shell_sort(list_to_sort):
            n = len(list_to_sort)
            gap = n // 2

            while gap > 0:
                for i in range(gap, n):
                    temp = list_to_sort[i]
                    j = i
                    while j >= gap and list_to_sort[j - gap] > temp:
                        list_to_sort[j] = list_to_sort[j - gap]
                        j -= gap
                    list_to_sort[j] = temp
                gap //= 2
        shell_sort(list_to_sort)
        create_file(list_to_sort)
        return list_to_sort
