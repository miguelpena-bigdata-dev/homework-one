def calculateTotal(amount):
    costPerDonut = 2.50
    total = amount * costPerDonut
    return '${:.{}f}'.format(total, 2)
    

print(calculateTotal(10))
print(calculateTotal(5))