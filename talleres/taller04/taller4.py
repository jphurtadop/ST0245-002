import random
from matplotlib import pyplot as pl
import time

def array_generator(len):
    """List generator"""
    array = [0] * len
    for i in range(len):
        array[i] = i

    return array

def arrayMax(arr):
    return arrayMax_aux(arr, 0, 0)

def arrayMax_aux(arr, i, max):
    if i == len(arr):
        return max
    else:
        if arr[i] > max:
            max = arr[i]
        return arrayMax_aux(arr, i+1, max)

def groupSum_aux(list, start, target):
    if start >= len(list): return target == 0
    return groupSum_aux(list, start + 1, target - list[start]) \
            or groupSum_aux(list, start + 1, target)

def groupSum(list, target):
    return groupSum_aux(list, 0, target)

#----------------------------Fibonacci---------------------------------#

def fib_r(n):                             #Fibonacci recursivo
    if n <= 1: return n
    return fib_r(n-1) + fib_r(n-2)