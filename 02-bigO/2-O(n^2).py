def print_items(n):

    # n^3
    for i in range(n):
        for j in range(n):
            for k in j:
                print(i, k, j)

print_items(10)