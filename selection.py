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

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])


size = len(list2)
selectionSort(list2, size)
print('siralanmis sayilar :')
print(list2)  

end_time_naive = str(time.time() - start_time_naive) 
print(end_time_naive+"s")


