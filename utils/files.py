def readFile(name):
    with open(name, "r", errors="ignore") as file:  
        return file.read()    #  .read  LEE EL CONTENIDO DEL ARCHIVO ESPECIFICADO Y LO DEVUELVE COMO CADENA.

def wordCount(text):
  palabras_totales = len(text.split())
  return palabras_totales

def uniqueWordCount(text):
  palabras_totales = text.split()     #  .split  SEPARA UNA UNA CADENA DE TEXTO Y LA CONVIERTE EN UNA LISTA(ARRAY)
  palabras_unicas = set(palabras_totales)
  return len(palabras_unicas)

def findContent(text, word):
    palabras_totales = text.split()      #  .split  SEPARA UNA UNA CADENA DE TEXTO Y LA CONVIERTE EN UNA LISTA(ARRAY)
    total_palabras = palabras_totales.count(word)     #  .count  CUENTA EL NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA LISTA
    return total_palabras

def quijote_count(text):
    #text = text.lower()      # .lower  CONVIERTE UN TEXTO A MINUSCULAS. (NO ES NECESARIO USARLO PORQUE QUIJOTE Y SANCHO SIEMPRE VAN EN MAYUSCULAS)
    
    quijote_count = text.count("Quijote")
    sancho_count = text.count("Sancho")
    
    return quijote_count, sancho_count


def modificarYcrearTxt(test):
   bookCompleto_modificado = test.replace("Quijote", "Quixote")
   with open('el_quixote.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(bookCompleto_modificado)
   return



#  .read   |  LEE EL CONTENIDO DEL ARCHIVO ESPECIFICADO Y LO DEVUELVE COMO CADENA.
#  .split  |  SEPARA UNA UNA CADENA DE TEXTO Y LA CONVIERTE EN UNA LISTA(ARRAY)
#  .count  |  CUENTA EL NUMERO DE VECES QUE APARECE UN ELEMENTO EN UNA LISTA
#  .lower  |  CONVIERTE UN TEXTO A MINUSCULAS. QUIJOTE:  2203   
