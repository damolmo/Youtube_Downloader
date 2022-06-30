# Youtube Downloader GUI
# Full youtube downloader with the usage of Pytube library
# Provides mp3 and mp4 files of youtube videos


# Global Imports
import os

os.system("pip3 install wget")
os.system("pip3 install pytube")
os.system("pip install pytube")
os.system("pip install pytube3")
os.system("pip3 install pygame")
os.system("pip install pygame")
#os.system("python -m pip install git+https://github.com/pytube/pytube")
os.system("pip install pillow")


import pygame
import wget
import os
import json
import threading
import os.path
import time
from datetime import date
from datetime import datetime
from pathlib import Path
import pytube
from pytube import YouTube

pygame.font.init() # Import font
pygame.mixer.init() # Import sounds

# Local imports
from resources import *
from downloader import *

# Global variables
vec = pygame.math.Vector2


def vec_to_int(vector):
    return int(vector.x), int(vector.y)

def write_json () :
    data = json.dumps(yt_app_data)
    with open('resource.json', 'w') as save:
        save.write(data)

def check_app_data() :
    yt_app_data["YT_DOWNLOADER"]["RUNNING"] = "YES"
    write_json()

def finalize_program() :
    yt_app_data["YT_DOWNLOADER"]["RUNNING"] = "NO"
    write_json()

def create_window() :

    while yt_app_data["YT_DOWNLOADER"]["RUNNING"] == "YES" :
        create_window_animation(yt_01, sub_01)
        clock.tick(3)
        create_window_animation(yt_02, sub_02)
        clock.tick(3)
        create_window_animation(yt_03, sub_03)
        clock.tick(3)


def create_window_animation(LOGO, SUBTITLE) :
    WIN.fill("#000000")
    WIN.blit(LOGO, (360, -100))

    WIN.blit(SUBTITLE, (320, 450))

    pygame.display.update()

class Main :

    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()


    def check_click(self, mouse) :
        if self.rect.collidepoint(mouse):
            finalize_program()
            down = Downloader()
            down.start_app()

    def user_control(self) :

        while yt_app_data["YT_DOWNLOADER"]["RUNNING"] == "YES" :
            for event in pygame.event.get():

                if event.type == pygame.QUIT :
                    run = False
                    pygame.quit()


                if event.type == pygame.MOUSEBUTTONDOWN :
                    self.check_click(event.pos)

    def start_threads(self) :
        check_app_data()

        # Create two new threads
        thread_1 = threading.Thread(target = self.user_control, name ="mouse")
        thread_2 = threading.Thread(target = create_window, name="ui")

        # Start Both Threads
        thread_2.start()
        thread_1.start()

        start = self.user_control()

        # Wait for both threads to end
        while yt_app_data["YT_DOWNLOADER"]["RUNNING"] == "YES" :
            thread_2.join()
            thread_1.join()

    def start_program(self) :
        while self.running :
            self.start_threads()


youtube = Main()
youtube.start_program()


