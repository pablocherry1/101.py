'''
Strings
''' 

my_string = "Este es un string \ncon salto de linea"

print(my_string)

my_tab_string = "\tEste es un string con tabulacion"

print(my_tab_string)

name, surname, age = "juan pablo", "Hodgins", 31

print("Linea con marcadores Nombre: {} Nickname: {} Edad: {}".format(name, surname, age))

print("Linea con placeholders Nombre: %s Nickname: %s Edad: %d"%(name, surname, age))

print(f"string literals o interpolacion Nombre: {name} Nickname: {surname} Edad: {age}")

print(name.capitalize())

print(name.upper())

print(name.count("b"))