from collections import defaultdict


def get_neighbours(row, col, n_rows, n_cols):
    all_neighbours = [(row-1, col), (row+1, col), (row, col+1), (row, col-1)]
    existing_neighbours = []
    for r, c in all_neighbours:
        if (0 <= r < n_rows) and (0 <= c < n_cols):
            existing_neighbours.append((r, c))
    return existing_neighbours


def get_out_ways(row, col, n_rows, n_cols):
    out_ways = 0
    out_ways += (row == 0)
    out_ways += (row == n_rows-1)
    out_ways += (col == 0)
    out_ways += (col == n_cols-1)
    return out_ways


class Solution:
    def findPaths(self, n_rows: int, n_cols: int, max_moves: int, start_row: int, start_col: int) -> int:
        res = 0
        old_dict = defaultdict(int)
        old_dict[(start_row, start_col)] = 1
        new_dict = defaultdict(int)

        for _ in range(max_moves):
            for (row, col), in_ways in old_dict.items():
                out_ways = get_out_ways(row, col, n_rows, n_cols)
                res += in_ways * out_ways
                for neighbour in get_neighbours(row, col, n_rows, n_cols):
                    new_dict[neighbour] += in_ways
            old_dict = new_dict
            new_dict = defaultdict(int)
        return res


if __name__ == '__main__':
    print(Solution().findPaths(n_rows=1, n_cols=3, max_moves=3, start_row=0, start_col=1))