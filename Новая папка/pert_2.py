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

from itertools import permutations

def logical_function(x, y, z, w):
    """Функция для вычисления значения F для каждой комбинации"""
    return int((x <= (y == w)) and (y == (w <= z)))

def print_truth_table():
    """Вывод таблицы истинности для наглядности"""
    print("Задача 1:")
    print("x y z w F")
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                for w in [0, 1]:
                    F = logical_function(x, y, z, w)
                    print(x, y, z, w, F)

def match_variables_with_columns(table):
    variables = ['x', 'y', 'z', 'w']
    
    # Перебираем все возможные перестановки переменных (x, y, z, w)
    for perm in permutations(variables):
        correct = True
        for row in table:
            # Пример: perm = ('x', 'y', 'z', 'w'), значит соответствие переменных
            # row[0] -> perm[0], row[1] -> perm[1], и так далее
            mapping = {perm[i]: row[i] for i in range(4)}
            x, y, z, w = mapping['x'], mapping['y'], mapping['z'], mapping['w']
            
            # Если значение логической функции не совпадает с данными в таблице, пропускаем
            if logical_function(x, y, z, w) != row[-1]:
                correct = False
                break
        
        # Если соответствие найдено, выводим порядок переменных
        if correct:
            return ''.join(perm)

    return "No matching order found"

# Пример таблицы (4 переменные + F)
table = [
    [1, 0, 0, 1, 0],  # Пример строки таблицы истинности (включая результат F)
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1]
]

# Вывод таблицы истинности (дополнительно для наглядности)
print_truth_table()

# Найдем порядок переменных
result = match_variables_with_columns(table)
print(f"\nПорядок переменных: {result}")


