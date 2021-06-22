for test_case in range(1):
    answer = 0
    cnt = 0
    table_len = int(input())
    table = [list(map(int, input().split())) for _ in range(table_len)]
    table = list(zip(*table))
    for row in table:
        row = "".join(str(row)).replace(", ", "").strip("(|)").lstrip("2|0").rstrip("1|0")
        length = len(row)
        print(row)
        before, idx = "1", 0
        for i in range(1, length):
            if row[i] != "0":
                print(row[i])
                if row[i] != before:
                    # print(before, cnt, idx, answer)
                    answer += 0.5
                    before = row[i]
                    print(before, i)

                idx = i
                print(idx)
        cnt += 1
    print("#" + str(test_case) + " " + str(int(answer)))
