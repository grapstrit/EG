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
                print(x, y, z, w, F)
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
'''