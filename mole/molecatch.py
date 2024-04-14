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




class mole:
    def __init__(self, i, j):
        self.i = i
        self.j = j
        self.img = mole_img1
        self.crop = 0
        self.move = 10
        self.stage = 0
        self.stay_time = 200
        self.clicked = False
        self.size = mole_size

    def crop_change(self):
        if self.stage == 0:
            if random.random() < 0.1:
                self.stage = 1
        elif self.stage == 1:
            self.crop += self.move
            if self.crop >= self.size[1]:
                self.crop =  self.size[1]
                self.stage = 2
                self.stay_start = now_time
        elif self.stage == 2:
            if now_time - self.stay_start > self.stay_time:
                self.stage = 3
        elif self.stage == 3:
            self.crop -= self.move
            if self.crop <= 0:
                self.crop = 0
                self.stage = 0
                self.img = mole_img1
                self.clicked = False

        self.img_cropped = self.img.subsurface((0, 0, self.size[0], self.crop))
        self.pos = tup_r((x_list[self.i] - self.size[0] / 2, y_list[self.j] - self.crop))
        self.range = (self.pos[0], self.pos[1], self.size[0], self.crop)


    def show(self):
        screen.blit(self.img_cropped, self.pos)

mole_list = []
for i in range(3):
    for j in range(3):
        mole_list.append(mole(i, j))
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
    for mole in mole_list:
        mole.crop_change()

    if click_go == True:
        for mole in mole_list:
            if mole.clicked == False:
                x, y = pygame.mouse.get_pos()
                x1, y1, w, h = mole.range
                if x1 <= x <= x1 + w and y1 <= y <= y1 + h:
                    mole.clicked = True
                    # 이미지가 내려가야됨(stage = 3), 이미지 바꾸기(맞은 이미지)
                    mole.stage = 3
                    mole.img = mole_img2
        click_go = False



    # 그리기
    screen.blit(bg_img, (0, 0))
    for mole in mole_list:
        mole.show()
    pygame.display.flip()

pygame.quit()
