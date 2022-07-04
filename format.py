from resources import *
import pytube
from pytube import YouTube
from pytube import Playlist
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import wget
import threading
import os.path
import platform

from downloader import *

vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)


class Format :

    def __init__(self) :
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()
        self.color = pygame.Color('white')
        self.font = pygame.font.Font(None, 60)
        self.video_rect = pygame.Rect(540, 430, 300, 100)
        self.short_rect = pygame.Rect(880, 420, 300, 100)
        self.playlist_rect = pygame.Rect(200, 420, 300, 100)
        self.choosing_format = True
        self.format = ''

    def check_click(self, mouse) :
        if self.video_rect.collidepoint(mouse) :
            self.format = "video"

        elif self.short_rect.collidepoint(mouse) :
            self.format = "short"

        elif self.playlist_rect.collidepoint(mouse) :
            self.format = "playlist"

        self.choosing_format = False

    def player_control(self) :

       while self.choosing_format :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.choosing_format = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)

    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())

    def draw(self) :

        while self.choosing_format :
            self.screen.fill("#000000")
            self.screen.blit(yt_01, (400, -100))

            # Title
            dialog = self.font.render("Choose your Youtube video format", 1, WHITE)
            self.screen.blit(dialog, (270, 340))

            # Icons
            self.screen.blit(videos_button, (self.video_rect.x, self.video_rect.y))
            self.screen.blit(short_button, (self.short_rect.x, self.short_rect.y))
            self.screen.blit(playlist_button, (self.playlist_rect.x, self.playlist_rect.y))

            pygame.display.update()


    def start_choosing_format(self) :
        delta_time = self.clock.tick() / 1000

        # Create three new threads
        thread_1 = threading.Thread(target = self.player_control, name ="mouse")
        thread_2 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))
        thread_3 = threading.Thread(target = self.draw, name="ui")


        # Start Both Threads
        thread_3.start()
        thread_1.start()
        thread_2.start()

        start = self.player_control()

        # Wait for both threads to end
        while self.choosing_format:
            thread_3.join()
            thread_1.join()
            thread_2.join()

        if not self.choosing_format :
            # Create object of Downloader class
            downloader = Downloader()

            # Go to the next view
            downloader.start_app(self.format)
            self.choosing_format = True
            self.start_choosing_format()

        pygame.quit()





