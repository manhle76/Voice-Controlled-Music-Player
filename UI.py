<<<<<<< HEAD
<<<<<<< HEAD
import pygame

# Colors
GREEN = (0, 250, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
ORANGE = (255, 165, 0)


class Button:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def is_mouse_in(self):
        mx, my = pygame.mouse.get_pos()
        return (self.x < mx < self.x + self.width and
                self.y < my < self.y + self.height)

    def draw_box(self, screen):
        font = pygame.font.SysFont(None, 25)
        text_render = font.render(self.name, True, BLACK)
        border = pygame.draw.rect(
            screen, ORANGE, (self.x, self.y, self.width, self.height), 1)
        text_rect = text_render.get_rect(center=border.center)

        if self.is_mouse_in():
            pygame.draw.line(screen, RED,
                             (text_rect.left, text_rect.bottom + 1),
                             (text_rect.right, text_rect.bottom + 1), 1)
            pygame.draw.rect(screen, (255, 204, 152),
                             (self.x, self.y, self.width, self.height))

        screen.blit(text_render, text_rect)

    def draw_plus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)
        pygame.draw.line(screen, BLACK, (cx, cy - size), (cx, cy + size), 1)

    def draw_minus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)


def draw_volume_symbol(screen, x, y, radius, name):
    border = pygame.draw.circle(screen, RED, (x, y), radius, 1)
    font = pygame.font.SysFont(None, 45)
    text = font.render(f"{name:.0f}", True, BLACK)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_time(screen, x, y, w, h, time):
    font = pygame.font.SysFont(None, 25)
    text = font.render(time, True, BLACK)
    border = pygame.draw.rect(screen, RED, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_seek_bar(screen, x, y, w, h, process):
    border = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, BLACK, border, 1)
    process_rect = pygame.Rect(x + 1, y + 1, process, h - 2)
    pygame.draw.rect(screen, GREEN, process_rect)


def draw_name_song(screen, x, y, w, h, name):
    max_size = 25
    font_size = max_size

    while font_size > 10:
        font = pygame.font.SysFont("cambria", font_size)
        text = font.render(name, True, BLACK)
        if text.get_rect().width <= w - 10:
            break
        font_size -= 1

    border = pygame.draw.rect(screen, WHITE, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)
=======
import pygame

# Colors
GREEN = (0, 250, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
ORANGE = (255, 165, 0)


class Button:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def is_mouse_in(self):
        mx, my = pygame.mouse.get_pos()
        return (self.x < mx < self.x + self.width and
                self.y < my < self.y + self.height)

    def draw_box(self, screen):
        font = pygame.font.SysFont(None, 25)
        text_render = font.render(self.name, True, BLACK)
        border = pygame.draw.rect(
            screen, ORANGE, (self.x, self.y, self.width, self.height), 1)
        text_rect = text_render.get_rect(center=border.center)

        if self.is_mouse_in():
            pygame.draw.line(screen, RED,
                             (text_rect.left, text_rect.bottom + 1),
                             (text_rect.right, text_rect.bottom + 1), 1)
            pygame.draw.rect(screen, (255, 204, 152),
                             (self.x, self.y, self.width, self.height))

        screen.blit(text_render, text_rect)

    def draw_plus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)
        pygame.draw.line(screen, BLACK, (cx, cy - size), (cx, cy + size), 1)

    def draw_minus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)


def draw_volume_symbol(screen, x, y, radius, name):
    border = pygame.draw.circle(screen, RED, (x, y), radius, 1)
    font = pygame.font.SysFont(None, 45)
    text = font.render(f"{name:.0f}", True, BLACK)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_time(screen, x, y, w, h, time):
    font = pygame.font.SysFont(None, 25)
    text = font.render(time, True, BLACK)
    border = pygame.draw.rect(screen, RED, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_seek_bar(screen, x, y, w, h, process):
    border = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, BLACK, border, 1)
    process_rect = pygame.Rect(x + 1, y + 1, process, h - 2)
    pygame.draw.rect(screen, GREEN, process_rect)


def draw_name_song(screen, x, y, w, h, name):
    max_size = 25
    font_size = max_size

    while font_size > 10:
        font = pygame.font.SysFont("cambria", font_size)
        text = font.render(name, True, BLACK)
        if text.get_rect().width <= w - 10:
            break
        font_size -= 1

    border = pygame.draw.rect(screen, WHITE, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
=======
import pygame

# Colors
GREEN = (0, 250, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)
ORANGE = (255, 165, 0)


class Button:
    def __init__(self, x, y, width, height, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name

    def is_mouse_in(self):
        mx, my = pygame.mouse.get_pos()
        return (self.x < mx < self.x + self.width and
                self.y < my < self.y + self.height)

    def draw_box(self, screen):
        font = pygame.font.SysFont(None, 25)
        text_render = font.render(self.name, True, BLACK)
        border = pygame.draw.rect(
            screen, ORANGE, (self.x, self.y, self.width, self.height), 1)
        text_rect = text_render.get_rect(center=border.center)

        if self.is_mouse_in():
            pygame.draw.line(screen, RED,
                             (text_rect.left, text_rect.bottom + 1),
                             (text_rect.right, text_rect.bottom + 1), 1)
            pygame.draw.rect(screen, (255, 204, 152),
                             (self.x, self.y, self.width, self.height))

        screen.blit(text_render, text_rect)

    def draw_plus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)
        pygame.draw.line(screen, BLACK, (cx, cy - size), (cx, cy + size), 1)

    def draw_minus_button(self, screen, size):
        cx = self.x + self.width / 2
        cy = self.y + self.height / 2
        pygame.draw.line(screen, BLACK, (cx - size, cy), (cx + size, cy), 1)


def draw_volume_symbol(screen, x, y, radius, name):
    border = pygame.draw.circle(screen, RED, (x, y), radius, 1)
    font = pygame.font.SysFont(None, 45)
    text = font.render(f"{name:.0f}", True, BLACK)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_time(screen, x, y, w, h, time):
    font = pygame.font.SysFont(None, 25)
    text = font.render(time, True, BLACK)
    border = pygame.draw.rect(screen, RED, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)


def draw_seek_bar(screen, x, y, w, h, process):
    border = pygame.Rect(x, y, w, h)
    pygame.draw.rect(screen, BLACK, border, 1)
    process_rect = pygame.Rect(x + 1, y + 1, process, h - 2)
    pygame.draw.rect(screen, GREEN, process_rect)


def draw_name_song(screen, x, y, w, h, name):
    max_size = 25
    font_size = max_size

    while font_size > 10:
        font = pygame.font.SysFont("cambria", font_size)
        text = font.render(name, True, BLACK)
        if text.get_rect().width <= w - 10:
            break
        font_size -= 1

    border = pygame.draw.rect(screen, WHITE, (x, y, w, h), 1)
    text_rect = text.get_rect(center=border.center)
    screen.blit(text, text_rect)
>>>>>>> 57c02483a769b2b1c793f10614ac540529af5839
