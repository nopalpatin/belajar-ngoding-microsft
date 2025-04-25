#operasi logika atau boolean
#operator not (tidak)
print( 'NOT' )
a = True
c = not a
print('data a =', a)
print("NOT")
print('data c =', c)

#operator or (atau) salah satu true maka hasilnya true
print( 'OR' )
a = True
b = False
c = a or b
print(a, 'OR' ,b, '=', c)

print( 'OR' )
a = False
b = True
c = a or b
print(a, 'OR' ,b, '=', c)

print( 'OR' )
a = True
b = True
c = a or b
print(a, 'OR' ,b, '=', c)

print( 'OR' )
a = False
b = False
c = a or b
print(a, 'OR' ,b, '=', c)

#operator and (dan) kedua true maka hasilnya true
print( 'AND' )
a = True
b = False
c = a and b
print(a, 'AND' ,b, '=', c)

print( 'AND' )
a = False
b = True
c = a and b
print(a, 'AND' ,b, '=', c)

print( 'AND' )
a = False
b = False
c = a and b
print(a, 'AND' ,b, '=', c)

print( 'AND' )
a = True
b = True
c = a and b
print(a, 'AND' ,b, '=', c)

#operator xor (xor) salah satu true maka hasilnya true
print( 'XOR' )
a = True
b = False
c = a ^ b
print(a, 'XOR' ,b, '=', c)

print( 'XOR' )
a = False
b = True
c = a ^ b
print(a, 'XOR' ,b, '=', c)

print( 'XOR' )
a = False
b = False
c = a ^ b
print(a, 'XOR' ,b, '=', c)

print( 'XOR' )
a = True
b = True
c = a ^ b
print(a, 'XOR' ,b, '=', c)
