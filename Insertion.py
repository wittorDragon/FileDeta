import Bubble as bb
import mmToList as mm
import time

start_time = time.time()  # เริ่มจับเวลา

def insertion_sort(my_array):
    n = len(my_array)
    for i in range(1, n):
        current_value = my_array[i]
        j = i - 1
        
        # เลื่อนตำแหน่งของค่าที่มากกว่า current_value ไปข้างหน้า
        while j >= 0 and my_array[j] < current_value:
            my_array[j + 1] = my_array[j]
            j -= 1
        
        # ใส่ current_value ในตำแหน่งที่ถูกต้อง
        my_array[j + 1] = current_value
    return my_array

l = mm.dataTolist()
sp = bb.dataSpell()
print(sp[0])
my_array = []

for i in range(len(sp)):
    my_array.append(insertion_sort(sp[i]))

  
print(my_array[0])

end_time = time.time()  # จับเวลาสิ้นสุด
elapsed_time = end_time - start_time  # ระยะเวลาที่ใช้

print(f"ใช้เวลา: {elapsed_time:.4f} วินาที")
