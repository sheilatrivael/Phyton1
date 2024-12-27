def middle(a, b, c):
    largest = max(a, b, c)
    smallest = min(a, b, c)
    median = (a + b + c) - (largest + smallest)
    return median
    
y = middle(1, 2, 3)