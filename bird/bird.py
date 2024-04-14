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


def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)


def img_read(file_name, resize):
    img = pygame.image.load(file_name + ".png")
    img_size = img.get_size()
    img_size = (img_size[0] * resize, img_size[1] * resize)
    img = pygame.transform.smoothscale(img, img_size)
    return img


person_static = img_read("man_static", 1)
person_size = person_static.get_size()

p_left_list = [img_read("man_left1", 1), img_read("man_left2", 1), img_read("man_left3", 1)]
p_right_list = [img_read("man_right1", 1), img_read("man_right2", 1), img_read("man_right3", 1)]

class person:
    def __init__(self):
        self.img = person_static
        self.size = self.img.get_size()
        self.pos = (size[0] / 2 - self.size[0] / 2, size[1] - self.size[1])
        self.move = 10

    def show(self):
        screen.blit(self.img, self.pos)


player = person()
k = 0
left_go = False
right_go = False

exit_state = False
game_point = 0
game_time = 10000
game_over = False

point_font = pygame.font.Font("/System/Library/Fonts/Supplemental/PartyLET-plain.ttf", 60)
final_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Courier New.ttf", 80)

# 메인 이벤트
game_start_tme = pygame.time.get_ticks()
while not exit_state:
    clock.tick(60)
    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_state = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if key_name == "left":
                left_go = True
            elif key_name == "right":
                right_go = True
        if event.type == pygame.KEYUP:
            key_name = pygame.key.name(event.key)
            if key_name == "left":
                left_go = False
            elif key_name == "right":
                right_go = False


    k += 0.2
    now_time = pygame.time.get_ticks()
    remain_time = round((game_time - (now_time - game_start_tme)) / 1000)

    kk = int(k) % 3


    if left_go == True and right_go == False:
        player.pos = (player.pos[0] - player.move, player.pos[1])
        if player.pos[0] <= 0: player.pos = (0, player.pos[1])
        player.img = p_left_list[kk]
    elif left_go == False and right_go == True:
        player.pos = (player.pos[0] + player.move, player.pos[1])
        if player.pos[0] >= size[0]-player.size[0]: player.pos = (size[0]-player.size[0], player.pos[1])
        player.img = p_right_list[kk]


    if remain_time <= 0:
        remain_time = 0
        game_over = True

    # 그리기
    screen.fill(white)
    player.show()

    # 점수표시
    point = point_font.render(f"Score : {game_point}", True, black)
    point_size = point.get_size()
    point_pos = tup_r((10, 10))
    screen.blit(point, point_pos)

    # 남은 시간
    remain_time = point_font.render(f"Time : {remain_time}", True, black)
    remain_time_size = remain_time.get_size()
    remain_time_pos = tup_r((size[0] - remain_time_size[0] - 10, 10))
    screen.blit(remain_time, remain_time_pos)

    if game_over == True:
        finish_bg = pygame.Surface(size)
        finish_bg.fill(black)
        finish_bg.set_alpha(200)
        screen.blit(finish_bg, (0, 0))
        final_point = final_font.render(f"Final Score : {game_point}", True, white)
        final_point_size = final_point.get_size()
        final_point_pos = tup_r((size[0] / 2 - final_point_size[0] / 2, size[1] / 2 - final_point_size[1] / 2))
        screen.blit(final_point, final_point_pos)

    pygame.display.flip()

pygame.quit()
