lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8


def two_sum(lst, target):
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if target == lst[i] + lst[j]:
                return (i, j)

def two_sum_hashed(lst, target):
    dict = {}
    final = []
    for i in range(len(lst)):
        dict[i] = target - lst[i]
        sec_value = list(filter(lambda value: value == target - dict.get(i), dict.values()))

if __name__ == "__main__":
    print(two_sum([1, 2, 1, 3], 2))
    assert two_sum(lst, target) == (0, 6), "Базовый тестовый набор (test case)"
    assert two_sum([1, 1, 2, 3], 2) == (0, 1), "test case #2"
    assert two_sum(list(range(1000000)), 999999) == (0, 999999)