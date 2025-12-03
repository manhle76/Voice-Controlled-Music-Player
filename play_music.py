import threading
import pygame
from helper import load_playlist, convert_time, song_list
from UI import Button, draw_time, draw_seek_bar, draw_name_song, draw_volume_symbol
from speak_response import speak
from listen_command import listen
from mutagen.mp3 import MP3


class MusicPlayer:
    """
    A music player with GUI and voice control using pygame.
    Supports play, pause, next/back, volume control, and song selection by voice.
    """

    def __init__(self, song_folder):
        pygame.mixer.init()
        pygame.init()
        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption("Play Music")
        self.WHITE = (255, 255, 255)
        self.clock = pygame.time.Clock()

        self.running = True

        self.playlist = load_playlist(song_folder)
        self.song_names = song_list(self.playlist)
        self.durations = [MP3(path).info.length for path in self.playlist]
        self.index_current = 0
        self.pause = False
        self.current_volume = 0.5
        pygame.mixer.music.set_volume(self.current_volume)
        pygame.mixer.music.set_endevent(pygame.USEREVENT)

        # Button states
        self.start_stop_button_name = "start"
        self.back_button_name = "back"
        self.next_button_name = "next"

        # Start voice control thread
        threading.Thread(target=self.continues_voice, daemon=True).start()

    def continues_voice(self):
        """
        Continuously listens for voice commands and controls the music player.
        """
        KEY_WORD = {
            "stop": ["pause", "stop", "dừng lại", "ngừng lại"],
            "start": ["play", "start", "resume", "begin", "bắt đầu", "tiếp tục", "phát"],
            "back": ["back", "backward", "return", "quay lại", "trở lại", "lùi lại", "trước"],
            "next": ["next", "forward", "skip", "tiếp theo", " bỏ qua", "sau"],
            "volume up": ["louder", "volume up", "to hơn", "to lên", "lớn", "bự"],
            "volume down": ["volume down", "nhỏ"],
            "turn off": ["turn off", "quit", "tắt", "thoát"],
            "song name": self.song_names
        }

        while self.running:
            command = listen()
            if not command or command.strip() == "":
                continue

            hearing = []
            for key, values in KEY_WORD.items():
                for value in values:
                    if value.lower() in command.lower():
                        if key == "song name":
                            for song in values:
                                if song.lower() in command.lower():
                                    hearing.append(f"turn on the song {song}")
                        else:
                            hearing.append(key)

            if len(hearing) == 0:
                continue

            if len(hearing) > 1:
                hearing[-1] = "or " + hearing[-1]
                speak(f"Which one do you want? {', '.join(hearing)}")

                continue

            print("Listening...")
            print("Đang lắng nghe...")
            self.execute_command(hearing[0], command)

    def execute_command(self, action, command=""):
        """Executes a single voice or button command."""
        if action == "start":
            if not self.pause and self.start_stop_button_name == "start":
                pygame.mixer.music.load(self.playlist[self.index_current])
                pygame.mixer.music.play()
            elif self.pause:
                pygame.mixer.music.unpause()
                self.pause = False
            self.start_stop_button_name = "stop"

        elif action == "stop":
            pygame.mixer.music.pause()
            self.pause = True
            self.start_stop_button_name = "start"

        elif action == "next":
            self.index_current = (self.index_current + 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.index_current])
            pygame.mixer.music.play()

        elif action == "back":
            self.index_current = (self.index_current - 1) % len(self.playlist)
            pygame.mixer.music.load(self.playlist[self.index_current])
            pygame.mixer.music.play()

        elif action == "volume up":
            self.current_volume = min(1.0, self.current_volume + 0.05)
            pygame.mixer.music.set_volume(self.current_volume)

        elif action == "volume down":
            self.current_volume = max(0, self.current_volume - 0.05)
            pygame.mixer.music.set_volume(self.current_volume)

        elif action == "turn off":
            self.running = False
            pygame.quit()

        elif "turn on the song" in action or action not in ["start", "stop", "next", "back", "volume up", "volume down", "turn off"]:
            # Match song name
            for i, song in enumerate(self.song_names):
                if song.lower() in command.lower():
                    self.index_current = i
                    pygame.mixer.music.load(self.playlist[i])
                    pygame.mixer.music.play()
                    break

    def draw_ui(self):
        """Draws all UI elements on the screen."""
        self.screen.fill(self.WHITE)

        # Buttons
        start_stop = Button(50, 70, 100, 100, self.start_stop_button_name)
        start_stop.draw_box(self.screen)

        back = Button(250, 70, 100, 100, self.back_button_name)
        back.draw_box(self.screen)

        next_btn = Button(450, 70, 100, 100, self.next_button_name)
        next_btn.draw_box(self.screen)

        volume_down = Button(50, 320, 40, 40, "")
        volume_down.draw_box(self.screen)
        volume_down.draw_minus_button(self.screen, 10)

        volume_up = Button(150, 320, 40, 40, "")
        volume_up.draw_box(self.screen)
        volume_up.draw_plus_button(self.screen, 10)

        # Volume display
        draw_volume_symbol(self.screen, 120, 260, 50,
                           self.current_volume * 100)

        # Time display
        pos_sec = int(pygame.mixer.music.get_pos() // 1000)
        if not pygame.mixer.music.get_busy() and not self.pause:
            minute, second = 0, 0
        else:
            minute, second = convert_time(pos_sec)
        draw_time(self.screen, 400, 330, 70, 30, f"{minute:02d}:{second:02d}")

        # Seek bar
        SEEK_BAR_WIDTH = 220
        SEEK_BAR_HEIGHT = 10
        process = (
            pos_sec / self.durations[self.index_current]) * (SEEK_BAR_WIDTH - 2)
        draw_seek_bar(self.screen, 320, 280, SEEK_BAR_WIDTH,
                      SEEK_BAR_HEIGHT, process)

        # Song name
        draw_name_song(self.screen, 320, 230, 200, 20,
                       self.song_names[self.index_current])

        return start_stop, back, next_btn, volume_up, volume_down

    def run(self):
        """Main loop to handle events and draw UI."""
        while self.running:
            self.clock.tick(90)
            start_stop, back, next_btn, volume_up, volume_down = self.draw_ui()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.USEREVENT:
                    self.execute_command("next")
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if start_stop.is_mouse_in():
                        self.execute_command(self.start_stop_button_name)
                    if back.is_mouse_in():
                        self.execute_command("back")
                    if next_btn.is_mouse_in():
                        self.execute_command("next")
                    if volume_up.is_mouse_in():
                        self.execute_command("volume up")
                    if volume_down.is_mouse_in():
                        self.execute_command("volume down")

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    player = MusicPlayer(r"Songs")

    print("Listening...")
    print("Đang lắng nghe...")
    player.run()
