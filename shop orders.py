orders = [120, 45, 300, 85, 15, 250, 60, 400]
vip_orders = []
small_orders = []
total_orders = 0
small_order_count = 0

for order in orders:
    total_orders += order
    if order < 50:
        small_order_count += 1
    if order >= 100:
        vip_orders.append(order)
    else:
        small_orders.append(order)

average = total_orders / len(orders)

print("total orders:", total_orders)
print("vip orders:",vip_orders)
print("small order amount", small_order_count)
print("Average Order Amount:", average)

