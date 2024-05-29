from palindromo import es_palindromo
def test_palindromo():
    assert es_palindromo("%perritotirrep") == "Es palindromo"

if __name__ == "__main__":
    test_palindromo()
    print("Prueba exitosa!")