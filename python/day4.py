#den 4 v pythonu 31.srpna 2022
def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
         return "Bonjour"
    else:
         return "hello"

greet("en")
greet("fr")
greet("cz") # = = en

#return statement


print(greet("en") , "Pepis")
print(greet("fr") , "Bary")
