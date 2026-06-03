def activity_selection(start, finish):

    activities = list(zip(start, finish))

    activities.sort(key=lambda x: x[1])

    count = 1
    last_finish = activities[0][1]

    for s, f in activities[1:]:

        if s >= last_finish:
            count += 1
            last_finish = f

    return count


n = int(input("Enter number of activities: "))

start = list(map(int, input("Enter start times: ").split()))
finish = list(map(int, input("Enter finish times: ").split()))

print("Maximum Activities =", activity_selection(start, finish))