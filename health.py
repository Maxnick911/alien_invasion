import pygame

class Health:
    def __init__(self, ai_game):
        """Ініціалізація параметрів здоров'я."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Завантаження зображення сердечка та отримання його прямокутника
        self.image = pygame.image.load('images\\heart.png')
        self.rect = self.image.get_rect()

        # Встановлення позиції для першого сердечка у лівому верхньому куті
        self.rect.x = 20
        self.rect.y = 20

    def show_health(self):
        """Відображення кількості життів на екрані."""
        for heart_number in range(self.stats.ships_left):
            # Для кожного життя, зміщуємо сердечко вправо
            offset_x = heart_number * (self.rect.width + 10)
            self.screen.blit(self.image, (self.rect.x + offset_x, self.rect.y))
