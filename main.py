import time


def triplets(nums: list) -> list:
    result = set()
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] == 0 or nums[j] == 0 or nums[k] == 0:
                    result.add(tuple(sorted([nums[i], nums[j], nums[k]])))
    return [list(triplet) for triplet in result]


if __name__ == "__main__":
    start_time = time.time()
    input_nums = [1, 2, 0, 3, 0, 4]
    triplets_result = triplets(input_nums)
    print(triplets_result)
    end_time = time.time()
    print(start_time, end_time)
    print(f"Время выполнения: {end_time - start_time} секунд")
