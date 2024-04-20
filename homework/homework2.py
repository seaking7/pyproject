def print_hourglass(size):
    index = 0

    # size만큼 줄반복
    for i in range(size):
        # size만큼 문자 찍기
        char = 0
        while char < size :
            # 시작할때 - 기호 찍기
            if char >= index and char <= size - index - 1:
                if char % 2 == 1:
                    print("+", end="")
                else:
                    print("*", end="")
            else:
                print("-", end="")
            char += 1

        # 줄바꿈 수정
        print("")

        # 인덱스 조정
        if i < size/2 -1:
            index += 1
        else:
            index -= 1

case_cnt = int(input())
while case_cnt > 0:
    hourglass_size = int(input())

    print_hourglass(hourglass_size)

    case_cnt -= 1