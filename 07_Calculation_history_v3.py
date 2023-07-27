
# display history
print("\nCalculation History:")
    for i in range(1, len(calculation_history_A) + 1):
        print("Calculation {}".format(i))
        print("Area: {:.2f}".format(calculation_history_A[i - 1]))
        print("Perimeter: {:.2f}".format(calculation_history_P[i - 1]))
