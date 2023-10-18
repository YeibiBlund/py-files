# import your functions here    //   IMPORTAR LA CLASE DONDE ESTAN LAS FUNCIONES
from utils import files

# read the quijote here    // LEER ARCHIVO TXT Y PASARLO A CADENA 
book = files.readFile('el_quijote.txt')
book2 = files.readFile('el_quijote_ii.txt')
bookCompleto = book+book2

print('Libro Completo: ', bookCompleto)

# Word Count    // CONTADOR DE PALABRAS TOTALES   .wordcount
print('Palabras totales: ', files.wordCount(bookCompleto))

# Unique Word Count    // CONTADOR DE PALABRAS UNICAS 
print('\nPalabras Unicas: ', files.uniqueWordCount(bookCompleto))

# Quijote count    //CONTADOR DE PALABRAS EN CONCRETO  "QUIJOTE" "SANCHO"
quijote, sancho = files.quijote_count(bookCompleto)
print('\nVeces que se utiliza la palabra QUIJOTE: ', quijote)
print('Veces que se utiliza la palabra SANCHO: ', sancho)

# Change Quijote to Quixote and write it to a new file "el_quixote.txt"   //COPIAR TEXTO Y CREAR UN ARCHIVO TXT
files.modificarYcrearTxt(bookCompleto)
print('Change Quijote to Quixote: True')
