import glob
import os


def ls():
    files = sorted(glob.glob('*.html'))
    for xfile in files:
    	print ('%s' % xfile)


ls()
