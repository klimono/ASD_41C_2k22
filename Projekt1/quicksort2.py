import random
import sys
import time
sys.setrecursionlimit(500000)

#tablica liczb losowych, te same wartosci zostana wykorzystane do kolejnych tablic posortowanych
randArray = []
for x in range(0, 30000):
    randArray.append(random.randint(0, 50))
#tablica liczb posortowanych
sortUP = sorted(randArray)
#tablica liczb posortowanych odwrotnie
sortDOWN = sortUP[::-1]


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
    start_time = time.time()
    quick(tablica, 0, len(tablica) - 1)
    return time.time()-start_time

##############################POMIAR################################

print("quicksort sortUP: ")
print(quicksort(sortUP))

print("quicksort sortDown: ")
print(quicksort(sortDOWN))

print("quicksort random: ")
print(quicksort(randArray))

