import time
from typing import List


def find_triplets(src: List):
    result = set()
    src_no_zeros = [num for num in src if num != 0]
    zero_count = src.count(0)
    if zero_count == 0:
        return result

    if zero_count >= 3:
        result.add((0, 0, 0))

    if zero_count >= 2:
        for num in set(src_no_zeros):
            result.add((num, 0, 0))
            result.add((0, num, 0))
            result.add((0, 0, num))

    if zero_count >= 1:
        for n, num in enumerate(src_no_zeros):
            for num2 in src_no_zeros[n+1:]:
                result.add((0, num, num2))
                result.add((0, num2, num))
                result.add((num2, 0, num))
                result.add((num, 0, num2))
                result.add((num, num2, 0))
                result.add((num2, num, 0))

    return result


if __name__ == "__main__":
    start_time = time.time()
    input_nums = [1, 2, 0, 3, 0, 4]
    triplets_result = find_triplets(input_nums)
    print(triplets_result)
    end_time = time.time()
    print(f"Время выполнения: {end_time - start_time} секунд")
