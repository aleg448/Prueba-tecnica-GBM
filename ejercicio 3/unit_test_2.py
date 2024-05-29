from jumping import minimum_jumps, process_test_cases

def test_normal_value():
    input_data = "5\n1\n2\n3\n4\n5"
    expected_result = "1\n3\n2\n3\n4"
    result = process_test_cases(input_data)
    print(result)
    if result == expected_result:
        print("Success")
    else:
        print(f"Failed. Expected {expected_result}, but got {result}")
if __name__ == "__main__":
    test_normal_value()