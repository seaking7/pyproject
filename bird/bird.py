import random

import math
import pygame

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

bird_list = [img_read("bird1", 0.5), img_read("bird2", 0.5), img_read("bird3", 0.5),
             img_read("bird4", 0.5), img_read("bird5", 0.5), img_read("bird6", 0.5)]

dung_img = img_read("dung", 1)

class Bird:
    def __init__(self):
        self.img = bird_list[0]
        self.size = self.img.get_size()
        self.create_x = -self.size[0]
        self.create_y = random.randrange(50, 400)
        self.target_x = size[0]
        self.target_y = random.randrange(50, 400)
        if random.random() > 0.5:
            self.create_x, self.target_x = self.target_x, self.create_x
        self.dx = self.target_x - self.create_x
        self.dy = self.target_y - self.create_y
        self.dd = (self.dx ** 2 + self.dy ** 2) ** 0.5  # 빗변(피타고라스 정리)
        self.pos = (self.create_x, self.create_y)
        self.move = random.randrange(3, 10)
        self.x_speed = self.move * self.dx / self.dd
        self.y_speed = self.move * self.dy / self.dd
        self.timer = 0
        self.any_move = 0.1

        self.angle = math.atan(abs(self.dy/self.dx)) * 180 / math.pi  # 새의 날아 가는 각도 계산

        self.drop_x = random.randrange(100, size[0] - 100 - self.size[0])
        self.drop = False

    def show(self):
        if self.x_speed < 0:
            self.img = pygame.transform.flip(self.img, True, False)

        if self.dx * self.dy < 0:
            self.img = pygame.transform.rotate(self.img, self.angle)
        else:
            self.img = pygame.transform.rotate(self.img, -self.angle)

        screen.blit(self.img, self.pos)


class Person:
    def __init__(self):
        self.img = person_static
        self.size = self.img.get_size()
        self.pos = (size[0] / 2 - self.size[0] / 2, size[1] - self.size[1])
        self.move = 10
        self.timer = 0
        self.any_move = 0.2

    def show(self):
        screen.blit(self.img, self.pos)


class Dung:
    def __init__(self, x, y, x_speed):
        self.img = dung_img
        self.pos = x, y
        self.x_speed = x_speed
        self.y_speed = 3
        self.acceleration = 0.1
        self.size = self.img.get_size()

    def show(self):
        screen.blit(self.img, self.pos)


player = Person()
bird = Bird()
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
            player.timer = 0
            if key_name == "left":
                left_go = False
            elif key_name == "right":
                right_go = False

    now_time = pygame.time.get_ticks()
    remain_time = round((game_time - (now_time - game_start_tme)) / 1000)

    if left_go is True and right_go is False:
        player.pos = (player.pos[0] - player.move, player.pos[1])
        player.timer += player.any_move
        if player.pos[0] <= 0:
            player.pos = (0, player.pos[1])
        player.img = p_left_list[int(player.timer) % len(p_left_list)]
    elif left_go is False and right_go is True:
        player.pos = (player.pos[0] + player.move, player.pos[1])
        player.timer += player.any_move
        if player.pos[0] >= size[0] - player.size[0]:
            player.pos = (size[0] - player.size[0], player.pos[1])
        player.img = p_right_list[int(player.timer) % len(p_right_list)]
    else:
        player.img = person_static

    if remain_time <= 0:
        remain_time = 0
        game_over = True

    bird.timer += bird.any_move
    bird.img = bird_list[int(bird.timer) % len(bird_list)]
    bird.pos = (bird.pos[0] + bird.x_speed, bird.pos[1] + bird.y_speed)

    if bird.x_speed  > 0:    # 왼쪽에서 오른쪽
        if bird.pos[0] >= bird.drop_x and bird.drop == False:
            dung = Dung(bird.pos[0] + bird.size[0] / 2, bird.pos[1] + bird.size[1], bird.x_speed)
            bird.drop = True
    else:
        if bird.pos[0] <= bird.drop_x and bird.drop == False:
            dung = Dung(bird.pos[0] + bird.size[0] / 2, bird.pos[1] + bird.size[1], bird.x_speed)
            bird.drop = True



    # 그리기
    screen.fill(white)
    player.show()
    bird.show()

    if bird.drop:
        dung.y_speed += dung.acceleration
        dung.pos = dung.pos[0] + dung.x_speed, dung.pos[1] + dung.y_speed
        dung.show()

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

    if game_over:
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