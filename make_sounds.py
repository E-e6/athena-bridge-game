import wave
import struct
import math

def create_beep(filename, freq=440, duration_ms=300, volume=0.5, sample_rate=44100):
    n_samples = int(sample_rate * duration_ms / 1000)
    wav_file = wave.open(filename, "w")
    nchannels = 1
    sampwidth = 2
    framerate = sample_rate
    nframes = n_samples
    comptype = "NONE"
    compname = "not compressed"
    wav_file.setparams((nchannels, sampwidth, framerate, nframes, comptype, compname))

    for i in range(n_samples):
        sample = volume * math.sin(2 * math.pi * freq * i / sample_rate)
        wav_file.writeframes(struct.pack('h', int(sample * 32767.0)))

    wav_file.close()

# Create two beep sounds: high pitch for correct, low pitch for wrong
create_beep("correct.wav", freq=880)
create_beep("wrong.wav", freq=220)

print("Sound files created!")