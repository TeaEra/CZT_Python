# _*_ coding: utf-8 _*_
#
# Author: TeaEra
# Created date: 2014-08-28

def search_range(A, target):
    if not A:
        return [-1, -1]
    if len(A) == 1:
        if A[0] == target:
            return [0, 0]
        else:
            return [-1, -1]
    min_num = A[0]
    max_num = A[-1]
    if target < min_num or target > max_num:
        return [-1, -1]
    start_idx = 0
    end_idx = len(A)
    mid_idx = (start_idx + end_idx) / 2
    #
    if A[mid_idx] == target:
        left_part = A[start_idx:mid_idx]
        right_part = A[mid_idx:end_idx+1]
        left_pos = search_range(left_part, target)
        right_pos = search_range(right_part, target)
        if left_pos[-1] != -1 and right_pos[-1] != -1:
            return [left_pos[0], len(left_part) + right_pos[-1]]
        elif left_pos[-1] == -1 and right_pos[-1] == -1:
            return [-1, -1]
        elif left_pos[-1] == -1:
            return \
                [len(left_part) + right_pos[0], len(left_part) + right_pos[-1]]
        elif right_pos[-1] == -1:
            return left_pos
    elif A[mid_idx] < target:
        right_pos = search_range(A[mid_idx+1:], target)
        if right_pos[-1] != -1:
            return [right_pos[0]+mid_idx+1, right_pos[-1]+mid_idx+1]
        return right_pos
    elif A[mid_idx] > target:
        left_pos = search_range(A[:mid_idx], target)
        return left_pos

if __name__ == "__main__":
    #
    print("---")
    #print(search_range([5, 7, 7, 8, 8, 10], 8))
    #print(search_range([8, 10], 8))
    print(search_range([0,0,0,0,0,1,2,3,3,3,4,4,4,5,5,7,7,7], 6))