from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput

class MusicPlayer(QMediaPlayer):
    def __init__(self):
        super().__init__()
        self.__audio = QAudioOutput()
        self.setAudioOutput(self.__audio)

    def setVolume(self, volume):
        self.__audio.setVolume(volume);

    def getVolume(self):
        return self.__audio.volume()
    
    def isMuted(self):
        return self.__audio.isMuted()
    
    def setMuted(self, muted):
        return self.__audio.setMuted(muted)