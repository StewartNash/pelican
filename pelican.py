#from pathlib import Path
import os
import sys

#current_directory = Path.cwd()
current_directory = os.getcwd()
library_path = current_directory
if library_path not in sys.path:
	sys.path.append(library_path)

import pixelturtle

my_turtle  pixelturtle.PixelTurtle()
