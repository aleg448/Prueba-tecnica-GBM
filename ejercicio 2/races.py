
#Calculate points
    #position, system
    #is position in range of the system?
    #return points, otherwise 0
def calculate_points(position, system):
    if position < len(system):
        return system[position]
    return 0
#determine champions
def determine_champions(races, systems, P):
    #results, system
    champions_list = []
    for system in systems:
        K, points = system
        scores = [0] * P
        #pilots from race length
        for race in races:
            for pilot in range(P):
                position = race[pilot] - 1
                #each position and pilot calls calculate_points
                scores[pilot] += calculate_points(position, points)
        #list of list to capture points
        max_score = max(scores)    
        #return champions for each system
        champions = [str(pilot + 1) for pilot in range(P) if scores[pilot] == max_score]
        champions_list.append(" ".join(champions))
    return champions_list

#read and split input, end at 0 0
def process_input(input_data):
    data = input_data.strip().split('\n')
    idx = 0
    #count line
    results = []
    #loop until 0 0
    #read G and P, split and map
    while True:
        G, P = map(int, data[idx].split())
        idx += 1
        if G == 0 and P == 0:
            break
        #map races  
        races = []
        for _ in range(G):
            race = list(map(int, data[idx].split()))
            races.append(race)
            idx += 1
        #read systems
        S = int(data[idx])
        idx += 1
        systems = []
        for _ in range(S):
            system_input = list(map(int, data[idx].split()))
            K = system_input[0]
            points = system_input[1:]
            systems.append((K, points))
            idx += 1
        #call determine_champion for each system
        champions_list = determine_champions(races, systems, P)
        #return champions 
        results.extend(champions_list)  
    return results

def run_test_case():
    test_input = """\
1 3
3 2 1
3
3 5 3 2
3 5 3 1
3 1 1 1
3 10
1 2 3 4 5 6 7 8 9 10
10 1 2 3 4 5 6 7 8 9
9 10 1 2 3 4 5 6 7 8
2
5 5 4 3 2 1
3 10 5 1
2 4
1 3 4 2
4 1 3 2
2
3 3 2 1
3 5 4 2
0 0
"""
    results = process_input(test_input)
    for result in results:
        print(result)

if __name__ == "__main__":
    run_test_case()
    #main()
    #uncomment to run with inputs