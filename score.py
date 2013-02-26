#-*- coding: utf-8 -*-

import math

K = 16

def Score(Ra, Rb, doc):
    Ea = 1 / (1 + math.pow(10, (Rb - Ra) / 400))
    Eb = 1 / (1 + math.pow(10, (Ra - Rb) / 400))
    Ra = Ra + K * (doc['a'] - Ea)
    Rb = Rb + K * (doc['b'] - Eb)
    savedb (Ra, Rb)

