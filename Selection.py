import Bubble as bb
import mmToList as mm
import time

start_time = time.time()  # เริ่มจับเวลา

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        index = i 
        for j in range(i+1,n):
            if arr[index] < arr[j]:
                index = j
        arr[i],arr[index] = arr[index],arr[i]
    return arr

def sort(arr,n,i):
    s = []
    s.append(arr[i])
    for h in range(n):
        if h == i:
            continue
        else:
            s.append(arr[h])
    return s


#main program
l = mm.dataTolist()
sp = bb.dataSpell()
data = []
for i in range(len(sp)):
    data.append(selection_sort(sp[i]))
    print(data[i])


end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")
