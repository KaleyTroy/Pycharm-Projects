import pygame
import sys
from random import *
import math
from styles import style
from icecream import ic

pygame.init()
width, height = 600, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Altar of Prayer")
clock = pygame.time.Clock()


def kill_check(event_check):
    if event_check.type == pygame.QUIT:
        pygame.quit()
        sys.exit()


def render_prayer():
    prayer = prayer_request()
    clean_prayer = (''.join(char for char in prayer if char.isalnum()) + ".png").lower()
    seed(clean_prayer)
    screen.fill('white')
    prayer_wheel(prayer)
    display_words(prayer.split())
    pygame.image.save(screen, clean_prayer)


def prayer_request():
    font = pygame.font.SysFont("lucida handwriting", 28)
    input_txt = ""
    input_active = True

    while input_active:
        for event in pygame.event.get():
            kill_check(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    input_txt = input_txt[:-1]
                else:
                    input_txt += event.unicode

        screen.fill("white")
        blessing_surface = font.render("Blessings", True, "purple")
        prayer_surface = font.render("What would you like to pray for?", True, "purple")
        input_surface = font.render(input_txt, True, "magenta")

        blessing_rect = blessing_surface.get_rect(center=(width // 2, height // 4 - 20))
        prayer_rect = prayer_surface.get_rect(center=(width // 2, height // 4 + 20))
        input_rect = input_surface.get_rect(center=(width // 2, height // 2))

        screen.blit(blessing_surface, blessing_rect)
        screen.blit(prayer_surface, prayer_rect)
        screen.blit(input_surface, input_rect)
        pygame.display.flip()

    return input_txt


def prayer_wheel(o_prayer):
    def kill_check_2():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def r_circle(r_radius_1, r_radius_2, r_position, r_rotation):
        r_angle = 0
        r_rgb = [[randint(50, 200), randint(-20, 20)] for _ in range(3)]
        for _ in range(r_rotation):
            for x, y in enumerate(r_rgb):
                r_rgb[x][0] += r_rgb[x][1]
                if not 50 < y[0] < 200: r_rgb[x][1] *= -1
            r_colour = [r_rgb[_][0] for _ in range(3)]
            r_angle += math.tau / r_rotation
            r_position_2 = [int(r_position[0] + r_radius_1 * math.cos(r_angle)),
                            int(r_position[1] + r_radius_1 * math.sin(r_angle))]

            c_circle(r_radius_2, r_position_2, r_colour)

    def c_circle(c_radius, c_position, c_colour):
        c_angle = 0
        while True:
            kill_check_2()
            c_angle += 0.01
            if c_angle > math.tau: break

            c_position_2 = [int(c_position[0] + c_radius * math.cos(c_angle)),
                            int(c_position[1] + c_radius * math.sin(c_angle))]

            test = math.sqrt((c_position_2[0] - 300) ** 2 + (c_position_2[1] - 300) ** 2) < 252

            if test:
                pygame.draw.circle(screen, c_colour, (c_position_2[0], c_position_2[1]), 3)

            pygame.display.flip()

    # === === Variables === ===
    for _ in ("control","small_control"):
        val = style[_]
        o_radius_0 = val["radius_0"]
        o_rotation_0 = val["rotation_0"]
        o_radius_1 = val["radius_1"]
        o_rotation_1 = val["rotation_1"]
        o_hole_size = val["hole_size"]
        o_growth = val["growth"]
        o_position_0 = (300 + val["hori_drift"], 300 + val["vert_drift"])
        o_hole_size -= o_growth

        # === === Variables === ===
        for _ in range(o_rotation_0):
            o_hole_size += o_growth
            if o_hole_size > 250: o_hole_size *= -1
            o_radius_2 = o_radius_1 + o_hole_size

            angle = math.tau * ((_ - 3) % o_rotation_0) / o_rotation_0
            o_position = [o_position_0[0] + o_radius_0 * math.cos(angle),
                          o_position_0[1] + o_radius_0 * math.sin(angle)]
            r_circle(o_radius_1, o_radius_2, o_position, o_rotation_1)

    # Closing circle
    kill_check_2()
    angle = 0
    rgb = [[randint(10, 10), randint(0, 5)] for _ in range(3)]
    while angle < math.tau:
        for x, y in enumerate(rgb):
            rgb[x][0] += rgb[x][1]
            if not 5 < y[0] < 250: rgb[x][1] *= -1
        f_colour = [rgb[_][0] for _ in range(3)]
        angle += 0.005
        if angle > 2 * math.pi: break
        f_position = [int(300 + 250 * math.cos(angle)),
                      int(300 + 250 * math.sin(angle))]
        pygame.draw.circle(screen, f_colour, f_position, 6)
        pygame.display.flip()


def display_words(words):
    font = pygame.font.SysFont("lucida handwriting", 60)
    total_height = sum([font.get_height() for _ in words])
    current_y = 750 - (total_height // 2)

    for word in words:
        total_width = sum([font.render(char, True, (0, 0, 0)).get_width() for char in word])

        current_x = (width - total_width) // 2

        for char in word:
            char_color = [randint(50, 255) for _ in range(3)]
            char_surface = font.render(char, True, char_color)

            char_rect = char_surface.get_rect(center=(current_x + char_surface.get_width() // 2, current_y))
            screen.blit(char_surface, char_rect)
            current_x += char_surface.get_width()  # Move to the next character

        current_y += font.get_height()  # Move to the next line

    pygame.display.flip()


render_prayer()
while True:
    for event in pygame.event.get():
        kill_check(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                render_prayer()
