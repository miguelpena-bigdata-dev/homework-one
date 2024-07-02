def parseStringData(data: str):
    tokens = data.split()
    donut_name: str = tokens[0] + " " + tokens[1]
    donut_count: int = int(tokens[2])
    donut_cost: float = float(tokens[3]) 
    return donut_name, donut_count, donut_cost

# data_input = input("")
data_input = "Vanilla Donut 10 2.25"
donut_name, donut_count, donut_cost = parseStringData(data_input)

print(donut_name)
print(donut_count)
print(donut_cost)

