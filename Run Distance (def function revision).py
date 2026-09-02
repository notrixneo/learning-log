"""
Exercise: Running Tracker Analysis
Mistakes Made:
- Forgot the colon at the end of the `def` statement.
- Placed the guard clause outside the function body instead of at the top.
- Accidentally called the function inside itself (recursion) instead of checking `len(distance)`.

Key Learnings:
- Guard clauses must be at the very top of the function to catch empty lists before math is attempted.
- Checking `len(distance) == 0` prevents a ZeroDivisionError.
"""


def analyze_run(distance):
    if len(distance) == 0:
            return 0, 0, 0
    
    total = sum(distance)
    average = total / len(distance)
    longest = max(distance)
    return total, average, longest
    

monday_run = [5.2, 3.4]
tuesday_run = []
wednesday_run = [6.8]
thursday_run = [4.1, 2.5, 5.0]
friday_run = [8.3, 3.0]

mon_total, mon_average, mon_long = analyze_run(monday_run)
tue_total, tue_average, tue_long = analyze_run(tuesday_run)
wed_total, wed_average, wed_long = analyze_run(wednesday_run)
thur_total, thur_average, thur_long = analyze_run(thursday_run)
fri_total, fri_average, fri_long = analyze_run(friday_run)

print(f"Total Run Distance Monday: {mon_total:.2f} Average {mon_average:.2f} Longest run: {mon_long:.2f}")
print(f"Total Run Distance Tuesday: {tue_total:.2f} Average {tue_average:.2f} Longest run: {tue_long:.2f}")
print(f"Total Run Distance Wednesday: {wed_total:.2f} Average {wed_average:.2f} Longest run: {wed_long:.2f}")
print(f"Total Run Distance Thursday: {thur_total:.2f} Average {thur_average:.2f} Longest run: {thur_long:.2f}")
print(f"Total Run Distance Friday: {fri_total:.2f} Average {fri_average:.2f} Longest run: {fri_long:.2f}")