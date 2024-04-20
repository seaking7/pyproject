def print_triangle(n):
    num = 1
    triangle = []
    for i in range(n):
        row = []
        for j in range(n - i):
            row.append(num)
            num += 1
        triangle.append(row)

    # 배열에 담은 숫자를 출력
    for i in range(n):
        index = i
        for j in range(i + 1):
            print(triangle[j][index], end=" ")
            index -= 1
        print()

# t를 입력받는다
t = int(input())

# 숫자를 입력받으면서 반복
for i in range(t):
    number = int(input())
    print_triangle(number)
    print()