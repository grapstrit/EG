'''
¬ — Логическое отрицание (NOT).
В Python: not

Пример: not x
Λ — Логическая конъюнкция (И, AND).
В Python: and

Пример: x and y
V — Логическая дизъюнкция (ИЛИ, OR).
В Python: or

Пример: x or y
⊕ — Логическое исключающее ИЛИ (XOR).
В Python: ^

Пример: x ^ y
→ — Импликация (если... то, IF...THEN).
В Python: (not x) or y

Пример: (not x) or y
↔ или ≡ — Логическая эквиваленция (эквивалентность, IF AND ONLY IF).
В Python: ==

Пример: x == y
⊤ — Истина (TRUE).
В Python: True

Пример: True
⊥ — Ложь (FALSE).
В Python: False

Пример: False
'''


'''
print("Задача 1:")
print("x y z w F")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int((x <= (y == w)) and (y == (w <= z)))
                if (x+y+z+w in [1]) or (x+y+z+w >= 2 and F == 1):
                    print(x, y, z, w, F)


            
y   x   w   z   F
1   0   0   1   1
0   0   1   0   1
0   0   0   1   0


F()
F(0001)=0
F(0010)=1

Задача 1:
x y z w F
0 0 0 1 1
0 0 1 0 0+
0 1 0 0 1
0 1 1 0 1+
'''


'''
print("Задача 2:")
print("x y z w F")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int((x == (not y)) <= ((x and w) == (z and (not w))))
                if F == False:
                    print(x, y, z, w, F)
                print("")
                print("x y w z")
'''


'''
print("Задача 3:")
print("x y z w F")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int(((x <= y) == (w <= x)) and (z <= w))
                if F == True: 
                    print(x, y, z, w, F)
                print("")
                print("w x y z")
'''



'''
print("Задача 4:")
print("x y z w F")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int(((not z) == y) <= ((w and (not x)) == (y and x)))
                if F == False:
                    print(x, y, z, w, F)
                print("")
                print("z y w x")
'''



'''
print("Задача 5:")
print("x y z w F")
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int(((not x) and (not y)) or (y == z) or (not w))
                if F == False:
                    print(x, y, z, w, F)
                print("")
                print("y x z w")
'''

def G(N):
    if N == 0:
        return "0"
    three = ""
    while N > 0:
        three = str(N % 3) + three
        N //= 3
    return three

def F(N):
    s = str(N)
    
    if N % 3 == 0:
        s = s + str(-3)
    else:
        s = str((N % 3) * 3)
    
    r = int(s, 2)
    return r

for N in range(1, 12 + 1):
    r = F(N)
    print(N, r)