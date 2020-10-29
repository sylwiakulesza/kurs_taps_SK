liczby = [1,2,3,4,5]
"""
for i in liczby:
    print(liczby)


for i in range (10): #zostana wypisane liczby id 0 do 9
    print(i)
for i in range(15,17): #zostaną wypisane liczby 15 i 16, ale juz nie bedzie zawieralo sie 17,
    print(i)           # petla if wykona sie 2 razy


licznik = 0
while licznik < 10:
    print(licznik)
    licznik += 1

licznik1 = 0
while True:
    print(licznik1)
    licznik1 += 1
    if licznik1 >= 2:
        break
"""
for x in range(20):
    if x % 2 == 0:
        continue
    print(x)
