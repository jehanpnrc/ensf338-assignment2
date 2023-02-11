import sys
sys.setrecursionlimit(20000)
import matplotlib.pyplot as plt
import json

from threading import stack_size
stack_size(33554432)
from time import perf_counter

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi-1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high

with open("ex2.json") as f:
    data = json.load(f)
    
timingresult = []
size = []

for arr in data:
    timestart = perf_counter()
    low = 0
    high = len(arr) - 1
    
    func1(arr, low, high)
    timestop = perf_counter()
    size.append(len(arr))
    timingresult.append(timestop-timestart)
    
print(timestop-timestart)
plt.plot(size, timingresult)
plt.xlabel("Size")
plt.ylabel("Time (seconds)")
plt.show()




