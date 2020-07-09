#!/usr/bin/env python
import os
import random
import re
import pprint
import stat
import string
import subprocess
import sys
import textwrap
from pandocfilters import toJSONFilter, CodeBlock, Emph, Image, Para, Str
from PIL import Image as Img
from PIL import ImageDraw, ImageFont

__version__ = '0.0.1'

MARKDOWN_TAG_NAME = 'run'
ARTIFACTS_DIR = 'run_artifacts'
DEBUG_FILE = f'{ARTIFACTS_DIR}/debug.txt'

def debug(msg):
    FD = open(f'{DEBUG_FILE}', 'a')
    FD.write(f'{msg}\n\n')
    FD.close()

def execute(cmd):
    output = None
    try:
        process = \
            subprocess.run(cmd,
                check=True,
                shell=True,
                stdout=subprocess.PIPE,
                universal_newlines=True)
        output = process.stdout
    except (OSError, CalledProcessError) as e:
        pass
    return output

def getRandomFileName(length=17, ext=None):
    c = string.ascii_letters + string.digits
    if ext is None: ext = ''
    while True:
        name = ''.join(random.SystemRandom().choices(c, k=length))
        path = f'{ARTIFACTS_DIR}/{name}{ext}'
        if not os.path.isfile(path): break
    return path

def initialize():
    os.makedirs(ARTIFACTS_DIR, exist_ok=True)

def parse(value):
    output = None
    meta = {'value': value, 'cmd': None, 'in': None,
            'out': None, 'img': None}
    try:
        meta['tag'] = value[0][1][0]
    except IndexError:
        return None
    if meta['tag'] != MARKDOWN_TAG_NAME:
        return None
    meta['body'] = os.linesep.join(value[1].strip().split(os.linesep))
    for param in value[0][2]:
        if len(param) != 2 or not param[0] in meta:
            return None
        meta[param[0]] = param[1].strip()
    if meta['out'] != 'text' and meta['out'] != 'image':
        return None
    if meta['in'] == 'script':
        output = toScript(meta)
    elif meta['in'] == 'shell':
        output = toShell(meta)
    else:
        return None
    [[ident, classes, keyvals], code] = value
    if meta['out'] == 'text':
        return CodeBlock([ident, classes, keyvals], output)
    imgPath = None
    if meta['img'] is None:
        imgPath = toImageFromText(meta, output)
    else:
        imgPath = toImage(meta)
    if imgPath is None:
        return None
    return [Para([Image([ident, classes, keyvals],
        [], [imgPath, "fig:"])])]

def run(key, value, format, meta):
    if key == 'CodeBlock':
        result = parse(value)
        if result is None:
            return None
        return result

def toImage(meta):
    if not os.path.exists(meta['img']):
        return None
    return meta['img']

def toImageFromText(meta, output):
    fontSize = 14
    imgPath = getRandomFileName(ext='.png')
    maxTextWidth = 70
    height = 0
    width = 0
    text = '\n'.join(line.strip() for line in re.findall(r'.{1,80}(?:\s+|$)', output))
    for f in text.split("\n"):
        height += 1
        c = len(f)
        if c > width:
            width = c
    height = height * fontSize + (int(height * fontSize / 4.2))
    width = int(width * fontSize / 2.3)
    fnt = ImageFont.truetype('arial.ttf', fontSize)
    image = Img.new(mode = "RGB", size = (width, height), color='white')
    draw = ImageDraw.Draw(image)
    draw.text((5,0), text, font=fnt, fill=(0,0,0))
    image.save(imgPath)
    return imgPath

def toScript(meta):
    tmpScriptPath = getRandomFileName()
    with open(tmpScriptPath, 'w') as fd:
        fd.write(meta['body'])
    st = os.stat(tmpScriptPath)
    os.chmod(tmpScriptPath, os.stat(tmpScriptPath).st_mode | stat.S_IEXEC)
    cmd = "{0} {1}".format(meta['cmd'], tmpScriptPath)
    return execute(cmd)

def toShell(meta):
    cmd = "{0} {1}".format(meta['cmd'], meta['body'])
    return execute(cmd)

def main():
    initialize()
    toJSONFilter(run)

if __name__ == "__main__":
    main()
