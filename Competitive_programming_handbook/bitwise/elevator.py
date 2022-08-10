
def elevator(weights, max_weight):
    people = len(weights)
    dp = [[float('inf'), 0] for _ in range(1 << people)]
    dp[0] = [1, 0]

    for s in range(1 << people):
        for person in range(people):
            if s & (1 << person):
                item = dp[s ^ (1 << person)].copy()
                last_trip_weight = item[1]
                if last_trip_weight + weights[person] <= max_weight:
                    item[1] += weights[person]
                if last_trip_weight + weights[person] > max_weight:
                    item[0] += 1
                    item[1] = weights[person]
                dp[s] = min(item, dp[s])
    all_people_subset = dp[(1 << people) - 1]
    return all_people_subset[0]


if __name__ == '__main__':
    print(elevator([2, 3, 3, 5, 6], 10))