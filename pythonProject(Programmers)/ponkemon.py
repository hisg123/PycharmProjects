def solution(nums):

    uni_nums = list(set(nums))

    if len(nums)//2 < len(uni_nums): answer = len(nums)//2
    else: answer = len(uni_nums)

    return answer

if __name__ == '__main__':
    solution([3,1,2,3])
    solution([3,3,3,2,2,4])
    solution([3, 3, 3, 2, 2, 2])