
# display history
print("\nCalculation History:")
    for i, (area, perimeter) in enumerate(zip(calculation_history_A,calculation_history_P), start=1):
        print("Calculation {} - Area: {:.2f}, Perimeter: {:.2f}".format(i, area, perimeter))
