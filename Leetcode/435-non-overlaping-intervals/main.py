from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        :return: Минимальное число интервалов, убрав которые интервалы не
        будут пересекаться

        Сортируем интервалы по началу
        Если cur[0] < prev[1] (текущий начинается раньше чем заканчивается предыдущий)
        Убираем интервал с самым дальним концом, потому что у него больше шансов пересечься
        """
        intervals = sorted(intervals, key=lambda x: x[0])
        erase_intervals_cnt = 0
        previous = intervals[0]
        for ind in range(1, len(intervals)):
            current = intervals[ind]
            # Если интервалы пересекаются
            if current[0] < previous[1]:
                erase_intervals_cnt += 1
                # Если конец предыдущего больше текущего, то исключить предыдущий
                if previous[1] > current[1]:
                    previous = current
                # Иначе исключить текущий
            else:
                previous = current
        return erase_intervals_cnt


if __name__ == '__main__':
    intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
    print(Solution().eraseOverlapIntervals(intervals))