def es_palindromo(texto):
    P="".join(c.lower() for c in texto if c.isalnum())
    resultado="Es palindromo" if P==P[::-1] else "No es palindromo"
    print(resultado)
    return resultado

"""
input, clean text and whitespaces, join into single continuous string
reverse text, compare text and reverse, return "Es palindromo",else return "No es palindromo"
"""