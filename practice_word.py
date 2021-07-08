# Escribir un programita que me reciba una cadena de texto/caracteres y me devuelva un diccionario con cada palabra que contiene y cada cuanto se repite
# Programita con funciona que reciba el diccionario anterior y me regrese una tupla con la palbra mas repetida

# Cuenta el # que aparece en cada palabra 

def count_word(text):
    text = text.split()
    # 'hola mundo saludos' -> ['hola', 'mundo', 'saludos'] 
    word = {}
    for i in text:
        if i in word:
            word[i] += 1
        else:
            word[i] = 1
    return word


def max_repeated(words):
    max_word = ''
    max_repeat = 0
    for word, freq in words.items():
        # todos son mayores hasta que se demuestre lo contrario
        if freq > max_repeat:
            max_word = word
            max_repeat = freq
    return max_word, max_repeat 

text = 'Hola mundo mundo mundo como estas tu tu tu tu tu'
print(count_word(text))
print(max_repeated(count_word(text)))



