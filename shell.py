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

def shellSort(array, n):

    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = array[i]
            j = i
            while j >= interval and array[j - interval] > temp:
                array[j] = array[j - interval]
                j -= interval

            array[j] = temp
        interval //= 2


size = len(list2)
shellSort(list2, size)
print('sıralamis sayilar : ')
print(list2)

end_time_naive = str(time.time() - start_time_naive) 
print(end_time_naive+"s")