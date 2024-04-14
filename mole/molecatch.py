import pygame
import random

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
mole_img1 = pygame.image.load("mole1.png")
mole_img2 = pygame.image.load("mole2.png")
mole_size = mole_img1.get_size()
mole_size = tup_r((mole_size[0] * 0.6, mole_size[1] * 0.6))
mole_img1 = pygame.transform.smoothscale(mole_img1, mole_size)
mole_img2 = pygame.transform.smoothscale(mole_img2, mole_size)
mole_img = mole_img1

mole_crop = 0
mole_move = 10
mole_stage = 0
mole_stay_time = 200
click_go = False

exit_state = False

# 메인 이벤트
while not exit_state:
    clock.tick(60)
    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_state = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            click_go = True

    now_time = pygame.time.get_ticks()
    if mole_stage == 0:
        if random.random() < 0.1:
            mole_stage = 1
    elif mole_stage == 1:
        mole_crop += mole_move
        if mole_crop >= mole_size[1]:
            mole_crop = mole_size[1]
            mole_stage = 2
            mole_stay_start = now_time
    elif mole_stage == 2:
        if now_time - mole_stay_start > mole_stay_time:
            mole_stage = 3
    elif mole_stage == 3:
        mole_crop -= mole_move
        if mole_crop <= 0:
            mole_crop = 0
            mole_stage = 0
            mole_img = mole_img1

    mole_img_cropped = mole_img.subsurface((0, 0, mole_size[0], mole_crop))
    mole_pos = tup_r((x_list[0] - mole_size[0] / 2, y_list[0] - mole_crop))
    mole_range = (mole_pos[0], mole_pos[1], mole_size[0], mole_crop)
    if click_go == True:
        x, y = pygame.mouse.get_pos()
        x1, y1, w, h = mole_range
        if x >= x1 and x <= x1 + w and y >= y1 and y <= y1+h:
            # 이미지가 내려가야됨(stage = 3), 이미지 바꾸기(맞은 이미지)
            mole_stage = 3
            mole_img = mole_img2
        click_go = False
    # 그리기
    screen.blit(bg_img, (0, 0))
    screen.blit(mole_img_cropped, mole_pos)
    pygame.display.flip()

pygame.quit()
