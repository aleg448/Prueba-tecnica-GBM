from races import process_input

def multiple_races():
    test_input = "3 10\n1 2 3 4 5 6 7 8 9 10\n10 1 2 3 4 5 6 7 8 9\n9 10 1 2 3 4 5 6 7 8\n2\n5 5 4 3 2 1\n3 10 5 1\n0 0\n"
    expected_output = ["3", "3"]
    results = process_input(test_input)
    assert results == expected_output, f"Expected {expected_output}, but got {results}"
    print("Broom, Broom, Success!!")

if __name__ == "__main__":
    multiple_races()