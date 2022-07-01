from resources import *
import pytube
from pytube import YouTube
import urllib.request
from io import BytesIO
from PIL import Image, ImageTk
import wget
import threading
import os.path
import platform

vec = pygame.math.Vector2

def vec_to_int(vector):
    return int(vector.x), int(vector.y)

def write_json () :
    data = json.dumps(yt_app_data)
    with open('resource.json', 'w') as save:
        save.write(data)

class Downloader :
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
        self.input_box = pygame.Rect(50, 400, 600, 100)
        self.active = False
        self.downloader = 1
        self.link = 'https://www.youtube.com/watch?v='
        self.player_one = 0
        self.player_two = 0
        self.player_three = 0
        self.path = 'downloads/'
        self.yt_video = YouTube
        self.mp4 = ''
        self.choose_format = False
        self.preview_photo =  YouTube
        self.video_title = ''
        self.description = YouTube

        self.download_video_rect = pygame.Rect(600, 400, 300, 100)
        self.download_audio_rect = pygame.Rect(940, 400, 300, 100)

    def get_video (self) :
        # Creation of youtube object
        self.yt_video = YouTube(self.link)

    def download_video(self) :
        # Get video properties + downloads it
        self.yt_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(self.path)

    def download_audio(self) :
        # Get audio properties + downloads it
        audio = self.yt_video.streams.filter(only_audio=True).first().download(self.path)
        base, ext = os.path.splitext(audio)
        new_file = base + '.mp3'
        os.rename(audio, new_file)

    def get_video_title(self) :
        # Get the title from the current video
        self.video_title = self.yt_video.streams.first().title

    def get_video_preview(self) :
        # Get the img from the url 
        self.preview_photo =  YouTube(self.link).thumbnail_url

        # Temp download the img
        try :
            if platform.system() == "Linux" :
                os.system("rm -f downloads/img.jpg")
            else :
                os.system("del /f downloads\img.jpg")
        except :
            print("img file doesn't exist! Not an issue\nWe'll download a new cover")

        wget.download(self.preview_photo, 'downloads/img.jpg')

        # Video data already downloaded
        # Going to the next view
        self.downloader = 0
        self.choose_format = True

    def get_description(self) :
        # Get video description
        self.description = self.yt_video.description


    def draw_video_preview (self) :

        while self.choose_format :

            self.screen.fill("#000000")
            self.screen.blit(mini_logo, (950, -50))

            # Video Title

            size = 0
            title = ''

            for char in self.video_title :
                size += 1

            
            for char in self.video_title[0:40:1]:
                title+=char

            text = self.font.render(title, 1, self.color)
            self.screen.blit(text, (50, 100))



            # Video Description
            # Total size of the yt video description
            max_size = 0

            for char in self.description :
                max_size +=1
            
            # Show description on display

            phrase = ''
            start = 0
            end = 85
            height = 170
            max_length = 0

            while max_size >= 85 and max_length < 340 :

                for char in self.description[start:end:1] :
                    phrase += char

                phrase.replace("\n", '')
                description = small_font.render(phrase, 1, WHITE)
                self.screen.blit(description, (50, height))

                phrase = ''
                max_size -=85
                max_length +=85
                start += 85
                end += 85
                height +=30


            # Video preview
            video_preview = pygame.transform.scale(pygame.image.load(os.path.join('downloads/img.jpg')), (500, 380))
            self.screen.blit(video_preview, (50, 280))


            # Video Download Buttons
            self.screen.blit(video_button, (600, 400))
            self.screen.blit(audio_button, (940, 400))

            # Display rect
            #pygame.draw.rect(WIN, BLACK, self.download_video)
            #pygame.draw.rect(WIN, WHITE, self.download_audio)

            pygame.display.update()


    def player_control(self) :

       while self.downloader > 0 :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.running = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.collidepoint(event.pos):

                        self.active = not self.active
                    else:
                        self.active = False

                if event.type == pygame.KEYDOWN:
                
                    if event.key == pygame.K_BACKSPACE:
                        self.link = self.link[:-1]
                    else:
                        self.link += event.unicode

                    if event.key == pygame.K_RETURN :
                            self.link = self.link[:-1]
                            self.get_video() # Gets the video from the given url
                            self.get_video_title()
                            self.get_description()
                            self.get_video_preview() # Get the required video data
                            enter = False
                            active = False
                        
    def preview_controller(self) :

       while self.choose_format :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.choose_format = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)



    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())

    def check_click (self, mouse) :

        if self.download_video_rect.collidepoint(mouse) :
            self.download_video()

        elif self.download_audio_rect.collidepoint(mouse) :
            self.download_audio()


    def draw(self):

        while self.downloader > 0 :
            self.screen.fill("#000000")
            self.screen.blit(yt_01, (360, -100))

            dialog = self.font.render("Enter Youtube Video ID :", 1, WHITE)
            self.screen.blit(dialog, (50, 340))

            self.input_box.w = (width * 2) - 100
            text = self.font.render(self.link, True, self.color)
            
            WIN.blit(text, (self.input_box.x+5, self.input_box.y+25))
            pygame.draw.rect(self.screen, self.color, self.input_box, 2)


            pygame.display.update()


    def start_app (self) :

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
        while self.downloader > 0:
            thread_3.join()
            thread_1.join()
            thread_2.join()

        # Create three new threads
        thread_1 = threading.Thread(target = self.draw_video_preview, name ="mouse")
        thread_2 = threading.Thread(target = self.preview_controller, name="ui")
        thread_3 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))


        # Start Both Threads
        thread_1.start()
        thread_2.start()
        thread_3.start()

        start = self.preview_controller()

        while self.choose_format :
            self.draw_video_preview()
            self.preview_controller()
            self.update_mouse_position(delta_time)


        pygame.quit()