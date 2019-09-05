# -*- coding: utf-8 -*-
import numpy as np

tasa_arribo_prioridad = 0.05 #tasa con la que llega un arribo con prioridad

for i in range(100):
    print(np.random.poisson(tasa_arribo_prioridad))
