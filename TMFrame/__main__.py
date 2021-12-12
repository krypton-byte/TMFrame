from . import TMFRAME
import argparse
from os.path import dirname, isfile, abspath
import ast
arg = argparse.ArgumentParser(
    prog='python -m '+dirname(__file__).split('/')[-1],
    description='Music Thumbnail (Generator/Maker)')
arg.add_argument(
    '--image',
    type=str,
    required=True,
    help='Thumbnail PATH')
arg.add_argument(
    '--title',
    type=str,
    required=True,
    help='Title')
arg.add_argument(
    '--artist',
    type=str,
    required=True,
    help='Artist')
arg.add_argument(
    '--color',
    type=str,
    required=True,
    help='Color, ex: [0, 0, 0] | [206, 0, 66] etc.')
arg.add_argument(
    '--out',
    type=str,
    required=True,
    help='output destination')
arg.add_argument(
    '--width',
    type=int,
    help='Resize Image')
parse = arg.parse_args()
if not isfile(abspath(parse.image)):
    raise FileNotFoundError(parse.image)
f = TMFRAME(parse.image)
f.coloring(ast.literal_eval(parse.color))
f.pasting()
f.drawing(parse.artist, parse.title)
if parse.width:
    f.image = f.image.resize(
        (parse.width, int((f.image.height/f.image.width)*parse.width)))
f.image.convert('RGB').save(parse.out)
