import Bubble as bb
import mmToList as mm
import time

start_time = time.time()  # เริ่มจับเวลา

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftHalf = arr[:mid]
    rightHalf = arr[mid:]

    sortedLeft = mergeSort(leftHalf)
    sortedRight = mergeSort(rightHalf)

    return merge(sortedLeft, sortedRight)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


l = mm.dataTolist()
sp = bb.dataSpell()
unsortedArr = []

for i in range(len(sp)):
    unsortedArr.append(mergeSort(sp[i]))
print(unsortedArr[1])


end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")