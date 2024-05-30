from races import process_input

def single_race():
    test_input = "1 3\n3 2 1\n3\n3 5 3 2\n3 5 3 1\n3 1 1 1\n0 0\n"
    expected_output = ["3", "3", "1 2 3"]
    results = process_input(test_input)
    assert results == expected_output, f"Expected {expected_output}, but got {results}"
    print("Broom, Success!")

if __name__ == "__main__":
    single_race()