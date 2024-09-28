'''
1.or или             \ Пример: b == 2 or b == 4 -> True
2.in принадлежит     \ Пример: 2 in [1, 2, 3] -> True
3.and И
4. == 
5. <= 
6. >=
7. not ( ! )
8. Следствие `->` (Python: <=)


1. Или          ∨       or     
2. И            ∧       and
3. Эквиваленция ≡       ==
4. Импликация   →       <=  
   Следствие    →       <=
   
5. Отрицание    !       not или !
'''
'''
# F = (x ∨ y) → (z ≡ x)
print('x y z F')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            F = int((x or y) <= (z == x))
            if (F == 0):
                print(x, y, z, F)            
            
            

x	z	y	F
-	0	0	0
-   0	-	0
'''

# ((w → y) → x) ∨ ¬z

print('x y z w F')
for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            for w in [0, 1]:
                F = int(((w <= y) <= x) or (not z))
                if(F==0):
                    print(x, y, z, w, F) 
                    


'''
x y z w F
0 0 1 0 0
0 1 1 0 0
0 1 1 1 0

z   y   w   x   F
1   1   1   0   0
1   0   -   -   0
1   1   0   0   0

'''






















