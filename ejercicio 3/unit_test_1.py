from jumping import minimum_jumps, process_test_cases

def test_minimum_value():
    input_data = "1\n1"
    expected_result = "1"
    result = process_test_cases(input_data)
    print(result)
    if result == expected_result:
        print("Success")
    else:
        print(f"Failed. Expected {expected_result}, but got {result}")
if __name__ == "__main__":
    test_minimum_value()