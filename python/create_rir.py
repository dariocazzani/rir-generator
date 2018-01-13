import math
import pyrirgen
from signal_processing import floats_to_wav
import numpy as np

DIM = [2, 3]
ORDER = [-1, 0, 1, 2]
ORIENTATION = math.pi * 2 # between 0 and 2 PI
HP_FILTER = [True, False]
MTYPE = ['bidirectional', 'hypercardioid', 'cardioid', 'subcardioid', 'omnidirectional']
RT = 1. # between 0.2 and 1.
RSL = list(np.linspace(2,16,99))

c = 340                          # Sound velocity (m/s)
fs = 16000                       # Sample frequency (samples/s)
n = 16000                         # Number of samples

NUM_RIR = 500

for idx in range(NUM_RIR):
    print(idx)
    r = list(np.random.choice(RSL, 3))
    s = list(np.random.choice(RSL, 3))
    L = list(np.random.choice(RSL, 3))
    rt = np.random.uniform(0.2,1)
    mtype = np.random.choice(MTYPE)
    hp_filter = np.random.choice(HP_FILTER)
    orientation = np.random.uniform(0, 2*math.pi)
    order = np.random.choice(ORDER)
    dim = np.random.choice(DIM)
    h = pyrirgen.generateRir(L, s, r, soundVelocity=c, fs=fs, reverbTime=rt, nSamples=n, micType=mtype, nOrder=order, nDim=dim, isHighPassFilter=hp_filter)
    floats_to_wav('rirs/rir{}.wav'.format(idx), h, fs)
