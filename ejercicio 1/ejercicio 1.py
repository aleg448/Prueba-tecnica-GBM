def es_palindromo():
    P="".join(c.lower() for c in input("Ingresa texto a verificar:") if c.isalnum())
    resultado="Es Palindromo" if P==P[::-1] else "No es Palindromo"
    print(resultado)
es_palindromo()

"""
input, clean text and whitespaces, join into single continuous string
reverse text, compare text and reverse, return "Es palindromo",else return "No es palindromo"
"""