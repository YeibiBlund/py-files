# import your functions here
from utils import files

# read the quijote here
book = files.readFile('el_quijote.txt')
book2 = files.readFile('el_quijote_ii.txt')
bookCompleto = book+book2

# Word Count
print('Palabras totales: ', files.wordCount(bookCompleto))


# Unique Word Count
# print('Unique Word Count: ', files.uniqueWordCount(book))

# Quijote count
# print('find Content: ', files.findContent(book, 'quijote'))
# print('find Content: ', files.findContent(book, 'sancho'))

# Change Quijote to Quixote and write it to a new file "el_quixote.txt"
# print('Change Quijote to Quixote: ', files.changeQuijoteToQuixote(book))
