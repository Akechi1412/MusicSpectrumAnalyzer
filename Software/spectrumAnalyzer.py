import librosa
import numpy as np

MIN_FREQ = 20               #Hz
MAX_FREQ = 20000            #Hz
NUM_FREQ_BAND = 8           #Hz
MAGNITUDE_RANGE = 8
SAMPLE_RATE = 44100         #Hz

class SpectrumAnalyzer():
    def __init__(self, chunkSize=4410, nFft=4096):
        self.__chunkSize = chunkSize
        self.__nFft = nFft
        self.__index = -1
        self.__chunks = []
        self.__period = int(np.ceil(self.__chunkSize / SAMPLE_RATE * 1000)) # milliseconds

    def create_chunks(self, src):
        data, _ = librosa.load(src, sr=SAMPLE_RATE)
        # print(len(data))
        # print(data.max())
        self.__chunks = self.make_chunks(data, self.__chunkSize)

    def get_period(self):
        return self.__period

    def reset_index(self):
        self.__index = -1

    def update_index(self, position):
        if self.__index == -1 and position == 0:
            return False
        newIndex = int(np.floor(position / self.__period))
        if newIndex >= len(self.__chunks):
            newIndex = len(self.__chunks) - 1
        if newIndex != self.__index:
            self.__index = newIndex
            # print("position: %d", position)
            # print("index: %d", newIndex)
            return True
        return False

    def cal_magnitude_levels(self):
        chunk = self.__chunks[self.__index]
        fftData = np.fft.rfft(chunk, n=self.__nFft)
        fftFreq = np.fft.rfftfreq(self.__nFft, d=1.0/SAMPLE_RATE)
        powerSpectrum = np.abs(fftData) ** 2
        # Divide the frequency range into 8 logarithmically spaced intervals
        freqBands = list(np.logspace(np.log10(MIN_FREQ), np.log10(MAX_FREQ), num=NUM_FREQ_BAND+1))
        # Compute the power in each frequency band
        power_bands = np.zeros(8)
        for i in range(NUM_FREQ_BAND):
            idx_start = np.searchsorted(fftFreq, freqBands[i])
            idx_stop = np.searchsorted(fftFreq, freqBands[i+1])
            power_bands[i] = np.sum(powerSpectrum[idx_start:idx_stop])
        maxPower = np.max(power_bands)
        if maxPower != 0:
            return [int(np.round(np.sqrt(power / maxPower) * (MAGNITUDE_RANGE))) 
                    for  power in power_bands]
        return [int(x) for x in power_bands]

    def make_chunks(self, data, chunkSize):
        numOfChunks = int(np.ceil(len(data) / float(chunkSize)))
        return [data[i * chunkSize:(i + 1) * chunkSize]
        for i in range(int(numOfChunks))]


