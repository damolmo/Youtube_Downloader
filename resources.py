import os
import pygame
import json
import sys
import ctypes


## Screen properties
pygame.init()
width, height = 640, 480
fpsClock = pygame.time.Clock()
WIN = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
if sys.platform == "win32":
    HWND = pygame.display.get_wm_info()['window']
    SW_MAXIMIZE = 3
    ctypes.windll.user32.ShowWindow(HWND, SW_MAXIMIZE)

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (93.3,13.3,16.1)


## Application Values
FPS = 60
clock = pygame.time.Clock()
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)
mini_font = pygame.font.Font(None, 18)

## App External Data
my_data = open("resource.json")
yt_app_data = json.load(my_data)

## App Internal Info
icon = pygame.image.load('Assets/logo/yt_01.gif')
pygame.display.set_icon(icon)
pygame.display.set_caption("Youtube Downloader")

## Assets
# Logo
mini_logo = pygame.transform.scale(pygame.image.load(os.path.join('Assets/logo', "yt_01.gif")), (240,240))
yt_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/logo', "yt_01.gif")), (480,480))
yt_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/logo', "yt_02.gif")), (480,480))
yt_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/logo', "yt_03.gif")), (480,480))

# Subtitle
sub_01 = pygame.image.load(os.path.join('Assets/subtitle', "sub_01.png"))
sub_02 = pygame.image.load(os.path.join('Assets/subtitle', "sub_02.png"))
sub_03 = pygame.image.load(os.path.join('Assets/subtitle', "sub_03.png"))

# Buttons
video_button = pygame.transform.scale(pygame.image.load(os.path.join('Assets/buttons', "video.png")), (300,100))
audio_button = pygame.transform.scale(pygame.image.load(os.path.join('Assets/buttons', "audio.png")), (300,100))
home_button = pygame.transform.scale(pygame.image.load(os.path.join('Assets/buttons', "home.png")), (75, 75))

# Formats
videos_button = pygame.image.load(os.path.join('Assets/buttons', "videos.png"))
short_button = pygame.image.load(os.path.join('Assets/buttons', "shorts.png"))
playlist_button = pygame.image.load(os.path.join('Assets/buttons', "playlist.png"))

# Loader
loader_01 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_0_delay-0.1s.gif")), (100,100))
loader_02 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_1_delay-0.1s.gif")), (100,100))
loader_03 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_2_delay-0.1s.gif")), (100,100))
loader_04 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_3_delay-0.1s.gif")), (100,100))
loader_05 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_4_delay-0.1s.gif")), (100,100))
loader_06 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_5_delay-0.1s.gif")), (100,100))
loader_07 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_6_delay-0.1s.gif")), (100,100))
loader_08 = pygame.transform.scale(pygame.image.load(os.path.join('Assets/loader', "frame_7_delay-0.1s.gif")), (100,100))


