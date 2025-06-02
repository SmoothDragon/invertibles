#!/usr/bin/env python3

from __future__ import division

import solid2 as sd
import scipy.spatial

from math import atan, sqrt
import numpy as np
from typing import *


if __name__ == '__main__':
    fn = 256
    r = 25
    point = sd.circle(r=r)
    piece = sd.hull()(point, sd.translate([r*np.pi*2/3,0])(point))
    piece = sd.rotate(60)(piece)
    piece = sd.hull()(piece, sd.translate([r*np.pi*2/3,0])(point))
    piece = sd.linear_extrude(10)(piece)
    final = sd.scad_render(piece, file_header=f'$fn={fn};')
    print(final)
