from races import process_input

def tied_champions():
    test_input = "2 4\n1 3 4 2\n4 1 3 2\n2\n3 3 2 1\n3 5 4 2\n0 0\n"
    expected_output = ["2 4", "4"]
    results = process_input(test_input)
    assert results == expected_output, f"Expected {expected_output}, but got {results}"
    print("Get two podiums in here, cause the test went well!")

if __name__ == "__main__":
    tied_champions()