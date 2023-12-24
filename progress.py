#!/usr/bin/env python3
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

svg_ns = "http://www.w3.org/2000/svg"
inkscape_ns = "http://www.inkscape.org/namespaces/inkscape"
xlink_ns = "http://www.w3.org/1999/xlink"

tree = ET.parse(sys.stdin)
root = tree.getroot()


def gen(e, prefix="*"):
    for i in e:
        label = (i.get(f"{{{inkscape_ns}}}label") or "").lstrip("!*")
        id_ = i.get("id")
        if i.tag == f"{{{svg_ns}}}g":
            print(f"* {label} ({id_})")
            gen(i, prefix="  -")
        elif i.tag == f"{{{svg_ns}}}image":
            if href := i.get(f"{{{xlink_ns}}}href"):
                status = "🫛" if Path(href).suffix == ".svg" else "❌"
                print(f"{prefix} {status} {label} ({id_})")


gen(root)
