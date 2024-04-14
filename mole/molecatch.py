import pygame, random

pygame.init()
# 게임창 옵션
size = (1000, 1000)
screen = pygame.display.set_mode(size)
title = 'MOLECATCH'
pygame.display.set_caption(title)
# 게임내 필요설정
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
x_list = [170, 500, 830]
y_list = [250, 597, 919]


def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)


bg_img = pygame.image.load("mole_bg.png")
bg_img = pygame.transform.smoothscale(bg_img, size)
mole_img = pygame.image.load("mole1.png")
mole_size = mole_img.get_size()
mole_size = tup_r((mole_size[0] * 0.6, mole_size[1] * 0.6))
mole_img = pygame.transform.smoothscale(mole_img, mole_size)

mole_crop = 0
mole_move = 5
mole_stage = 0

exit = False

# 메인 이벤트
while not exit:
    clock.tick(60)
    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(pygame.mouse.get_pos())

    if mole_stage == 0:
        if random.random() < 0.1:
            mole_stage = 1
    elif mole_stage == 1:
        mole_crop += mole_move
        if mole_crop >= mole_size[1]:
            mole_stage = 2
            mole_crop = mole_size[1]

    mole_img_cropped = mole_img.subsurface((0, 0, mole_size[0], mole_crop))
    mole_pos = tup_r((x_list[0] - mole_size[0] / 2, y_list[0] - mole_crop))

    # 그리기
    screen.blit(bg_img, (0, 0))
    screen.blit(mole_img_cropped, mole_pos)
    pygame.display.flip()

pygame.quit()
