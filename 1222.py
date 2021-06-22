for test_case in range(1,11):
    N = int(input())
    numbers = list(map(int, input().split("+")))
    print("#" + str(test_case) + " " + str(sum(numbers)))