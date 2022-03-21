from ntpath import join
import time
print("DOSYA MENUSU : \n1)input.txt dosyasi\n2)sirali.txt dosyasi\n3)tersten_sirali.txt dosyasi\n")

sayi = int(input("lutfen islem yapmak istediginiz dosya numarasini giriniz : "))
if sayi == 1 :

    f = open('c:/Users/Pc/Desktop/c/veri/input.txt','r')   
    sayilar = f.read().lower()

    list1 = []
    list1 = sayilar.split(" ")
    list2 = []
    i = 0
    for sayi in list1:
        a = int(list1[i])
        list2.append(a)
        i+=1
    
    print("\nSORT MENUSU : \n1)selection sort\n2)bubble sort\n3)insertion sort\n4)shell sort\n5)dosyadaki sira")
    sayi1 = int(input("lutfen yapmak istediginiz islemi giriniz : "))
    if sayi1 == 1 :
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
    elif sayi1 == 2 :
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
    elif sayi1 == 3 :
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
    elif sayi1 == 4 :
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
    elif sayi1 == 5 :
        print(list2)
    else :
        print("lutfen gecerli bir sayi giriniz!")

elif sayi == 2 :
    f = open('c:/Users/Pc/Desktop/c/veri/sirali.txt','r')   
    sayilar = f.read().lower()

    list1 = []
    list1 = sayilar.split(" ")
    list2 = []
    i = 0
    for sayi in list1:
        a = int(list1[i])
        list2.append(a)
        i+=1
    
    print("\nSORT MENUSU : \n1)selection sort\n2)bubble sort\n3)insertion sort\n4)shell sort\n5)dosyadaki sira")
    sayi1 = int(input("lutfen yapmak istediginiz islemi giriniz : "))
    if sayi1 == 1 :
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
    elif sayi1 == 2 :
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
    elif sayi1 == 3 :
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
    elif sayi1 == 4 :
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
    elif sayi1 == 5 :
        print(list2)
    else :
        print("lutfen gecerli bir sayi giriniz!")

elif sayi == 3 :
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
    
    print("\nSORT MENUSU : \n1)selection sort\n2)bubble sort\n3)insertion sort\n4)shell sort\n5)dosyadaki sira")
    sayi1 = int(input("lutfen yapmak istediginiz islemi giriniz : "))
    if sayi1 == 1 :
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
    elif sayi1 == 2 :
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
    elif sayi1 == 3 :
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
    elif sayi1 == 4 :
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
    elif sayi1 == 5 :
        print(list2)
    else :
        print("lutfen gecerli bir sayi giriniz!")

else :
    print("lutfen gecerli bir numara giriniz!")

