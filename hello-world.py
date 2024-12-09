# hola mundo
# mi primer comienzo en python con varios ejercicios

print('Hola mundo')
print("Hola mundo")

"""
Como 
poner
comentarios
de varias
líneas.
"""

'''
En python se pueden usar " o ' para strings,
al igual que en varios
lenguajes de back.
'''

#usando type & print
'''
type: especifica el tipo de objeto

'''
#print strg

print(type('Hola mundo ^^'))

a =8

x = type(a)

print(x)

# print tuple

b = ('kazutora', 'juuzou', 'L')

y = type (b)

print (y)

# estoy experimentando con print y type jiji

# print float

c = 5.5

z = type(c)

print(z)

# print complex int

h = 1+3j

m = type(h)

print (m)

# print type list

animes= ["Shingeky no Kyojin", "Desu Noto", "Tokyo Revengers"]

print(animes)

# print type set

characters = {"Eren Yeager", "Sano Manjiro", "Kamado Tanjiro"}

print(characters)

# print type dictionary

anime =	{
  "snk": "Levi Ackerman",
  "kny": "Inosuke Hashibira",
  "dn": "Light Yagami"
}
print(anime)

# print dictionary but only printing single item

anime1 = {
 "snk": "Levi Ackerman",
 "kny": "Inosuke Hashibira",
 "dn": "Light Yagami"
}

print(anime1["kny"])

'''
type imprime str,int, tuple, etc...

el primero ejemplo imprime string = string
el segundo ejemplo imprime numero integrado = int
el tercer ejemplo imprime un objeto float = float
el cuarto ejemplo imprime un objeto boolean = bool
el quinto ejemplo imprime un objeto tuple = tuple
el sexto ejemplo imprime un complex number = complex
el septimo ejemplo imprime list data type = list
el octavo ejemplo imprime set = set
el noveno ejemplo imprime dictionary = dict
'''

# type str 2° metodo
print(type('Lunita'))

# type int 2° metodo
print(type(8)) # otro modo de type sin la formula jeje


# type 2° metodo float
print(type(5.5)) # objeto float


# type bool 2° metodo
print(type(True)) # objeto bool


# type tuple 2° metodo
print(type((9.8, 3.14, 2.7)))


# type complex numb 2° metodo
print(type(9+8j))


# type list 2° metodo
print(type([animes])) # tomado del quinto ejemplo superior ^^

# type set 2° metodo

print(type({"Manjiro Sano","Baji Keisuke","Ken Ryujugi"}))

# type dictionary 2° metodo

print(type(anime))

'''

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢽⣿⣿⢿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣤⣤⣤⣤⣤⣤⣤⣤⣄⣀⣀⡀⠀⠀⠀⠀⠠⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠠⠐⠂⠉⠉⣹⠛⠂⠈⠉⠉⠉⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣛⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢾⣿⣿⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠄⠀⠉⢈⣉⠁⠐⠤⢑⠀⣠⣤⣀⠤⠤⠤⠀⠀⠉⠿⣿⣿⣿⣿⣿⣷⣿⣶⣿⣾⣭⣿⣽⣿⡿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⠊⠀⠒⠀⠉⠁⠒⠯⣢⣀⢸⠞⠋⠁⠰⣶⣤⣌⡒⠶⢤⣀⠀⠉⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣟⣿⣻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⠀⠀⠀⠀⠀⠀⠠⠂⠈⠀⠀⠀⠐⢒⣒⣶⣦⠄⠀⠑⢞⠛⢷⡄⠈⢢⣀⠉⠑⠀⡘⠕⠠⠀⠙⢽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣿⠀⠀⠀⠀⠀⠐⠀⡀⠂⢀⠄⠀⠉⢀⡤⣴⠇⢐⣦⡣⠈⢈⠐⢽⡄⠈⡝⢷⣦⡀⠈⠀⠀⠐⠄⠈⢝⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠑⠤⡒⠁⡠⡊⠔⠊⠀⢀⠔⠚⡡⠊⠀⣠⡏⢹⣧⢳⡀⢓⢄⡅⠀⣇⠀⠐⡌⠢⠀⠀⢀⠀⠆⠈⠚⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣀⣄⣤⣠⣤⣤⣤⣤⣤⣤⣼⣿⣿⣿⣿⣧⣧⣤⣼⣿⠟⠀⠀⠀⡀⡃⠜⠠⠃⠀⣠⢻⠇⣸⢤⠸⡟⡀⡀⠄⠀⡄⢇⠀⠘⡀⠀⠀⠘⢄⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⣿⢿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠌⠈⠀⡐⠁⢀⣴⠃⣾⠀⢸⢧⠀⡇⢀⢱⠆⢠⡇⠈⢧⠀⢨⠂⡀⠀⠈⢆⠀⢸⠀⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿
⠛⠉⠛⠑⠛⠛⠛⠛⠛⠛⠻⣿⣿⣿⣿⠛⠉⢉⠇⠀⠀⡠⠂⠐⠀⡠⠀⢀⣾⢻⠀⡇⠀⢸⠀⠀⠂⢸⡸⠀⡜⠈⡀⠈⣧⠀⠂⠈⢄⠀⠀⡇⡏⠂⠘⢿⣿⣿⣿⢿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠋⣍⣀⡀⠀⠔⠁⠀⣠⣾⠃⢀⣾⡏⠰⠀⡇⠀⠈⠀⠀⠀⢸⠃⣸⡇⠀⢡⠀⠹⡄⠸⡐⡀⢣⠀⡹⡅⠀⡀⡂⠝⠛⠛⠛⠛⠻⠿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⠀⠀⢀⠃⡄⠀⢠⣾⣻⡏⠀⣞⣿⠁⠘⠀⡇⠀⢀⠀⠀⠀⡀⣴⠁⡇⠀⠘⠐⡄⢳⠘⣇⢜⠀⠁⠁⠁⠀⢋⠂⡀⠀⠀⠀⠀⠀⠐⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠛⠿⣿⣿⠀⠀⡈⢐⡄⢀⡟⠀⡏⡇⢸⢸⣯⠀⠀⠀⡇⠀⢸⠀⠀⡈⠀⣿⠀⡧⠀⠀⣇⢿⣾⡘⡌⡞⡘⣆⠀⢰⠀⢸⠀⠉⠀⠀⠀⠀⠀⠈⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠀⠀⡠⠛⠛⢄⠄⢤⢸⣇⠾⡇⠀⠁⠠⣟⠸⢏⠀⠀⡄⢿⠀⢸⡄⠀⠁⢘⡼⠀⢳⠀⠀⣿⣀⣿⡅⢱⢣⠁⢻⡄⢸⣧⡈⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡄⠊⢸⠀⠀⡠⠂⠀⠀⣻⡈⡀⢀⠈⠀⠘⣧⠀⢸⠂⢠⢹⣼⡄⠠⡇⠀⢀⢾⡷⠀⡟⡇⢀⣿⠿⠋⢡⡼⢾⡄⢸⢻⣼⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣴⠟⠓⠲⠏⠠⠂⢠⠀⣠⠞⡙⣿⡿⠛⡀⡄⡀⣿⣀⠎⠀⣼⡞⣿⣷⡀⢧⠀⣰⣿⠙⡘⢰⣳⡘⠁⠀⠤⢺⠃⡿⢁⠈⠀⢿⢧⣀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠰⠑⣿⠀⠀⢰⣀⣷⡶⠥⠚⠉⠉⠓⠻⠇⠀⢃⢹⣷⡼⠁⣀⣼⣏⣸⡿⠻⠷⢼⢄⢸⢇⡾⠀⣌⡟⠀⠀⠀⠀⠈⠀⠇⢸⢰⠀⢸⡞⢃⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⢀⠁⠀⢻⠀⡀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⢀⡞⡖⣿⢷⠿⣷⣼⠛⣯⠙⠒⠂⢘⡚⡏⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀⠀⣼⢻⢀⣼⡇⠘⡀⠀⠀⠀⠀⠀⠀⢠⣿⢀
⠀⠀⠀⠀⡈⠀⠀⠈⡄⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣂⣤⢿⡃⣸⢆⠘⣿⣇⠻⡄⠀⠀⠀⠙⠁⠀⠀⢦⣀⢀⠠⠀⠀⠀⠀⠀⡰⢃⠞⢿⡟⠀⠀⠰⡖⠒⠒⠒⠒⢒⣾⠇⠈
⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠈⠀⠀⠀⠀⠀⠀⢀⣤⠏⢸⡟⠁⢸⣷⠙⣆⣧⣸⣷⢱⣿⣄⠀⠀⠀⠀⠀⠀⢀⣈⣀⣠⠔⠂⠀⠀⣴⡇⠃⠀⡠⠁⠀⠀⠀⠈⢦⡀⠀⠀⣾⡏⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⢠⡶⢿⢿⠟⢀⢼⠀⠀⣾⡿⠀⠙⠈⢻⠙⢧⣻⡊⣷⣦⣀⣀⡠⠤⠭⠭⠿⠐⠒⠒⠒⠚⠿⢤⣤⠞⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⡿⢠⣿⣿
⠀⠀⠀⠀⠀⠀⢂⠀⢀⠔⠀⠀⠀⠀⡾⣱⠓⢁⡴⢂⢿⡀⠀⠘⡿⠀⠀⠀⠀⠀⢀⣘⠽⣮⡟⠁⠀⡀⠠⠔⠒⢸⠀⠀⠀⠀⠀⠀⠀⠀⠁⠂⠄⡀⠀⠀⠀⡈⠀⠀⠙⢧⠃⣻⣿
⠀⠀⠀⠀⠀⠀⢀⠔⠁⠀⠀⠀⣠⠴⠓⡡⠖⠉⢀⣾⡈⠃⠀⠀⡁⠀⠀⠀⠀⣠⠛⢻⣿⡟⠀⡠⠀⠀⢀⡠⠐⢉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢀⠀⠀⡇⠀⠀⠀⠀⠉⠻⣻
⠀⠀⠀⠀⠀⡔⠁⠀⠀⠀⡔⠉⢠⡞⠉⠀⠀⠀⣾⢻⣧⠀⠀⠀⠁⠀⠀⣴⣿⣿⠀⢠⠋⠀⢰⠀⠀⡄⠁⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⢠⠃⠀⠀⠀⠀⠀⠀⠈
⠀⠀⢀⣠⡞⠠⠁⠀⠀⠐⠁⢀⢠⠃⠀⠀⢀⡜⢻⣎⢿⡀⠀⢸⠀⡠⠾⠯⠴⡏⠀⡔⠀⢀⠆⡠⠊⠀⣠⣶⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀
⣶⣾⠀⣟⠿⡀⠀⠀⡰⠁⠀⠀⠈⣀⣀⢴⡟⠀⢸⣿⡀⠇⢠⠣⠀⠀⠀⠀⠀⠱⠀⢙⠀⣞⡀⢊⣤⠾⠉⠉⠻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀
⡿⠁⠀⠸⣗⢦⠀⢠⠁⠈⣉⢉⠝⠁⠀⢺⠀⠀⢸⡟⠁⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡴⣏⡹⠛⠁⠀⠀⠀⠀⠘⡄⠐⠤⡄⠀⠀⠀⠀⠀⠀⠀⠘⠀⠀⡄⠘⡀⠀⠀⠄⠀⠀⠀
⠁⠀⠀⠀⠙⣿⣢⠃⠀⠤⠛⠁⠀⠀⠀⢸⡀⠀⢸⡇⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠇⠂⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⠤⠄⣀⡀⠀⠀⠀⠀⠀⠀⢂⡐⠀⠀⡇⠀⢠⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⡼⢃⠀⢸⢱⠘⠃⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠙⢿⠒⠢⢄⢸⠁⠀⠀⠘⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠸⠀⢀⠐⠀⠀⠀⠀⠀⠰⠁⠈⠀⡸⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠎⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀⠀⠣⠀⢈⡆⠀⠀⠀⠀⢣⠂⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⣷⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⢀⣀⠀⠀⠀⠀⠐⢆⠄⠀⠀⠀⠀⠈⡏⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⡀⠀⢀⠔⠁⢠⡏⢄⡇⠀⠀⠀⠀⠀⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠩⠭⠉⠒⣌⢢⣀⠀⠀⠀⠀⢓⠀⠀⠀⠀

'''