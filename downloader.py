from resources import *
import pytube
from pytube import YouTube
from pytube import Playlist
from pytube.cli import on_progress
import urllib.request
import wget
import threading
import os.path
import platform
import pyperclip
from os.path import exists


vec = pygame.math.Vector2
previousprogress = 0

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
        self.download_path = ''.join(('C:/Users/', os.getlogin(), '/Desktop/Youtube_Downloader'))
        self.yt_video = YouTube
        self.yt_playlist = Playlist
        self.mp4 = ''
        self.choose_format = False
        self.preview_photo =  YouTube
        self.video_title = ''
        self.description = YouTube
        self.format = ''
        self.downloading = False
        self.isVideo = False
        self.isAudio = False
        self.playlist_len = 0
        self.playlist_counter = 0
        self.resolutions_array = []

        self.download_video_rect = pygame.Rect(600, 400, 300, 100)
        self.download_audio_rect = pygame.Rect(940, 400, 300, 100)

        self.r144p_rect = pygame.Rect(650, 450, 100, 50)
        self.r240p_rect = pygame.Rect(770, 450, 100, 50)
        self.r360p_rect = pygame.Rect(890, 450, 100, 50)
        self.r480p_rect = pygame.Rect(1010, 450, 100, 50)
        self.r720p_rect = pygame.Rect(1130, 450, 100, 50)
        self.r1080p_rect = pygame.Rect(650, 530, 100, 50)
        self.r1440p_rect = pygame.Rect(770, 530, 100, 50)
        self.r2160p_rect = pygame.Rect(890, 530, 100, 50)
        self.r4320p_rect = pygame.Rect(1010, 530, 100, 50)

        self.choose_video_resolution = False

        self.video_res = "0p"

        self.previousprogress = 0

        self.high_res = False

        self.count = 0

        self.processing = False

        self.home_button_rect = pygame.Rect(800, 300, 200, 200)

    def draw_progress(self) :

        while self.downloading :
            self.draw_download_screen(loader_01)
            clock.tick(10)
            self.draw_download_screen(loader_02)
            clock.tick(10)
            self.draw_download_screen(loader_03)
            clock.tick(10)
            self.draw_download_screen(loader_04)
            clock.tick(10)
            self.draw_download_screen(loader_05)
            clock.tick(10)
            self.draw_download_screen(loader_06)
            clock.tick(10)
            self.draw_download_screen(loader_07)
            clock.tick(10)
            self.draw_download_screen(loader_08)
            clock.tick(10)

    def draw_resolutions_screen(self) :

        while self.choose_video_resolution :


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

            # Title
            res_title = small_font.render("Choose one of the following resolutions", 1, WHITE)
            self.screen.blit(res_title, (650, 350))

            # Resolution buttons
            # [144, 240, 360, 480, 720, 1080, 1440, 2160, 4320 ] # All possible resolutions at this moment

            for resolution in self.resolutions_array :
                if 144 in self.resolutions_array :
                    r144p_button = pygame.image.load(os.path.join('Assets/buttons/144p.png'))
                    self.screen.blit(r144p_button, (self.r144p_rect.x, self.r144p_rect.y))

                if 240 in self.resolutions_array :
                    r240p_button = pygame.image.load(os.path.join('Assets/buttons/240p.png'))
                    self.screen.blit(r240p_button, (self.r240p_rect.x, self.r240p_rect.y))

                if 360 in self.resolutions_array :
                    r360p_button = pygame.image.load(os.path.join('Assets/buttons/360p.png'))
                    self.screen.blit(r360p_button, (self.r360p_rect.x, self.r360p_rect.y))

                if 480 in self.resolutions_array :
                    r480p_button = pygame.image.load(os.path.join('Assets/buttons/480p.png'))
                    self.screen.blit(r480p_button, (self.r480p_rect.x, self.r480p_rect.y))

                if 720 in self.resolutions_array :
                    r720p_button = pygame.image.load(os.path.join('Assets/buttons/720p.png'))
                    self.screen.blit(r720p_button, (self.r720p_rect.x, self.r720p_rect.y))

                if 1080 in self.resolutions_array :
                    r1080p_button = pygame.image.load(os.path.join('Assets/buttons/1080p.png'))
                    self.screen.blit(r1080p_button, (self.r1080p_rect.x, self.r1080p_rect.y))

                if 1440 in self.resolutions_array :
                    r1440p_button = pygame.image.load(os.path.join('Assets/buttons/1440p.png'))
                    self.screen.blit(r1440p_button, (self.r1440p_rect.x, self.r1440p_rect.y))

                if 2160 in self.resolutions_array :
                    r2160p_button = pygame.image.load(os.path.join('Assets/buttons/2160p.png'))
                    self.screen.blit(r2160p_button, (self.r2160p_rect.x, self.r2160p_rect.y))

                if 4320 in self.resolutions_array :
                    r4320p_button = pygame.image.load(os.path.join('Assets/buttons/4320p.png'))
                    self.screen.blit(r4320p_button, (self.r4320p_rect.x, self.r4320p_rect.y))

            pygame.display.update()

    def resolution_controller(self) :

       while self.choose_video_resolution :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.downloading = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click_res(event.pos)

    def check_click_res(self, mouse) :
        if self.r144p_rect.collidepoint(mouse) :
            self.video_res = "144p"
            self.downloading = True

        elif self.r240p_rect.collidepoint(mouse) :
            self.video_res = "240p"
            self.downloading = True
            self.choose_video_resolution = False

        elif self.r360p_rect.collidepoint(mouse) :
            self.video_res = "360p"
            self.downloading = True
            self.choose_video_resolution = False

        elif self.r480p_rect.collidepoint(mouse) :
            self.video_res = "480p"
            self.downloading = True
            self.choose_video_resolution = False

        elif self.r720p_rect.collidepoint(mouse) :
            self.video_res = "720p"
            self.downloading = True
            self.choose_video_resolution = False

        elif self.r1080p_rect.collidepoint(mouse) :
            self.video_res = "1080p"
            self.downloading = True
            self.choose_video_resolution = False
            self.high_res = True

        elif self.r1440p_rect.collidepoint(mouse) :
            self.video_res = "1440p"
            self.downloading = True
            self.choose_video_resolution = False
            self.high_res = True

        elif self.r2160p_rect.collidepoint(mouse) :
            self.video_res = "2160p"
            self.downloading = True
            self.choose_video_resolution = False
            self.high_res = True

        elif self.r4320p_rect.collidepoint(mouse) :
            self.video_res = "4320p"
            self.downloading = True
            self.choose_video_resolution = False
            self.high_res = True


    def draw_download_screen(self, loader) :

        self.screen.fill("#000000")
        self.screen.blit(mini_logo, (950, -50))

        # Title

        text = self.font.render("Youtube Downloader", 1, self.color)
        self.screen.blit(text, (50, 100))

        # Description

        description = small_font.render("We're currently downloading your videos from Youtube", 1, WHITE)
        self.screen.blit(description, (50, 170))

        description = small_font.render("Please, don't close the application until the download process succeed", 1, WHITE)
        self.screen.blit(description, (50, 200))


        # Video preview
        video_preview = pygame.transform.scale(pygame.image.load(os.path.join('downloads/img.jpg')), (500, 380))
        self.screen.blit(video_preview, (50, 220))

        # Download loader
        if self.previousprogress < 100 and self.playlist_len == 0 :
            self.screen.blit(loader, (800, 300))

        if self.previousprogress < 100 and self.playlist_len > 0 :
            if self.playlist_counter < self.playlist_len :
                self.screen.blit(loader, (800, 300))

        # Download progress
        if self.previousprogress < 100 and self.playlist_len == 0 :
            percentage = small_font.render("Downloading... ", 1, WHITE)
            self.screen.blit(percentage, (780, 450))
            percentage = small_font.render(str(self.previousprogress) + "%", 1, WHITE)
            self.screen.blit(percentage, (835, 480))

        if self.previousprogress < 100 and self.playlist_len > 0 and not self.processing :
            if self.playlist_counter < self.playlist_len :
                percentage = small_font.render("Downloading... " , 1, WHITE)
                self.screen.blit(percentage, (780, 450))
                percentage = small_font.render("[" + str(self.playlist_counter + 1) + "/" + str(self.playlist_len) + "]" , 1, WHITE)
                self.screen.blit(percentage, (835, 480))


        if self.processing :
            self.screen.blit(loader, (800, 300))
            percentage = small_font.render("Processing... " , 1, WHITE)
            self.screen.blit(percentage, (780, 450))


        if self.previousprogress == 100 and self.playlist_len == 0 :
            self.screen.blit(home_button, (820, 280))
            percentage = small_font.render("Your download is completed!", 1, WHITE)
            self.screen.blit(percentage, (750, 450))

        if self.previousprogress < 100 and self.playlist_len > 0:
            if self.playlist_counter == self.playlist_len :
                self.screen.blit(home_button, (820, 280))
                percentage = small_font.render("Your download is completed!", 1, WHITE)
                self.screen.blit(percentage, (750, 450))

        pygame.display.update()

        

    def download_progress(self, stream, chunk, bytes_remaining):

        # Download progress

        self.previousprogress
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining 

        liveprogress = (int)(bytes_downloaded / total_size * 100)
        if liveprogress > self.previousprogress:
            self.previousprogress = liveprogress
            print(liveprogress)

    def check_click_download(self, mouse) :
        if self.home_button_rect.collidepoint(mouse) :
            self.downloading = False
            self.downloader = 0

    def download_controller(self) :

       while self.downloading :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.downloading = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click_download(event.pos)

    def loading_controller(self) :

       while self.downloading :

            for event in pygame.event.get() :
                # Closes the game
                if event.type == pygame.QUIT:
                    self.downloader = 0
                    self.downloading = False

                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RETURN:
                        self.downloading = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.check_click(event.pos)

    def get_video (self) :
        # Creation of youtube object
        self.yt_video = YouTube(self.link, on_progress_callback=self.download_progress)

        # Creation of Playlist object
        self.yt_playlist = Playlist(self.link)

    def get_video_resolution(self) :
        # Get an array with the current video resolutions
        resolution =[int(i.split("p")[0]) for i in (list(dict.fromkeys([i.resolution for i in self.yt_video.streams if i.resolution])))]

        # Save it into an array
        self.resolutions_array = resolution

    def download_video(self) :

        # Check if we're downloading from a video or a playlist

        if self.format == "video" or self.format == "short" :
            if self.video_res == "1080p" or self.video_res == "1440p" or self.video_res == "2160p" or self.video_res == "4320p" :
                self.download_video_high_res()
                self.high_res = False

            else :
                # Get video properties + downloads it
                self.yt_video.streams.filter(res=self.video_res, file_extension='mp4').first().download(self.download_path)

        else :
            self.playlist_len = len(self.yt_playlist.videos)
            for video in self.yt_playlist.videos:
                if self.video_res == "1080p" or self.video_res == "1440p" or self.video_res == "2160p" or self.video_res == "4320p" :
                    self.download_playlist_high_res(video)
                    self.playlist_counter +=1

                else :
                    video.streams.filter(res=self.video_res, file_extension='mp4').first().download(self.download_path)
                    self.playlist_counter +=1

    def download_playlist_high_res(self, current_video) :

        # This means youtube is not including audio and video in the same file
        # It's a known issue with adapatative youtube streaming
        # We'll download both, audio and video and use ffmpeg to have a final video file

        # Download the video as video.mp4
        video = current_video.streams.filter(res=self.video_res, file_extension='mp4').first().download()
        base, ext = os.path.splitext(video)
        os.rename(video, 'video.mp4')
        self.count +=1

        # Download the audio as audio.mp3
        audio = current_video.streams.filter(only_audio=True).first().download()
        base, ext = os.path.splitext(audio)
        os.rename(audio, 'audio.mp3')
        self.count +=1

        # Combine both files into a single file
        self.processing = True
        base_name = current_video.title
        base_name = base_name.replace(" ", "_")
        base_name = base_name.replace("-", "_")
        base_name = base_name.replace("ñ", "n")
        base_name = base_name.replace("&", "and")
        base_name = base_name.replace('"', '')
        base_name = base_name.replace("á", "a")
        base_name = base_name.replace("à", "a")
        base_name = base_name.replace("é", "e")
        base_name = base_name.replace("í", "i")
        base_name = base_name.replace("ó", "o")
        base_name = base_name.replace("ú", "u")
        base_name = base_name.replace("!", "")
        base_name = base_name.replace("¡", "")
        base_name = base_name.replace("¿", "")
        base_name = base_name.replace("?", "")
        os.system("ffmpeg.exe -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4")
        os.rename("output.mp4", base_name + '.mp4')

        # Move the final file to user' downloads dir
        os.system("move %s.mp4 %s" % (base_name, self.download_path))

        # Delete temp files
        os.system("del /f audio.mp3")
        os.system("del /f video.mp4")
        os.system("del /f output.mp4")

        self.processing = False

    def download_video_high_res(self) :

        # This means youtube is not including audio and video in the same file
        # It's a known issue with adapatative youtube streaming
        # We'll download both, audio and video and use ffmpeg to have a final video file

        # Download the video as video.mp4
        video = self.yt_video.streams.filter(res=self.video_res, file_extension='mp4').first().download()
        base, ext = os.path.splitext(video)
        os.rename(video, 'video.mp4')
        self.count +=1

        # Download the audio as audio.mp3
        audio = self.yt_video.streams.filter(only_audio=True).first().download()
        base, ext = os.path.splitext(audio)
        os.rename(audio, 'audio.mp3')
        self.count +=1

        # Combine both files into a single file
        self.processing = True
        base_name = self.video_title.replace(" ", "_")
        base_name = base_name.replace("-", "_")
        base_name = base_name.replace("ñ", "n")
        base_name = base_name.replace("&", "and")
        base_name = base_name.replace('"', '')
        base_name = base_name.replace("á", "a")
        base_name = base_name.replace("à", "a")
        base_name = base_name.replace("é", "e")
        base_name = base_name.replace("í", "i")
        base_name = base_name.replace("ó", "o")
        base_name = base_name.replace("ú", "u")
        base_name = base_name.replace("!", "")
        base_name = base_name.replace("¡", "")
        base_name = base_name.replace("¿", "")
        base_name = base_name.replace("?", "")
        os.system("ffmpeg.exe -i video.mp4 -i audio.mp3 -c:v copy -c:a aac output.mp4")
        os.rename("output.mp4", base_name + '.mp4')

        # Move the final file to user' downloads dir
        os.system("move %s.mp4 %s" % (base_name, self.download_path))

        # Delete temp files
        os.system("del /f audio.mp3")
        os.system("del /f video.mp4")
        os.system("del /f output.mp4")

        self.processing = False


    def download_audio(self) :

        # Check if we're downloading from a video or a playlist

        audio = ''

        if self.format == "video" or self.format == "short" :
            # Get audio properties + downloads it
            audio = self.yt_video.streams.filter(only_audio=True).first().download(self.download_path)
            base, ext = os.path.splitext(audio)
            new_file = base + '_audio' + '.mp3'
            os.rename(audio, new_file)

        else :
            self.playlist_len = len(self.yt_playlist.videos)
            for mp3 in self.yt_playlist.videos :
                audio = mp3.streams.filter(only_audio=True).first().download(self.download_path)
                base, ext = os.path.splitext(audio)
                new_file = base + '_audio' + '.mp3'
                os.rename(audio, new_file)
                self.playlist_counter +=1

    def get_video_title(self) :
        # Get the title from the current video
        self.video_title = self.yt_video.streams.first().title

    def get_video_preview(self) :
        # Get the img from the url 
        self.preview_photo =  YouTube(self.link).thumbnail_url

        wget.download(self.preview_photo, 'downloads/img.jpg')

        # Video data already downloaded
        # Going to the next view
        self.downloader = 0
        self.choose_format = True

        if self.img_exists :
            self.downloading = False

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
                    pygame.quit()

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

                    if event.key == pygame.K_SPACE :
                        self.link = pyperclip.paste()

                    if event.key == pygame.K_RETURN :
                            self.link = self.link[:-1]
                            self.downloader = 0
                            self.downloading = True
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
            self.choose_format = False
            self.isVideo = True
            self.choose_video_resolution = True
            self.get_video_resolution()
            
        elif self.download_audio_rect.collidepoint(mouse) :
            self.choose_format = False
            self.isAudio = True
            self.downloading = True

    def draw(self):

        while self.downloader > 0 :
            self.screen.fill("#000000")
            self.screen.blit(yt_01, (360, -100))

            if self.format == "video" :
                dialog = self.font.render("Enter Youtube Video ID / Press SPACE to paste a URL :", 1, WHITE)
                self.screen.blit(dialog, (50, 340))

            elif self.format == "short" :
                dialog = self.font.render("Enter Youtube Short ID / Press SPACE to paste a URL :", 1, WHITE)
                self.screen.blit(dialog, (50, 340))

            elif self.format == "playlist" :
                dialog = self.font.render("Enter Youtube Playlist ID / Press SPACE to paste a URL :", 1, WHITE)
                self.screen.blit(dialog, (50, 340))

            self.input_box.w = (width * 2) - 100
            text = self.font.render(self.link, True, self.color)
            
            WIN.blit(text, (self.input_box.x+5, self.input_box.y+25))
            pygame.draw.rect(self.screen, self.color, self.input_box, 2)


            pygame.display.update()

    def draw_loading(self) :

        while self.downloading :
            self.draw_loading_screen(loader_01)
            clock.tick(10)
            self.draw_loading_screen(loader_02)
            clock.tick(10)
            self.draw_loading_screen(loader_03)
            clock.tick(10)
            self.draw_loading_screen(loader_04)
            clock.tick(10)
            self.draw_loading_screen(loader_05)
            clock.tick(10)
            self.draw_loading_screen(loader_06)
            clock.tick(10)
            self.draw_loading_screen(loader_07)
            clock.tick(10)
            self.draw_loading_screen(loader_08)
            clock.tick(10)

    def img_exists(self) :
        exists = False

        try :
            if os.path.exists("downloads/img.jpg") :
                exists = True

        except :

            print("Waiting for source...")

        return exists

    def draw_loading_screen(self, loader):

        self.screen.fill("#000000")
        self.screen.blit(yt_01, (360, -100))

        # Download loader
        if self.downloading  :
            self.screen.blit(loader, (550, 300))

        # Download progress
        if self.downloading  :
            percentage = small_font.render("Downloading Youtube Data, please wait...", 1, WHITE)
            self.screen.blit(percentage, (400, 450))

        pygame.display.update()

    def remove_previous_download(self) :
        # Temp download the img
        try :
            if platform.system() == "Linux" :
                os.system("rm -f downloads/img.jpg")
            else :
                os.system("del /f downloads\img.jpg")
        except :
            print("img file doesn't exist! Not an issue\nWe'll download a new cover")

    def download_sources (self) :
        self.remove_previous_download()
        self.get_video() # Gets the video from the given url
        self.get_video_title()
        self.get_description()
        self.get_video_preview() # Get the required video data

    def assign_format(self) :

        if self.format == "video" :
            self.link  = 'https://www.youtube.com/watch?v='

        elif self.format == "short" :
            self.link = 'https://www.youtube.com/shorts/'

        elif self.format == "playlist" :
            self.link = 'https://www.youtube.com/watch?v='


    def start_app (self, formato) :

        self.format = formato
        delta_time = self.clock.tick() / 1000

        # Assign format
        self.assign_format()

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
        thread_1 = threading.Thread(target = self.draw_loading, name ="mouse")
        thread_2 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))
        thread_3 = threading.Thread(target = self.loading_controller, name="ui")
        thread_4 = threading.Thread(target = self.download_sources, name="ui")

        # Start Both Threads
        thread_1.start()
        thread_3.start()
        thread_2.start()
        thread_4.start()

        start = self.loading_controller()

        # Wait for both threads to end
        while self.downloading :
            thread_1.join()
            thread_3.join()
            thread_2.join()
            thread_4.join()

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
            thread_1.join()
            thread_2.join()
            thread_3.join()

        # Create three new threads
        thread_1 = threading.Thread(target = self.draw_resolutions_screen, name ="mouse")
        thread_2 = threading.Thread(target = self.resolution_controller, name="ui")
        thread_3 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))

        # Start Both Threads
        thread_1.start()
        thread_2.start()
        thread_3.start()

        start = self.resolution_controller()

        while self.choose_video_resolution :
            thread_1.join()
            thread_2.join()
            thread_3.join()

        # Create three new threads
        if self.isVideo :
            thread_0 = threading.Thread(target = self.download_video, name ="video")

        else :
            thread_0 = threading.Thread(target = self.download_audio, name ="audio")

        thread_1 = threading.Thread(target = self.draw_progress, name ="mouse")
        thread_2 = threading.Thread(target = self.download_controller, name="ui")
        thread_3 = threading.Thread(target = self.update_mouse_position, name="ui", args=([delta_time]))

        # Start Both Threads
        thread_0.start()
        thread_1.start()
        thread_2.start()
        thread_3.start()

        start = self.download_controller()

        while self.downloading :
            thread_0.join()
            thread_1.join()
            thread_2.join()
            thread_3.join()

