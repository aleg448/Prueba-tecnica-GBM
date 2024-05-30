from races import process_input

def max_pilots():
    test_input = "1 100\n" + " ".join(str(i+1) for i in range(100)) + "\n1\n100 " + " ".join(str(100-i) for i in range(100)) + "\n0 0\n"
    expected_output = ["1"]
    results = process_input(test_input)
    assert results == expected_output, f"Expected {expected_output}, but got {results}"
    print("All GOOD!!!")

if __name__ == "__main__":
    max_pilots()