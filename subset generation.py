def generate(arr, index, current):

    if index == len(arr):
        print(current)
        return

    generate(arr, index + 1, current)

    generate(arr, index + 1,
             current + [arr[index]])


def generate_iterative(arr):

    n = len(arr)

    for mask in range(1 << n):

        subset = []

        for i in range(n):

            if mask & (1 << i):
                subset.append(arr[i])
        print(subset)

arr = list(map(int, input("Enter elements: ").split()))
generate_iterative(arr)

generate(arr, 0, [])