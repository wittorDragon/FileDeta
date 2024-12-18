import Bubble as bb
import mmToList as mm
import time

start_time = time.time()   # เริ่มจับเวลา

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high): # run
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]


    array[i+1], array[high] = array[high], array[i+1]
    return i+1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index-1)
        quicksort(array, pivot_index+1, high)
    return array

l = mm.dataTolist()
sp = bb.dataSpell()
my_array = []
for i in range(len(sp)):
    my_array.append(quicksort(sp[i]))

print(my_array[0])



end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")



