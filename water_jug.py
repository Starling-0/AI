def check(x, y, visited=set()):
    return (x, y) in visited

def waterjug(x, y, a, b, f1, f2, n, visited=set()):
    if check(x, y, visited):
      return

    if x == f1 and y == f2:
        print(f"Water Jug completed in {n} steps.")
        exit(1)
    visited.add((x, y))
    #print(x, y)

    # Recursive calls for all possible jug operations
    waterjug(0, y, a, b, f1, f2, n + 1, visited)           # Empty Jug 1
    waterjug(x, 0, a, b, f1, f2, n + 1, visited)           # Empty Jug 2
    waterjug(a, y, a, b, f1, f2, n + 1, visited)           # Fill Jug 1
    waterjug(x, b, a, b, f1, f2, n + 1, visited)           # Fill Jug 2
    waterjug(min(x + y, a), max(0, x + y - a), a, b, f1, f2, n + 1, visited)  # Pour from Jug 2 to Jug 1
    waterjug(max(0, x + y - b), min(x + y, b), a, b, f1, f2, n + 1, visited)  # Pour from Jug 1 to Jug 2

# inputs
x = int(input("Capacity of Jug 1: "))
y = int(input("Capacity of Jug 2: "))
a = int(input("Total Capacity of Jug 1: "))
b = int(input("Total Capacity of Jug 2: "))
f1 = int(input("Final capacity of Jug 1: "))
f2 = int(input("Final capacity of Jug 2: "))
n = 0
waterjug(x, y, a, b, f1, f2, n)