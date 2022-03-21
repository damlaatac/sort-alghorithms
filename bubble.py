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

start_time_naive1 = time.time()

def bubbleSort(array):
    
  for i in range(len(array)):

    for j in range(0, len(array) - i - 1):

      if array[j] > array[j + 1]:

        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp


bubbleSort(list2)

print('siralanmis sayilar : ')
print(list2)

end_time_naive = str(time.time() - start_time_naive1) 
print(end_time_naive+"s")