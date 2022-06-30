from resources import *
import pytube
from pytube import YouTube

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

    def get_video (self) :
        # Creation of youtube object
        self.yt_video = YouTube(self.link)

    def download_video(self) :
        # Get video properties + downloads it
        self.yt_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(self.path)

    def player_control(self) :

       if self.downloader > 0 :

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
                            yt_app_data["YT_URL"]["URL"] = self.link
                            self.get_video() # Gets the video from the given url
                            self.download_video() # Download the video
                            enter = False
                            self.link = 'https://www.youtube.com/watch?v='
                            active = False
                            write_json()


    def update_mouse_position(self, dt):
        self.mouse = vec(pygame.mouse.get_pos())


    def draw(self):
        self.screen.fill("#c4302b")
        self.screen.blit(yt_01, (360, -100))

        self.input_box.w = (width * 2) - 100
        text = self.font.render(self.link, True, self.color)
        
        WIN.blit(text, (self.input_box.x+5, self.input_box.y+25))
        pygame.draw.rect(self.screen, self.color, self.input_box, 2)


        pygame.display.update()


    def start_app (self) :

        while self.downloader > 0:
            delta_time = self.clock.tick() / 1000
            self.player_control()        
            self.update_mouse_position(delta_time)
            self.draw()


    
        pygame.quit()