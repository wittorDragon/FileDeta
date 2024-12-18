import mmToList as mm
import time

start_time = time.time()  # เริ่มจับเวลา

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        
        for j in range(0,n-i-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

def dataSpell():
    sp = []
    for i in range(len(l)):
        sp.append(mm.spell(l[i]))
    return sp

l = mm.dataTolist()
sp = dataSpell()
data = []

# for i in range(len(sp)):
#     data.append(bubble_sort(sp[i]))

# for i in range(0,10):
#     print(l[i])
#     print(data[i],'\n')


end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")
