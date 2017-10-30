import pathlib
import Player
import Sampler
import WaveFile
import noise_generator

def get_noize(N=44100, color='white', state=None, rate=44100, second=2):
    wav = []
    count = 0
    for noize in noise_generator.noise_generator(N=N, color=color, state=state):
        noize /= 3
        noize = 1.0 if 1.0 < noize else noize
        noize = -1.0 if noize < -1.0 else noize
#        print(noize)
        wav.append(noize)
        count += 1
        if rate * second <= count: break
    return wav

print(noise_generator._noise_generators)
#44.1kHzで2秒間
hz = 44100
second = 5
p = Player.Player()
p.Open(rate=hz)

wf = WaveFile.WaveFile()
wf.BasePath = pathlib.PurePath(f'res/noize/')
for color in noise_generator._noise_generators.keys():
    print(color)
    wav = Sampler.Sampler().Sampling(get_noize(N=hz, color=color, state=None, rate=hz, second=second))
    p.Play(wav, rate=hz)
    wf.Write(wav, fs=hz, filename=color)
p.Close()

