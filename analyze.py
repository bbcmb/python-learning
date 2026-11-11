import csv

prices = []

with open("product.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        prices.append(float(row["price"]))

average = sum(prices) / len(prices)
highest = max(prices)
lowest = min(prices)

print("Average price:", round(average, 2))
print("Highest price:", highest)
print("Lowest price:", lowest)