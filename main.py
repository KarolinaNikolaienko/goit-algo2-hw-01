from task_1 import min_max
from task_2 import min_k


def main():
    # Task 1
    print("Task 1")
    arr = [9, 4, 2, -7, 3, 1, 10, -11]
    print(min_max(arr))

    # Task 2
    print("Task 2")
    arr = [18, 30, -2, 1, -10, 76, 9, -43]
    print(min_k(arr, 3))
    print(min_k(arr, 6))

    arr = [38, 27, 43, 3, 9, 82, 10]
    print(min_k(arr, 1))
    print(min_k(arr, 7))


if __name__ == "__main__":
    main()
