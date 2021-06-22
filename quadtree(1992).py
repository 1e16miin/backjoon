import sys

n = int(input())
data = [list(map(int, input())) for _ in range(n)]

ans = ""

def is_white(img):
    # print(img)
    if 1 not in img:
        return True


def is_black(img):
    # print(img)
    if 0 not in img:
        return True


def swap(img, ret):
    width = len(img[0])
    height = len(img)

    if width == 1 or height == 1:
        # print(img)
        return ret
    if is_white(img):
        # print(img)
        return "w"
    elif is_black(img):
        return "b"

    ret += "x"
    for i in range(width):
        for j in range(height):
            ret += swap(img[0:width // 2][0:height // 2], ret)
            ret += swap(img[0:width // 2][height // 2:height], ret)
            ret += swap(img[width // 2:width][0:height // 2], ret)
            ret += swap(img[width // 2:width][height // 2:height], ret)


print(data)
print(data[0:n // 2][0:n // 2])
#
# print(swap(data, ans))