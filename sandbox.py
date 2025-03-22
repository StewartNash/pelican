import os
import sys

#sys.path.append(os.path.join(os.path.dirnmae(__file__), 'utilities')
sys.path.append(os.path.dirname(__file__))

from pelican import HfssInterface
from pelican import HfssPixelArray

pattern = [(1, 1), (2, 3), (5, 4), (3, 6), (7, 4)]
my_hfss_interface = HfssInterface()
design = my_hfss_interface.design
my_hfss_pixel_array = HfssPixelArray(design, pattern)
my_hfss_pixel_array.draw()
