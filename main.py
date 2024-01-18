import time


def triplets(nums: list) -> list:
    result = []
    length = len(nums)
    for i in range(length - 2):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if nums[i] * nums[j] * nums[k] == 0 and i != j != k != i:
                    result.append([nums[i], nums[j], nums[k]])
    return result


if __name__ == "__main__":
    start_time = time.time()
    input_nums = [1, 2, 0, 3, 0, 4]
    triplets_result = triplets(input_nums)
    print(triplets_result)
    end_time = time.time()
    print(start_time, end_time)
    print(f"Время выполнения: {end_time - start_time} секунд")
