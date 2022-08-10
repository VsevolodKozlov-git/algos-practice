class Solution():
    def main(self, item_day):
        items = len(item_day)
        days = len(item_day[0])
        dp = [[0] * days for _ in range(1 << items)]

        shift = 0
        for i in range(1 << items):
            if 1 << shift == i:
                assign_val = item_day[shift][0]
                shift += 1
            else:
                assign_val = float('inf')
            dp[i][0] = assign_val

        for day in range(1, days):
            for sub_set in range(1, 1 << items):
                dp[sub_set][day] = dp[sub_set][day-1]
                for item in range(items):
                    cur_price = item_day[item][day]
                    min_sum = dp[sub_set ^ (1 << item)][day-1]
                    if (1 << item) & (sub_set):
                        dp[sub_set][day] = min(dp[sub_set][day],
                                               min_sum + cur_price)
        return dp[1 << items - 1][-1]


if __name__ == '__main__':
    item_day = [[9, 2, 1],
                [2, 2, 7],
                [3, 7, 1]]
    print(Solution().main(item_day))
