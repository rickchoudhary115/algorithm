def first_fit_decreasing(items, capacity):

    items.sort(reverse=True)

    bins = []

    for item in items:

        placed = False

        for i in range(len(bins)):

            if bins[i] + item <= capacity:
                bins[i] += item
                placed = True
                break

        if not placed:
            bins.append(item)

    return len(bins)


items = list(map(int, input("Enter item sizes: ").split()))
capacity = int(input("Enter bin capacity: "))

print("Bins Required =", first_fit_decreasing(items, capacity))