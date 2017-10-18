from random import choice

#we have 46 symbols
symbols =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","@","!","%","&","/","(",")","=",";","^"]
print(symbols)
ID = 0

for i in symbols:
    ID = ID + 1

a = choice(symbols)
print(a, a, a, a, a)

#print(randint(1,30), randint(1,30), randint(1,30), randint(1,30), randint(1,30), randint(1,30))
