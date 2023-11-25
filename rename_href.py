#!/usr/bin/env python3
import os
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

tree = ET.parse(sys.argv[1])
root = tree.getroot()

for image in root.iter('image'):
    old = Path(image.get('{http://www.w3.org/1999/xlink}href'))
    new = old.with_stem(image.get('id'))
    image.set('{http://www.w3.org/1999/xlink}href', str(new))

    try:
        old.rename(new)
    except:
        pass

tree.write(sys.argv[1], 'unicode')
