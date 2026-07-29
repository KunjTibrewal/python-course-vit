#a is not equal to b
a = 2
b = 4
print(bool(a == b))
# Following also prints the same
print(a == b)
# Returns False as a is None
a = None
print(bool(a))
# Returns false as a is an empty sequence
a = ()
print(bool(a))
# Returns false as a is 0
a = 0.0
print(bool(a))
#integer
a = 10
print(type(a))
print(a)
#float 
a = 10.5
print(type(a))
print(a)
a = 10
print(type(a))
print(a)
#binary 
b = 0b1010
print(type(b))
print(b)
#octal 
c = 0o12
print(type(c))
print(c)
#hexadecimal 
d = 0xB
print(type(d))
print(d)
