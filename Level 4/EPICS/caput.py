import os, time, numpy as np

import cothread
from cothread.catools import *


print(caget("chris:amplitude"))

for n in np.arange(1.0, 0.1, -0.01):
    caput("chris:amplitude", n)
    print(caget("chris:amplitude"))
    time.sleep(0.25)

for n in np.arange(0.1, 1.0, 0.01):
    caput("chris:amplitude", n)
    print(caget("chris:amplitude"))
    time.sleep(0.25)

print(caget("chris:function"))
