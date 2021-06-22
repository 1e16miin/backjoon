import copy


T = int(input())


for test_case in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    answer = set()
    answer.add(0)
    for score in scores:
        temp = copy.deepcopy(answer)
        for s in answer:
            temp.add(s+score)

        answer = answer.union(temp)

    print("#" + str(test_case), end=" ")
    print(len(answer))

