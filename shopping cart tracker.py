prices = [15, 80, 42, 5, 99, 30]
total = 0
expensive_items = []


for price in prices:
    total += price
    if price >= 50:
        expensive_items.append(price)

print("total:", total)
print("expensive items:", expensive_items)
        