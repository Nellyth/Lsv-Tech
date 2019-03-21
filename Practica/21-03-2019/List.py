a=0
language = ['French', 'English', 'German']

def prueba1():
    global a
    a=2
def prueba2():
    prueba1()
    c=a
    print(c)

def extend():
    # language tuple
    language_tuple = ('Spanish', 'Portuguese')

    # language set
    language_set = {'Chinese', 'Japanese'}

    # appending element of language tuple
    global language
    language.extend(language_tuple)

    print('Extend List List: ', language)

    # appending element of language set
    language.extend(language_set)

    print('Extend List Dicc: ', language)

def remove(dato):
    #delete a data for your information
    global language
    language.remove(dato)
    print("Remove:           ",language)

def pop(dato):
    #delete a data in a position
    global language
    language.pop(dato)
    print("Pop:              ",language)

def clear(language):
    #Clear all list
    language.clear()
    print("Clear:            ",language)

def count(dato):
    #Count the number of times a piece of information is repeated on the list.
    global language
    language_tuple = ('Spanish', 'Portuguese')
    language.extend(language_tuple)
    language.extend(language_tuple)
    print("List:             ", language)
    print("Count:            ",language.count(dato))

def insert(pos,dato):
    #insert a data in a given position
    global language
    language.insert(pos, dato)
    print("Insert:           ", language)

def sort():
    #Order the list
    global language
    language.sort()
    print("Sort Ascendant:   ", language)
    language.sort(reverse=True)
    print("Sort Descendant:  ", language)

def split():
    #Separate a String
    cad="Hola Mundo"
    print("separate chain:   ",cad.split())

prueba2()
extend()
remove('English')
pop(0)
clear(language)
count("Spanish")
insert(3,"English")
sort()
split()
