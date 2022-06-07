#STRUKTURA DANYCH ZAWIERAJACA LITERE + WARTOSC ORAZ DANE DO DRZEWA W KODOWANIU HUFFMANA#
class Alfabet:
    def __init__(self, count, chr, lew=None, praw=None):
        self.chr = chr
        self.count = count
        self.lew = lew
        self.praw = praw
        self.wart = ""
    def __lt__(self, tmp):
        return self.count < tmp.count
###


####KOPIEC START####
def kopiec_create(kopiec, i):
    lew = 2 * i + 1
    praw = 2 * i + 2
    if lew < len(kopiec) and kopiec[lew] < kopiec[i]:
        min = lew
    else:
        min = i
    if praw < len(kopiec) and kopiec[praw] < kopiec[min]:
        min = praw
    if min != i:
        kopiec[i], kopiec[min] = kopiec[min], kopiec[i]
        kopiec_create(kopiec, min)


def kopiec(kopiec):
    for i in range(len(kopiec) // 2 - 1, -1, -1):
        kopiec_create(kopiec, i)
####KOPIEC END####


#EXTRACT MIN XY, BUDOWA DRZEWA HUFFMANA
def extractMinXY(tree):
    #UZYCIE KOPCA
    kopiec(tree)
    lew = tree[0]
    lew.wart = "0"
    if len(tree) > 2:
        if (tree[1] < tree[2]):
            praw = tree[1]
            praw.wart = "1"
        else:
            praw = tree[2]
            praw.wart = "1"
    elif len(tree) == 2:
        praw = tree[1]
        praw.wart = "1"
    #TWORZENIE NOWEGO RODZICA
    temp = Alfabet(lew.count + praw.count, lew.chr + praw.chr, lew, praw)
    #DODAWANIE NOWEGO RODZICA
    tree.append(temp)
    #TEST WIAZAN
    print("Tworzenie wiazan: ")
    print("lew: ", lew.chr, " praw: ", praw.chr, " rodzic_nxt: ", "'", temp.chr, "'")
    #USUWANIE WYKORZYSTANYCH ELEMENTOW TABLICY
    tree.remove(lew)
    tree.remove(praw)
###


#ODCZYTANIE Z DRZEWA HUFFMANA KODOW DLA LITER
def generujKody(tree, tmp='', final = []):
    code = tmp + str(tree.wart)
    if (tree.lew != None):
        generujKody(tree.lew, code)
    if (tree.praw != None):
        generujKody(tree.praw, code)
    if (len(tree.chr) == 1):
        final.append(Alfabet(code, tree.chr))
    return final
###


#TLUMACZENIE TEKSTU NA KOD BINARNY PRZEZ KODY KUFFMANA
def translate(input):
    output = ""
    for i in input:
        for j in final:
            if j.chr == i:
                output = output + str(j.count)
    return output
###


#KONWERSJA CIAGU BITOWEGO DO TEKSTU
def encode(input, output=''):
    for i in range(0, len(input), 7):
        tmp = input[i:i+7]
        dec = int(tmp,2)
        output = output + chr(dec)
    return output
###


# DEKLARACJA ALFABETU, ZNAKOW UZYWANYCH W PROGRAMIE
a = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'u', 'p', 'r', 's', 't', 'w',
    'z', 'y', 'x', ' ',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'U', 'P', 'R', 'S', 'T', 'W',
    'Z', 'Y', 'X'
]

#OTWARCIE PLIKU INPUT ORAZ KONWERSJA NA TABLICE CHAROW
input_file = open('input', "r")
input_string = input_file.read()
input_file.close()
input_char = []
for i in input_string:
    input_char.append(i)
input_char.remove('\n')

#ZLICZENIE LITER WYSTEPUJACYCH W INPUCIE DO TABLICY DANE
alfabet = []
for i in a:
    temp = Alfabet(0, i)
    alfabet.append(temp)
for i in alfabet:
    for k in input_char:
        if i.chr == k:
            i.count += 1

dane = []
for i in alfabet:
    if i.count != 0:
        dane.append(i)


#OBIEG FUNKCJI Z KOLEJKA PRIORYTETOWA RAZY LICZBA ELEMENTOW - 1
for i in range(0, len(dane) - 1):
    extractMinXY(dane)

#LISTA KODOW HOFFMANA DLA KAZDEJ LITERY
final = generujKody(dane[0])
#OUTPUT ZAPISANY W POSTACI BINARNEJ
output = (translate(input_char))
#OUTPUT ZAPISANY Z POSTACI BINARNEJ DO STANDARDOWEGO KODOWANIA
output_bin = encode(output)

#TEST
print("\nkod binarny: ", output)
print("\nkod binarny na standardowe kodowanie: ", output_bin)
print("\nkody HUFFMANA: ")
for i in final:
    print(i.chr, i.count)

#ZAPISANIE WSZYSTKICH WYNIKOW
output_file = open('output', "w")
for i in final:
    tmp = i.chr, i.count
    output_file.write(str(tmp))
    output_file.write("\n")
output_file.write("\n")
output_file.write(output)
output_file.write("\n")
output_file.write(output_bin)
output_file.close()


#ZAPISANIE POSTACI ZASZYFROWANEJ DO POROWNANIA ROZMIAROW Z PLIKIEM INPUT
output_file_bin = open('output.bin', "w")
output_file_bin.write(output_bin)
output_file_bin.close()


