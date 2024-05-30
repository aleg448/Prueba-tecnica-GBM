from races import process_input

def min_pilots():
    test_input = "1 1\n1\n1\n1 10\n0 0\n"
    expected_output = ["1"]
    results = process_input(test_input)
    assert results == expected_output, f"Expected {expected_output}, but got {results}"
    print("Is it really a SUCCESS if there's no one else?")

if __name__ == "__main__":
    min_pilots()