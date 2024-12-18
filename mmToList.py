#แตกสติง 1500ตัว
def dataTolist():
    l = []
    with open('d:\DSA1\week4\Data\mmHomework.txt','r', encoding='utf-8') as fin:
        for line in fin:
            n1,n2,n3,n4,n5,n6,n7,n8,n9,n10,n11,n12,n13,n14,n15,n16,n17,n18,n19 = line.split()
            l.append(n9)
    return l

#แยกสติง พร้อมแปลงเป็นเลข
def spell(l):
    sp = []
    for i in l:
        sp.append(int(i))
    return sp

#main program
# l = dataTolist()
# sp = spell(l[0]) # l[0] = "13060100"
# print(sp)


