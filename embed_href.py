#!/usr/bin/env python3

import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

svg_ns = "{http://www.w3.org/2000/svg}"
inkscape_ns = "{http://www.inkscape.org/namespaces/inkscape}"
xlink_ns = "{http://www.w3.org/1999/xlink}"

tree = ET.parse(sys.stdin)  # noqa: S314
root = tree.getroot()


def add_prefix(e: ET.Element, prefix: str):
    for c in e.iter():
        if id_ := c.get("id"):
            c.set("id", prefix + id_)
        if href := c.get(f"{xlink_ns}href"):
            c.set(
                f"{xlink_ns}href",
                re.sub(r"#([\w-]*)", f"#{prefix}\\1", href),
            )
        if style := c.get("style"):
            c.set(
                "style",
                re.sub(r"url\(\s*#([\w-]*)\s*\)", f"url(#{prefix}\\1)", style),
            )


def embed(e: ET.Element, prefix: str = "") -> ET.Element:
    if href := e.get(f"{xlink_ns}href"):
        path, _, id_ = href.partition("#")
    else:
        path, id_ = None, None

    if not (path and Path(path).suffix == ".svg"):
        for i, c in enumerate(e):
            e.remove(c)
            e.insert(i, embed(c))
        return e

    new_e = ET.parse(path).getroot()  # noqa: S314
    if id_ != "":
        new_e = new_e.find(f".//*[@id='{id_}']")
    new_e.attrib |= {
        k: v for k, v in e.attrib.items() if k != f"{xlink_ns}href"
    }
    add_prefix(new_e, prefix)
    return embed(new_e, prefix + id_ + "-")


ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace(
    "sodipodi",
    "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
)
ET.register_namespace(
    "inkscape",
    "http://www.inkscape.org/namespaces/inkscape",
)
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

embed(root)
tree.write(sys.stdout, encoding="unicode")
