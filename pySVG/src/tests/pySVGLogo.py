#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
"""
This module is used to create the pySVG Logo.
"""

import pysvg


def main():
    mySVG = pysvg.Svg(0, 0, width="100%", height="100%")
    t = pysvg.Text("pySVG", x=0, y=100)
    group = pysvg.G()
    group.set_transform("rotate(-30)")
    t.set_stroke_width('1px')
    t.set_stroke('#00C')
    t.set_fill('none')
    t.set_font_size("36")
    group.addElement(t)

    mySVG.addElement(group)

    print mySVG.getXML()
    mySVG.save('./testoutput/pySVGLogo.svg')

if __name__ == '__main__':
    main()
