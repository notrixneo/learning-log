def analyze_orders(orders):
    total = sum(orders)
    average = total / len(orders)
    largest = max(orders)
    return total, average, largest

monday_orders = [100, 50, 25, 75]
tuesday_orders = [200, 150, 300]


mon_total, mon_avg, mon_lar = analyze_orders(monday_orders)
tue_total, tue_avg, tue_lar = analyze_orders(tuesday_orders)

print(f"total: {mon_total} Average ${mon_avg:.2f} Largest order: {mon_lar}")
print(f"total: {tue_total} Average ${tue_avg:.2f} Largest order: {tue_lar}") 