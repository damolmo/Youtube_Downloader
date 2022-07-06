from resources import *
import threading
import os.path
import platform
from os.path import exists
import subprocess
import json
import os


vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

class Android :

    def __init__(self) :
        pygame.init()
        self.running = True
        self.screen = WIN
        self.rect = self.screen.get_rect()
        self.mouse = vec()
        self.mouse_visible = True
        self.clock = pygame.time.Clock()
        self.color = pygame.Color('white')
        self.font = pygame.font.Font(None, 60)

        self.android_transfer = False
        self.my_device_model = ''
        self.android_transfered = False
        self.device_detected = False

    def draw_loading(self) :

        while self.android_transfer :
            self.draw(loader_01)
            clock.tick(10)
            self.draw(loader_02)
            clock.tick(10)
            self.draw(loader_03)
            clock.tick(10)
            self.draw(loader_04)
            clock.tick(10)
            self.draw(loader_05)
            clock.tick(10)
            self.draw(loader_06)
            clock.tick(10)
            self.draw(loader_07)
            clock.tick(10)
            self.draw(loader_08)
            clock.tick(10)

    def draw(self, loader):

        self.screen.fill("#000000")
        self.screen.blit(mini_logo, (1000, -50))

        text = self.font.render("Android File Transfer", 1, self.color)
        self.screen.blit(text, (50, 100))

        description = small_font.render("Please, connect your phone to your computer", 1, WHITE)
        self.screen.blit(description, (50, 170))

        description = small_font.render("The file transfer process will start automatically", 1, WHITE)
        self.screen.blit(description, (50, 200))

        self.screen.blit(android_bg, (600, 100))

        if not self.android_transfered :
            if self.my_device_model != 'unknown' :
                self.screen.blit(loader, (270, 350))
                percentage = small_font.render("Transfering... " , 1, WHITE)
                self.screen.blit(percentage, (250, 500))

            elif self.my_device_model == 'unknown' :
                self.screen.blit(loader, (270, 350))
                percentage = small_font.render("Waiting for device.." , 1, WHITE)
                self.screen.blit(percentage, (220, 500))

        if self.android_transfered :
            percentage = small_font.render("Operation Completed!" , 1, WHITE)
            self.screen.blit(percentage, (150, 350))

        pygame.display.update()

    def check_adb_device(self):

        while self.android_transfer :

            try:
                my_device_model = subprocess.check_output("cd platform-tools & adb shell getprop ro.product.model", shell=True, )
                my_device_model = my_device_model.decode("utf-8")
                my_device_model = str(my_device_model)
                self.my_device_model = my_device_model.replace(" ", "")
                self.device_detected = True

            except subprocess.CalledProcessError as e:
                self.my_device_model = "unknown"


    def check_click(self, mouse) :
        if self.rect.collidepoint(mouse) :
            print("Hello android")

    def player_control(self) :

        while self.android_transfer :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.android_transfer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)
                       

    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())

    def file_transfer(self) :

        while not self.android_transfered :
            if self.device_detected :

                type_of_file = yt_app_data["DOWNLOAD"]["FILE"]
                file = yt_app_data["DOWNLOAD"]["PATH"]

               
                if type_of_file == "audio" :
                    os.system("cd platform-tools & adb push %s /sdcard/Music" % file)
                    self.android_transfered = True

                else:
                    os.system("cd platform-tools & adb push %s /sdcard/Movies" % file)
                    self.android_transfered = True


    def start_transfer(self) :
        self.android_transfer = True
        delta_time = self.clock.tick() / 1000

        # Create three new threads
        thread_1 = threading.Thread(target = self.player_control, name ="mouse")
        thread_2 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))
        thread_3 = threading.Thread(target = self.draw_loading, name="ui")
        thread_4 = threading.Thread(target = self.check_adb_device, name="adb")
        thread_5 = threading.Thread(target = self.file_transfer, name="adb")

        # Start Both Threads
        thread_3.start()
        thread_1.start()
        thread_2.start()
        thread_4.start()
        thread_5.start()

        start = self.player_control()

        # Wait for both threads to end
        while self.android_transfer :
            thread_3.join()
            thread_1.join()
            thread_2.join()
            thread_4.join()
            thread_5.join()

