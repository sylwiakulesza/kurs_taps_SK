x = 5
print(x == 2)
print(x != 2)
print(x > 590)

imie = 'Sylwia'
nazwisko = 'Kulesza'
wiek = 26

if nazwisko == 'Kulesza' and wiek == 26:
    print('Czesc Kulesza, masz 26 lat')
else:
    print('to nie Ty!')


if imie in ['Sylak', 'Siśka'] and wiek == 26:
    print('Czesc Kulesza, masz 26 lat')
else:
    print('nie jestes Sylak ani Siśka')

zmienna1 = 1
zmienna2 = 2
zmienna3 = 3

if zmienna1 > 0:
    print('1')
elif zmienna2 < 0:
    print('2')
else:
    print('same falsy')

zmienna4 = -1

if zmienna4 > 0:
    print('1')
elif zmienna2 == 2:
    print('2')
else:
    print('same falsy')
