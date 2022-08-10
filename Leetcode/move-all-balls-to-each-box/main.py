from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        answer = [0] * len(boxes)
        # count only left required operations
        ones_cnt = 0
        prev_left_operations = 0
        for ind, box in enumerate(boxes):

            answer[ind] += prev_left_operations + ones_cnt

            # prepare for next iteration
            prev_left_operations += ones_cnt
            if box == '1':
                ones_cnt += 1
        # do the same for right
        ones_cnt = 0
        prev_right_operations = 0
        for ind in range(len(boxes)-1, -1, -1):
            box = boxes[ind]
            answer[ind] += prev_right_operations + ones_cnt

            prev_right_operations += ones_cnt
            if box == '1':
                ones_cnt += 1
        # answer is coorect because left+right = total number of operations required
        return answer


if __name__ == '__main__':
    print(Solution().minOperations('110'))