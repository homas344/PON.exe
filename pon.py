# ██████╗░░█████╗░███╗░░██╗░░░███████╗██╗░░██╗███████╗
# ██╔══██╗██╔══██╗████╗░██║░░░██╔════╝╚██╗██╔╝██╔════╝
# ██████╔╝██║░░██║██╔██╗██║░░░█████╗░░░╚███╔╝░█████╗░░
# ██╔═══╝░██║░░██║██║╚████║░░░██╔══╝░░░██╔██╗░██╔══╝░░
# ██║░░░░░╚█████╔╝██║░╚███║██╗███████╗██╔╝╚██╗███████╗
# ╚═╝░░░░░░╚════╝░╚═╝░░╚══╝╚═╝╚══════╝╚═╝░░╚═╝╚══════╝
#
# PON.exe - v1.2 BETA
# Підключення модулів
import subprocess
import pygame
import random
import sys
import cv2
import time
import threading

# Закриття процесу explorer.exe (щоб життя малиною не втикало)
subprocess.call('taskkill /F /IM explorer.exe', shell=True)

# Ініціалізація pygame
pygame.init()

# Встановлення розмірів екрана
screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

# Завантаження зображень
image1 = pygame.image.load("pon1.jpg")
image2 = pygame.image.load("pon2.jpg")
image3 = pygame.image.load("pon3.jpg")
image4 = pygame.image.load("pon4.jpg")
image5 = pygame.image.load("pon5.jpg")

# Масштабування зображень до розмірів екрану
image1 = pygame.transform.scale(image1, (screen_width, screen_height))
image2 = pygame.transform.scale(image2, (screen_width, screen_height))
image3 = pygame.transform.scale(image3, (screen_width, screen_height))
image4 = pygame.transform.scale(image4, (screen_width, screen_height))
image5 = pygame.transform.scale(image5, (screen_width, screen_height))

# Приховання курсора миші та "захоплення" миші
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

# Зображення 1
pygame.mixer.music.load("pon.wav")
screen.blit(image1, (0, 0))
pygame.display.flip()
pygame.mixer.music.play()
pygame.time.delay(3000)

# Глюки системи
for i in range(100):
    # Перевірка на закриття вікна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Зміна кольорової гами
    screen.fill((random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    pygame.display.flip()
    pygame.time.delay(100)

# Обробка подій миші
pygame.event.get()

# Зображення два
for i in range(100):
    # Перевірка на закриття вікна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Плавне перетікання всього екрану в різні частини екрану
    x = random.randint(0, screen_width)
    y = random.randint(0, screen_height)
    screen.blit(image2, (x, y))
    pygame.display.flip()
    pygame.time.delay(100)

# Обробка подій миші
pygame.event.get()

# Захист та зображення 3
for i in range(100):
    # Перевірка на закриття вікна
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Візуальні артефакти та глюки
screen.blit(image3, (0, 0))
pygame.display.flip()
pygame.time.delay(3000)
screen.blit(image4, (0, 0))
pygame.display.flip()
pygame.time.delay(3000)

# Обробка подій миші
pygame.event.get()

# Bluescreen
pygame.mixer.music.stop()
screen.blit(image5, (0, 0))
pygame.display.flip()
pygame.mixer.music.load("pon2.wav")
pygame.mixer.music.play()
pygame.time.delay(6000)

# Завантаження відео
video_path = "pon.mp4"
pygame.mixer.music.load("pon1.wav")
pygame.mixer.music.play()
cap = cv2.VideoCapture(video_path)

# Отримання кількості кадрів в секунду з відеофайлу
fps = cap.get(cv2.CAP_PROP_FPS)

# Отримання часу початку відтворення
start_time = time.time()

while cap.isOpened():
    # Обчислення поточного часу від початку відтворення
    current_time = time.time() - start_time

    # Обчислення індексу кадру, який потрібно показати
    frame_index = int(current_time * fps)

    # Переміщення до потрібного кадру у відео
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)

    # Отримання потрібного кадру
    ret, frame = cap.read()
    if not ret:
        break

    # Відображення відеокадру на екрані
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)  # Відображення без дзеркального відображення (горизонтальне відображення)
    frame = pygame.surfarray.make_surface(frame)

    # Поворот відео на 270 градусів
    rotated_frame = pygame.transform.rotate(frame, 270)

    # Масштабування відео до розмірів екрану зі збереженням пропорцій
    video_width = rotated_frame.get_width()
    video_height = rotated_frame.get_height()
    scale = min(screen_width / video_width, screen_height / video_height)
    scaled_width = int(video_width * scale)
    scaled_height = int(video_height * scale)
    scaled_frame = pygame.transform.scale(rotated_frame, (scaled_width, scaled_height))

    # Розрахунок координат для центру екрану
    x = (screen_width - scaled_width) // 2
    y = (screen_height - scaled_height) // 2

    screen.blit(scaled_frame, (x, y))
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

cap.release()
pygame.quit()
sys.exit()
