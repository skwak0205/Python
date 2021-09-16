import pygame
from random import *


#  시작 화면 보여주기
def display_start_screen():
    pygame.draw.circle(screen, WHITE, start_button.center, 60, 5)


# pos에 해당하는 버튼 확인
def check_buttons(pos):
    global start

    if start:  # 게임이 시작했을 경우
        check_number_buttons(pos)
    elif start_button.collidepoint(pos):
        start = True


def check_number_buttons(pos):
    global hidden

    for button in number_buttons:
        if button.collidepoint(pos):
            if button == number_buttons[0]:  # 올바른 숫자 click
                del number_buttons[0]
                if not hidden:
                    hidden = True  # 숫자 숨김 처리
            else:  # 잘못된 숫자 click
                print("Wrong")
            break


# 게임 화면 보여주기
def display_game_screen():
    for idx, rect in enumerate(number_buttons, start=1):
        if hidden:
            # 버튼 사각형 그리기
            pygame.draw.rect(screen, WHITE, rect)
        else:
            # 실제 숫자 텍스트
            cell_text = game_font.render(str(idx), True, WHITE)
            text_rect = cell_text.get_rect(center=rect.center)
            screen.blit(cell_text, text_rect)


# 레벨에 맞게 설정
def setup(level):
    # 얼마나 많은 숫자를 보여줄 것인가
    number_count = (level // 3) + 5
    number_count = min(number_count, 20)  # 최대 숫자 20

    # 실제 화면에 grid 형태로 숫자를 랜덤으로 배치
    shuffle_grid(number_count)


# 숫자 섞기
def shuffle_grid(number_count):
    rows = 5
    columns = 9

    cell_size = 130  # 각 Grid cell 별 가로, 세로 크기

    button_size = 110  # Grid cell 내에 실제로 그려질 버튼 크기
    screen_left_margin = 50  # 전체 스크린 왼쪽 여백
    screen_top_margin = 20  # 전체 스크린 위쪽 여백

    grid = [[0 for col in range(columns)] for row in range(rows)]

    number = 1
    while number <= number_count:
        row_idx = randrange(0, rows)  # 0이상 5 미만
        col_idx = randrange(0, columns)  # 0이상 9 미만

        if grid[row_idx][col_idx] == 0:
            grid[row_idx][col_idx] = number
            number += 1

            # 현재 grid cell 위치 기준으로 x, y 위치를 구함
            center_x = screen_left_margin + (col_idx * cell_size) + (cell_size / 2)
            center_y = screen_top_margin + (row_idx * cell_size) + (cell_size / 2)

            # 숫자 버튼 만들기
            button = pygame.Rect(0, 0, button_size, button_size)
            button.center = (center_x, center_y)

            number_buttons.append(button)


# 초기화
pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Memory Game")
game_font = pygame.font.Font(None, 120)  # 폰트 정의

# 시작 버튼
start_button = pygame.Rect(0, 0, 120, 120)
start_button.center = (120, screen_height - 120)

# 색
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)

number_buttons = []  # 플레이어가 눌러야 하는 버튼들

# 게임 시작 여부
start = False

# 숫자 숨김 여부
hidden = False

# 게임 시작 전에 게임 설정 함수 수행
setup(1)

# 게임 루프
running = True

while running:
    click_pos = None

    # 이벤트 루프
    for event in pygame.event.get():  # 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT:  # 창이 닫히는 이벤트인가
            running = False  # 게임 더 이상 실행 중 아님

        elif event.type == pygame.MOUSEBUTTONUP:
            click_pos = pygame.mouse.get_pos()

    # 화면 전체를 까맣게 칠함
    screen.fill(BLACK)

    if start:
        display_game_screen()
    else:
        # 시작 화면 표시
        display_start_screen()

    # 사용자가 클릭한 좌표값이 있을 경우
    if click_pos:
        check_buttons(click_pos)

    # 화면 업데이트
    pygame.display.update()

# 게임 종료
pygame.quite()
