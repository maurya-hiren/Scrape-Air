# Airport_Codes = ["DEL", "BOM", "BLR", "HYD", "MAA", "CCU", "AMD", "COK", "GOI", "PNQ"]

def generate_combinations(locations):
    combinations = []
    for i in range(len(locations)):
        for j in range(len(locations)):
            if i != j:  
                combinations.append(f"{locations[i]}-{locations[j]}")
    
    return combinations
# all_combinations = generate_combinations(Airport_Codes)

# for combination in all_combinations:
    # print(combination)

