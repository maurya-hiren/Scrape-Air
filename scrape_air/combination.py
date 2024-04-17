
string_array = ["DEL", "BOM", "BLR", "HYD", "MAA", "CCU", "AMD", "COK", "GOI", "PNQ"]

def generate_combinations(locations):
    combinations = []
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:  
                combinations.append(f"{locations[i]} - {locations[j]}")
    return combinations

all_combinations = generate_combinations(string_array)

for combination in all_combinations:
    print(combination)

print(f"Total number of combinations: {len(all_combinations)}")
