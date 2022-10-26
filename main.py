import os, sys
oc.chdir(sys.path[0])

from photoCheckin.py import photoChecker
from like.py import liker

photoChecker()
liker()