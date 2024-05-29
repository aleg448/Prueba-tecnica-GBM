#input, clean text and whitespaces, join into single continuous string
P="".join(c.lower() for c in input("Ingresa texto a verificar:") if c.isalnum())
#reverse text, compare text and reverse
#return "Es palindromo",else return "No es palindromo"
print("Es Palindromo" if P==P[::-1] else "No es Palindromo")
