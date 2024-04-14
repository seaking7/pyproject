import pygame, math, random

pygame.init()

def tup_r(tup):
    temp_list = []
    for a in tup:
        temp_list.append(round(a))
    return tuple(temp_list)


size = [500, 900]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("HANGMAN")

clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
hint_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Courier New.ttf", 80)
entry_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 60)
small_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Arial.ttf", 20)
title_font = pygame.font.Font("/System/Library/Fonts/Supplemental/Trattatello.ttf", 80)

sound1 = pygame.mixer.Sound("applause.ogg")
sound2 = pygame.mixer.Sound("applause10.ogg")
try_num = 0
exit = False
ready = False
game_over = False
save = False

f = open("voca.txt", "r")
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
while True:
    r_index = random.randrange(0, len(data_list))
    word = data_list[r_index]
    if len(word) <= 6: break
word = word.upper()
print(word)
word_show = "_" * len(word)

ok_list = []
no_list = []


k = 0
drop = False
enter_go = False
entry_text = ""


def draw_hint():
    hint = hint_font.render(word_show, True, white)
    hint_size = hint.get_size()
    hint_pos = tup_r((size[0] / 2 - hint_size[0] / 2, size[1] * 5 / 6 - hint_size[1] / 2))
    screen.blit(hint, hint_pos)


def draw_entry_text():
    # 입력창 표시
    entry = entry_font.render(entry_text, True, black)
    entry_size = entry.get_size()
    entry_pos = (size[0] / 2 - entry_size[0] / 2, size[1] * 17 / 18 - entry_size[1] / 2)
    entry_bg_size = 80
    pygame.draw.rect(screen, white, (
        size[0] / 2 - entry_bg_size / 2, size[1] * 17 / 18 - entry_bg_size / 2, entry_bg_size, entry_bg_size))
    screen.blit(entry, entry_pos)


def no_font_text():
    no_text = small_font.render(" ".join(no_list), True, red)
    no_text_pos = tup_r((20, size[1] * 2 / 3 + 20))
    screen.blit(no_text, no_text_pos)


def draw_outer_line():
    global E
    A = tup_r((0, size[1] * 2 / 3))
    B = tup_r((size[0], A[1]))
    C = tup_r((size[0] / 6, A[1]))
    D = tup_r((C[0], C[0]))
    E = tup_r((size[0] / 2, D[1]))
    if save != True:
        pygame.draw.line(screen, white, A, B, 3)
        pygame.draw.line(screen, white, C, D, 3)
        pygame.draw.line(screen, white, D, E, 3)


def draw_human():
    if try_num >= 1 or save == True: pygame.draw.circle(screen, white, G, r_head, 3)
    H = (G[0], G[1] + r_head)
    I = (H[0], H[1] + r_head)
    if try_num >= 2 or save == True: pygame.draw.line(screen, white, H, I, 3)
    l_arm = r_head * 2
    J = (I[0] - l_arm * math.cos(30 * math.pi / 180), I[1] + l_arm * math.sin(30 * math.pi / 180))
    K = (I[0] + l_arm * math.cos(30 * math.pi / 180), I[1] + l_arm * math.sin(30 * math.pi / 180))
    J = tup_r(J)
    K = tup_r(K)
    if try_num >= 3 or save == True: pygame.draw.line(screen, white, I, J, 3)
    if try_num >= 4 or save == True: pygame.draw.line(screen, white, I, K, 3)
    L = (I[0], I[1] + l_arm)
    if try_num >= 5 or save == True: pygame.draw.line(screen, white, I, L, 3)
    l_leg = l_arm * 1.5
    M = tup_r((L[0] - l_leg * math.cos(60 * math.pi / 180), L[1] + l_leg * math.sin(60 * math.pi / 180)))
    N = tup_r((L[0] + l_leg * math.cos(60 * math.pi / 180), L[1] + l_leg * math.sin(60 * math.pi / 180)))
    if try_num >= 6 or save == True: pygame.draw.line(screen, white, L, M, 3)
    if try_num >= 7 or save == True: pygame.draw.line(screen, white, L, N, 3)


def draw_red_line():
    global drop, k
    O = tup_r((size[0] / 2 - size[0] / 6, E[1] / 2 + F[1] / 2))
    P = (O[0] + k * 2, O[1])
    if P[0] > size[0] / 2 + size[0] / 6:
        P = (size[0] / 2 + size[0] / 6, O[1])
        drop = True
        k = 0

    pygame.draw.line(screen, red, O, P, 3)


def draw_start_text():
    title_text = title_font.render("HANGMAN", True, white)
    title_text_size = title_text.get_size()
    title_text_pos = tup_r((size[0] / 2 - title_text_size[0] / 2, size[1] / 2 - title_text_size[1] / 2))
    screen.blit(title_text, title_text_pos)
    small_text = small_font.render("PRESS ANY KEY", True, white)
    small_text_size = small_text.get_size()
    small_text_pos = tup_r((size[0] / 2 - small_text_size[0] / 2, size[1] * 4 / 5 - small_text_size[1] / 2))
    if pygame.time.get_ticks() % 1000 > 700:
        screen.blit(small_text, small_text_pos)

sound1.set_volume(1)
sound1.play()
while not exit:
    clock.tick(60)  # FPS 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            ready = True
    if ready == True: break
    screen.fill(black)
    draw_start_text()
    pygame.display.flip() # 업데이트


def draw_finish_text():
    finish_bg = pygame.Surface(size)
    finish_bg.fill(black)
    finish_bg.set_alpha(200)
    screen.blit(finish_bg, (0, 0))
    if save == True:
        finish_text = "You Saved the man"
    else:
        finish_text = "You Killed the man"
    finish = entry_font.render(finish_text, True, white)
    finish_size = finish.get_size()
    finish_pos = (size[0] / 2 - finish_size[0] / 2, size[1] / 2 - finish_size[1] / 2)
    screen.blit(finish, finish_pos)
    small_text = small_font.render("PRESS ANY KEY To Play Again", True, white)
    small_text_size = small_text.get_size()
    small_text_pos = tup_r((size[0] / 2 - small_text_size[0] / 2, size[1] * 4 / 5 - small_text_size[1] / 2))
    screen.blit(small_text, small_text_pos)


# 메인 이벤트

while not exit:
    clock.tick(60)  # FPS 설정

    # 각종 입력 감지
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            if (key_name == "return" or key_name == "enter"):
                if entry_text != "" and (ok_list + no_list).count(entry_text) == 0:
                    enter_go = True
            elif (len(key_name) == 1):
                if (ord(key_name) >= 65 and ord(key_name) <= 90) or (ord(key_name) >= 97 and ord(key_name) <= 122):
                    entry_text = key_name.upper()
                else:
                    entry_text = ""
            else:
                entry_text = ""

    if try_num == 8: k += 1
    if enter_go == True:
        result = word.find(entry_text)

        if result == -1:
            try_num += 1
            no_list.append(entry_text)
        else:
            ok_list.append(entry_text)
            for i in range(len(word)):
                if word[i] == entry_text:
                    word_show = word_show[:i] + entry_text + word_show[i + 1:]
        # if word_show.find("_") == -1: break
        enter_go = False
        entry_text = ""

    if drop == True:
        game_over = True
        word_show = word

    if word_show.find("_") == -1 and game_over == False:
        game_over = True
        save = True
        sound2.play()
    screen.fill(black)
    draw_outer_line()

    F = (E[0], E[1] * 2)
    if drop == False:
        pygame.draw.line(screen, white, E, F, 3)
    r_head = round(size[0] / 12)
    if drop == True:
        G = (F[0], F[1] + r_head + k * 5)
    else:
        G = (F[0], F[1] + r_head)
    draw_human()

    if drop == False and try_num >= 8:
        draw_red_line()


    draw_hint()
    draw_entry_text()
    no_font_text()

    # 종료화면
    if game_over == True:
        draw_finish_text()
    pygame.display.flip() # 업데이트

pygame.quit()
