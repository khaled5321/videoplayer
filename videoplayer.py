import threading
import vlc
import time
import itertools


class VideoThread(threading.Thread):

    def __init__(self, wid):
        threading.Thread.__init__(self)
        self.video_list = ['videos\sector_b5.mp4', 'videos\SVC_video.mp4']
        self.Instance = vlc.Instance()
        self.wid = wid
        self.Ended = 6
        self._is_running = True

    def run(self) -> None:
        player = self.Instance.media_player_new()
        player.video_set_aspect_ratio('5:3')
        for video in itertools.cycle(self.video_list):
            media = self.Instance.media_new(video)
            player.set_media(media)
            player.set_hwnd(self.wid) # use on windows
            # player.set_xwindow(wid) # use on linux
            player.play()
            time.sleep(1.5)
            current_state = player.get_state()
            while current_state != self.Ended:
                current_state = player.get_state()
                if not self._is_running:
                    return
                time.sleep(2)
            # duration = player.get_length() / 1000
            # time.sleep(duration)
        
    def stop(self):
        self._is_running = False
