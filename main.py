import os, sys
from libs.like import liker
from libs.photoCheckin import photoChecker

os.chdir(sys.path[0])

photoChecker()
liker()