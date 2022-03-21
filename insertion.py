from ntpath import join
import time 

f = open('c:/Users/Pc/Desktop/c/veri/tersten_sirali.txt','r')   
sayilar = f.read().lower()

list1 = []
list1 = sayilar.split(" ")
list2 = []
i = 0
for sayi in list1:
    a = int(list1[i])
    list2.append(a)
    i+=1
print(list2)

start_time_naive = time.time() 

def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
             
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        array[j + 1] = key


insertionSort(list2)
print('siralanmis sayilar : ')
print(list2)

end_time_naive = str(time.time() - start_time_naive) 
print(end_time_naive+"s")