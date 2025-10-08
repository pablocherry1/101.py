'''
Strings
''' 

my_string = "Este es un string \ncon salto de linea"

print(my_string)

my_tab_string = "\tEste es un string con tabulacion"

print(my_tab_string)

name, surname, age = "JP", "Hodgins", 31

print("Linea con marcadores \nNombre: {} \nNickname: {} \nEdad: {}".format(name, surname, age))

print("Linea con marcadores \nNombre: %s \nNickname: %s \nEdad: %d"%(name, surname, age))