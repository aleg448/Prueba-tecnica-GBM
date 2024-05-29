
#for y different x
    #if y<x then y=y+k, k++
    #if y>x then y=y-1, k++, return K
    #else just return k
    #calculate steps
def minimum_jumps(x):
    jumps = 0
    position = 0

    while position < x:
        jumps += 1
        position += jumps
    if position == x:
        return jumps
    if position == x + 1:
        jumps += 1
        position -= 1 

    return jumps
#read test cases as A LIST 
#process each test case   (skip first num)
#return jumps for list in dict 

def process_test_cases(input_data):
    test_cases = input_data.strip().split('\n')[1:]
    results = []
    for test_case in test_cases:
        x = int(test_case)
        result = minimum_jumps(x)
        results.append(str(result))
    return "\n".join(results)

