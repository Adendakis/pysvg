#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

import pysvg
import math


def testClipPath():
    mySVG = pysvg.Svg("a spiral with clipping")
    group = pysvg.G()
    pathId = "pathTriangle"
    myPath = pysvg.Path(pathData="M 0 0 L 450 450 L 900 0")
    clip = pysvg.ClipPath(id="pathTriangle")
    clip.addElement(myPath)
    clip.set_id(pathId)
    myDef = pysvg.Defs()
    myDef.addElement(clip)
    mySVG.addElement(myDef)
    group.set_clip_path("url(#%s)" % pathId)
    for i in range(1, 200):
        x = 2 * i * math.cos(2 * math.pi * i / 40.5) + 450
        y = 2 * i * math.sin(2 * math.pi * i / 40.5) + 450
        # print 'color: rgb(%s,%s,%s)' % (i, 200-i, i*(200-i)/50)
        c = pysvg.Circle(x, y, 0.2 * i)
        fill = 'none'
        strokewidth = 5
        stroke = 'rgb(%s,%s,%s)' % (i, 200 - i, i * (200 - i) / 50)
        myStyle = 'fill:%s;stroke-width:%s; stroke:%s' % (fill,
                                                          strokewidth,
                                                          stroke)
        c.set_style(myStyle)
        group.addElement(c)
    mySVG.addElement(group)
    mySVG.save('./testoutput/spiralClipped.svg')

if __name__ == '__main__':
    testClipPath()
