from jumping import minimum_jumps, process_test_cases

def test_nonsense_value():
    input_data = "empanada"
    expected_result = "Empty due to execution error"
    result = process_test_cases(input_data)
    print(result)
    if result == expected_result:
        print("Success")
    else:
        print(f"Failed?. Expected {expected_result}, but got {result}")
if __name__ == "__main__":
    test_nonsense_value()