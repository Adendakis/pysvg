#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

"""
This module was provided by joel duet to demonstrate Python 3.0 compatibility.
It plays around with transformations: skew, scaling and matrix
"""

import pysvg


# actions not working
def createText(content, x, y, actions=None):
    t = pysvg.Text(content, x, y)
    return t


def createMainBorderAndTexts():
    oh = pysvg.ShapeBuilder()
    elements = []

    r = oh.createRect(
        "0", "0", "946", "626", strokewidth="2px", stroke="#00C", fill="#FFF")
    elements.append(r)

    elements.append(createText("skewX(-40)", 320, 380))
    elements.append(createText("scaling(1.0 0.5)", 600, 210))
    elements.append(
        createText("matrix (0.866,0.5,-0.5,0.866,-300,-200)", 50, 480))

    return elements


def createShapes():
    oh = pysvg.ShapeBuilder()
    elements = []

    # skewX
    th = pysvg.TransformBuilder()
    th.setSkewX('-40.0')
    group = pysvg.G()
    group.set_transform(th.getTransform())
    r = oh.createRect(620, 300, width='100', height='50', rx=10,
                      ry=10, stroke='#F00', strokewidth='2px', fill='none')
    group.addElement(r)

    sh = pysvg.StyleBuilder()
    sh.setFilling('none')
    sh.setFontSize('36px')
    sh.setStrokeWidth('1px')
    sh.setStroke('#00C')
    t = pysvg.Text('Text', 635, 337)
    t.set_style(sh.getStyle())
    group.addElement(t)
    elements.append(group)

    # scaling
    th = pysvg.TransformBuilder()
    th.setScaling('1.0', '0.5')
    group = pysvg.G()
    group.set_transform(th.getTransform())
    r = oh.createRect(620, 300, width='100', height='50', rx=10,
                      ry=10, stroke='#F00', strokewidth='2px', fill='none')
    group.addElement(r)

    sh = pysvg.StyleBuilder()
    sh.setFilling('none')
    sh.setFontSize('36px')
    sh.setStrokeWidth('1px')
    sh.setStroke('#00C')
    t = pysvg.Text('Text', 635, 337)
    t.set_style(sh.getStyle())
    group.addElement(t)
    elements.append(group)

    # matrix
    th = pysvg.TransformBuilder()
    th.setMatrix('0.866', '0.5', '-0.5', '0.866', '-300.0', '-200.0')
    group = pysvg.G()
    group.set_transform(th.getTransform())
    r = oh.createRect(620, 300, width='100', height='50', rx=10,
                      ry=10, stroke='#F00', strokewidth='2px', fill='none')
    group.addElement(r)

    sh = pysvg.StyleBuilder()
    sh.setFilling('none')
    sh.setFontSize('36px')
    sh.setStrokeWidth('1px')
    sh.setStroke('#00C')
    t = pysvg.Text('Text', 635, 337)
    t.set_style(sh.getStyle())
    group.addElement(t)
    elements.append(group)

    return elements


def main():
    s = pysvg.Svg(height="100%", width="100%")
    s.set_viewBox("0 0 950 630")
    for element in createMainBorderAndTexts():
        s.addElement(element)
    for element in createShapes():
        s.addElement(element)
    print(s.getXML())
    s.save('./testoutput/testtransforms.svg')
if __name__ == '__main__':
    main()
