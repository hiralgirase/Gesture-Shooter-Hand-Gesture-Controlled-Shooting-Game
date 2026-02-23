import pygame
import time
import random

from explosion import Explosion
from player import Player
from bullet import Bullet
from enemy import Enemy
from enemy_bullet import EnemyBullet
from gesture_detector import GestureDetector

pygame.init()
pygame.mixer.init()

# ================= SOUND =================
shoot_sound = pygame.mixer.Sound("assets/shoot.mp3")
explosion_sound = pygame.mixer.Sound("assets/explosion.mp3")

pygame.mixer.music.load("assets/background.mp3")
pygame.mixer.music.play(-1)

# ================= SETTINGS =================
WIDTH, HEIGHT = 800, 600
FPS = 30
COOLDOWN = 0.4

# ================= WINDOW =================
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gesture Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# ================= BACKGROUND =================
background = pygame.image.load("assets/background.png").convert()
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# ================= OBJECTS =================
detector = GestureDetector()
player = Player(WIDTH, HEIGHT)

bullets = []
enemy_bullets = []
enemies = [Enemy(WIDTH)]
explosions = []

score = 0
last_shot = 0
running = True
game_over = False

# ================= GAME LOOP =================
while running:
    clock.tick(FPS)
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    gesture, hand_x = detector.get_gesture()

    # Move player with hand
    if hand_x is not None and not game_over:
        target_x = int(hand_x * WIDTH) - 30
        player.x += (target_x - player.x) * 0.2

    # Shoot with fist
    if gesture == "FIST" and not game_over:
        if time.time() - last_shot > COOLDOWN:
            bullets.append(Bullet(player.x + 20, player.y))
            shoot_sound.play()
            last_shot = time.time()

    keys = pygame.key.get_pressed()

    if not game_over:

        player.draw(screen)

        # ================= PLAYER BULLETS =================
        for bullet in bullets[:]:
            bullet.update()
            bullet.draw(screen)

            if bullet.y < 0:
                bullets.remove(bullet)

        # ================= ENEMIES =================
        for enemy in enemies[:]:
            enemy.update()
            enemy.draw(screen)

            # Enemy shooting
            if random.random() < 0.01:
                enemy_bullets.append(
                    EnemyBullet(enemy.x + 20, enemy.y + 40)
                )

            player_rect = pygame.Rect(player.x, player.y, 60, 60)
            enemy_rect = pygame.Rect(enemy.x, enemy.y, 60, 60)

            # Player collision
            if player_rect.colliderect(enemy_rect):
                player.health -= 1

            # Enemy off screen
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
                enemies.append(Enemy(WIDTH))

            # Bullet collision
            for bullet in bullets[:]:
                bullet_rect = pygame.Rect(bullet.x, bullet.y, 20, 40)

                if bullet_rect.colliderect(enemy_rect):
                    bullets.remove(bullet)
                    enemies.remove(enemy)

                    explosions.append(
                        Explosion(enemy.x + 30, enemy.y + 30)
                    )
                    explosion_sound.play()

                    enemies.append(Enemy(WIDTH))
                    score += 1
                    break

        # ================= ENEMY BULLETS =================
        for ebullet in enemy_bullets[:]:
            ebullet.update()
            ebullet.draw(screen)

            ebullet_rect = pygame.Rect(
                ebullet.x, ebullet.y, 10, 20
            )

            player_rect = pygame.Rect(player.x, player.y, 60, 60)

            if ebullet_rect.colliderect(player_rect):
                player.health -= 1
                enemy_bullets.remove(ebullet)

            if ebullet.y > HEIGHT:
                enemy_bullets.remove(ebullet)

        # ================= EXPLOSIONS =================
        for explosion in explosions[:]:
            explosion.update()
            explosion.draw(screen)

            if explosion.finished:
                explosions.remove(explosion)

        # ================= DIFFICULTY =================
        if score > 0 and score % 10 == 0:
            enemies.append(Enemy(WIDTH))

        # ================= UI =================
        score_text = font.render(
            f"Score: {score}", True, (255, 255, 255)
        )
        screen.blit(score_text, (10, 10))

        pygame.draw.rect(
            screen,
            (255, 0, 0),
            (10, 50, max(player.health, 0) * 2, 20)
        )

        if player.health <= 0:
            game_over = True

    else:
        game_over_text = font.render(
            "GAME OVER", True, (255, 0, 0)
        )
        restart_text = font.render(
            "Press R to Restart", True, (255, 255, 255)
        )

        screen.blit(game_over_text,
                    (WIDTH // 2 - 100, HEIGHT // 2 - 30))
        screen.blit(restart_text,
                    (WIDTH // 2 - 120, HEIGHT // 2 + 10))

        if keys[pygame.K_r]:
            player = Player(WIDTH, HEIGHT)
            bullets = []
            enemy_bullets = []
            enemies = [Enemy(WIDTH)]
            explosions = []
            score = 0
            game_over = False

    pygame.display.update()

pygame.quit()
detector.release()