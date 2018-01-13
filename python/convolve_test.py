import numpy as np
from signal_processing import wav_to_floats, floats_to_wav, add_reverb


rir , fs= wav_to_floats('rirs/rir9.wav')
audio, fs = wav_to_floats('test.wav')

print(rir.shape)
reverbed = add_reverb(audio, rir)

floats_to_wav('reverbed.wav', reverbed, fs)
