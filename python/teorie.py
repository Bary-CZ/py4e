#note's for bary!
x = "hello " + "there" #strings + concatenate = put together
print(x)
ddd = 5 - 1  # interger
print(ddd)

# x = 1 + hi NELZE

print(type(x)) #string
print(type("x"))  #type odpoví nám co je to string,variable nebo interger takže "class"!
print(type(1)) #interger = celá čísla

print(float(100) + 20)    #výsledek 120,0 float = číslo "s desetinnou čárkou"

# u dělení je pokaždé výsledek = (float)
print(10 / 10) # = 1.0

f = "123"
f = int(f) #změní ze slova na celé číslo NELZE použít na písmena!!
g = 1
print(f + g)
             #USER INPUT
name = input("kdo jsi?")
print ("vítej", name) #počká než uživatel něco napíše!

inp = input("Zadej číslo vytahu v eu a dostaneš podlaží usa")
usf = int(inp) + 1
print('usa podlaží', usf )
#oprava
#if else elif
x = 2
if x < 2 :
    print("small")
elif x < 10 : #elif bůže výt více
    print("medium")
else :
    print("Large")
print("all done")

#den 3 v pythonu 30.srpna 2022
#functions
def thing() :  #zapamutuje si,kod který můžeme využít vícekrát! thing() = pojmenovani
    print("hello")
    print("fun")
thing() #function můžeme přivolat vicekrát v kodu!
print("zip")
thing() #function můžeme přivolat vicekrát v kodu!
#určíme funkci def

#if statementx
x = 5
if x < 10:
    print('smaller')
if x > 20:
    print("bigger")

print("finis")
#indentation
#this ↓ doesn't work for some reason
x = 4
if x > 2 :
    print ("Bigger")
else :
    print("smaller")
print "All done"
