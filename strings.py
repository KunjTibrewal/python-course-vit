a = "kunj"
b = '''hello how are you?
i am good'''
print(a)                       #kunj
print(b)                       #hello how are you?
                               #i am good
print(a[0])                    #k
for i in a:
    print(i)                    #k
                                #u
                                #n
                                #j
print(len(a))                   #4
print(a[0:3])                   #kun
print(a[0:3:2])                 #kn
print(a[:4])                    #kunj
print(a[0:-3])                  #k
print(a.upper())                #KUNJ
c = "!!!rahul!!!!"
print(c.rstrip("!"))            #!!!rahul
print(c.lstrip("!"))            #rahul!!!!
print(c.strip("!"))             #rahul
print(c.replace("!", ""))       #rahul
d = "hello how are you?"
print(d.split(" "))              #['hello', 'how', 'are', 'you?']
print(a.center(20, "*"))         #*******kunj********
print(a.count("u"))             #1
print(a.find("j"))              #3
print(a.find("z"))              #-1
print(a.capitalize())           #Kunj
print(a.isalpha())              #True
print(a.endswith("j"))          #True