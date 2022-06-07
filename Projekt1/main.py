import random
import sys
import time
sys.setrecursionlimit(50000)

#tablica liczb losowych, te same wartosci zostana wykorzystane do kolejnych tablic posortowanych
randArray = []
for x in range(0, 300000):
    randArray.append(random.randint(0, 50))
#kopia zapasowa
randArrayCopy = randArray[:]
#tablica liczb posortowanych
sortUP = sorted(randArray)
#tablica liczb posortowanych odwrotnie
sortDOWN = sortUP[::-1]
#kopia zapasowa
sortDOWNcopy = sortDOWN[:]

####################################################################
#                            quicksort                             #
####################################################################

def partition(tablica, p, r):
    x = tablica[r]
    i = p - 1
    j = p
    for j in range(p, r):
        if tablica[j] <= x:
            i += 1
            tablica[j], tablica[i] = tablica[i], tablica[j]
    tablica[i + 1], tablica[r] = tablica[r], tablica[i + 1]
    return i + 1

def quick(tablica, p, r):
    if p < r:
        q = partition(tablica, p, r)
        quick(tablica, p, q - 1)
        quick(tablica, q + 1, r)

def quicksort(tablica):
    quick(tablica, 0, len(tablica) - 1)

##############################POMIAR################################

print("quicksort sortUP:")
start_time = time.time()
quicksort(sortUP)   #PROGRAM WYRZUCA ERROR, POMIAR PRZEPROWADZONO OSOBNO W DRUGIM PLIKU
print(time.time()-start_time)

print("quicksort sortDown:")
start_time = time.time()
quicksort(sortDOWN)    #PROGRAM WYRZUCA ERROR, POMIAR PRZEPROWADZONO OSOBNO W DRUGIM PLIKU
print(time.time()-start_time)
sortDOWN = sortDOWNcopy[:]

print("quicksort random: ")
start_time = time.time()
quicksort(randArray)
print(time.time()-start_time)
randArray = randArrayCopy[:]

####################################################################
#                            heapsort                              #
####################################################################

def heap(tablica, lenght, rodzic_id):
    rodzic = rodzic_id
    lew = 2*rodzic+1
    praw = 2*rodzic + 2
    if lew < lenght and tablica[lew] > tablica[rodzic]:
        rodzic = lew

    if praw < lenght and tablica[praw] > tablica[rodzic]:
        rodzic = praw

    if rodzic != rodzic_id:
        tablica[rodzic], tablica[rodzic_id] = tablica[rodzic_id], tablica[rodzic]
        heap(tablica, lenght, rodzic)

def heapsort(tablica):
    start_time = time.time()
    lenght = len(tablica)
    for i in range (lenght // 2 -1, -1, -1):
        heap(tablica, lenght, i)

    for i in range(lenght-1, 0, -1):
        tablica[i], tablica[0] = tablica[0], tablica[i]
        heap(tablica, i, 0)
    return time.time()-start_time

##############################POMIAR################################

print("heapsort sortUP: ")
start_time = time.time()
heapsort(sortUP)
print(time.time()-start_time)

print("heapsort sortDown: ")
start_time = time.time()
heapsort(sortDOWN)
print(time.time()-start_time)
sortDOWN = sortDOWNcopy[:]

print("heapsort random: ")
start_time = time.time()
heapsort(randArray)
print(time.time()-start_time)
randArray = randArrayCopy[:]

####################################################################
#                            mergesort                             #
####################################################################

def mergesort(tablica):
    start_time = time.time()
    i = 0
    j = 0
    k = 0
    if len(tablica) > 1:
        s = len(tablica) // 2
        lew = tablica[:s]
        praw = tablica[s:]
        mergesort(lew)
        mergesort(praw)

        while i < len(lew) and j < len(praw):
            if lew[i] < praw[j]:
                tablica[k] = lew[i]
                i += 1
            else:
                tablica[k] = praw[j]
                j += 1
            k += 1

        while i < len(lew):
            tablica[k] = lew[i]
            i += 1
            k += 1

        while j < len(praw):
            tablica[k] = praw[j]
            j += 1
            k += 1
    return time.time()-start_time

##############################POMIAR################################

print("mergesort sortUP: ")
start_time = time.time()
mergesort(sortUP)
print(time.time()-start_time)

print("mergesort sortDown: ")
start_time = time.time()
mergesort(sortDOWN)
print(time.time()-start_time)
sortDOWN = sortDOWNcopy[:]

print("mergesort random: ")
start_time = time.time()
mergesort(randArray)
print(time.time()-start_time)
randArray = randArrayCopy[:]

####################################################################
#                            bubble sort                           #
####################################################################

def bubblesort(tablica):
    start_time = time.time()
    for i in range(len(tablica)):
        for k in range(0, len(tablica) -1 - i):
            if tablica[k] > tablica[k+1]:
                tablica[k], tablica[k+1] = tablica[k+1], tablica[k]
    return time.time() - start_time

##############################POMIAR################################

print("bubblesort sortUP: ")
start_time = time.time()
bubblesort(sortUP)
print(time.time()-start_time)

print("bubblesort sortDown: ")
start_time = time.time()
bubblesort(sortDOWN)
print(time.time()-start_time)
sortDOWN = sortDOWNcopy[:]

print("bubblesort random: ")
start_time = time.time()
bubblesort(randArray)
print(time.time()-start_time)
randArray = randArrayCopy[:]
