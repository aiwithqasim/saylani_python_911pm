# ERRORS
# 1- : was missing in the function
# 2- indentation was wrong
# 3- formula to caluclate total & product was wrong += (total) and *= (product)

def perform_operations(numbers): 
    total = 0
    product = 1
    for num in numbers:
        total += num
        product *= num
    average = total / len(numbers)
    return total, product, average

def main():
    numbers = [1, 2, 3, 4, 5]
    total, product, average = perform_operations(numbers)
    print("Total:", total)
    print("Product:", product)
    print("Average:", average)

if __name__ == "__main__":
    main()
