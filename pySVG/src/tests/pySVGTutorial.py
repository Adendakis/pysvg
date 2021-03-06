#!/usr/bin/python
# -*- coding: iso-8859-1 -*-


import pysvg


class MyDropShadow(pysvg.Filter):
    def __init__(self):
        pysvg.Filter.__init__(self)
        self.set_x('-0.25')
        self.set_y('-0.25')
        self.set_width(3)
        self.set_height(3)
        self.set_id('MyDropShadow')
        self.myGauss = pysvg.FeGaussianBlur()
        self.myGauss.set_id('DropShadowGauss')
        self.myGauss.set_stdDeviation(1.0)
        self.myGauss.set_in('SourceAlpha')
        self.myGauss.set_result('blur')
        self.addElement(self.myGauss)
        self.feColorMatrix = pysvg.FeColorMatrix()
        self.feColorMatrix.set_id('DropShadowColorMatrix')
        self.feColorMatrix.set_result('bluralpha')
        self.feColorMatrix.set_type('matrix')
        self.feColorMatrix.set_values('1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0.500000 0 ')
        self.addElement(self.feColorMatrix)
        self.feOffset = pysvg.FeOffset()
        self.feOffset.set_id('DropShadowOffset')
        self.feOffset.set_dx(1.0)
        self.feOffset.set_dy(1.0)
        self.feOffset.set_in('bluralpha')
        self.feOffset.set_result('offsetBlur')
        self.addElement(self.feOffset)
        self.feMerge = pysvg.FeMerge()
        self.feMerge.set_id('DropShadowMerge')
        self.addElement(self.feMerge)
        self.firstFeMergeNode = pysvg.FeMergeNode()
        self.feMerge.addElement(self.firstFeMergeNode)
        self.firstFeMergeNode.set_id('DropShadowMergeNode1')
        self.firstFeMergeNode.set_in('offsetBlur')
        self.secondFeMergeNode = pysvg.FeMergeNode()
        self.feMerge.addElement(self.secondFeMergeNode)
        self.secondFeMergeNode.set_id('DropShadowMergeNode2')
        self.secondFeMergeNode.set_in('SourceGraphic')


def MyImage():
    s = pysvg.Svg()
    i = pysvg.Image(x=80, y=25, width=88, height=31)
    i.set_xlink_href('http://img0.gmodules.com/ig/images/googlemail.gif')
    s.addElement(i)
    i = pysvg.Image(x=80, y=125, width=88, height=31)
    i.set_xlink_href('../sourceimages/images.jpg')
    s.addElement(i)
    print s.getXML()
    s.save('./testoutput/10_Image.svg')


def MyLinearGradient():
    mySVG = pysvg.Svg("test")
    d = pysvg.Defs()

    lg = pysvg.LinearGradient()
    lg.set_id("orange_red")
    s = pysvg.Stop(offset="0%")
    s.set_stop_color('rgb(255,255,0)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    s = pysvg.Stop(offset="100%")
    s.set_stop_color('rgb(255,0,0)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    d.addElement(lg)

    oh = pysvg.ShapeBuilder()
    e = oh.createEllipse(cx="200", cy="190", rx="85", ry="55",
                         fill="url(#orange_red)")

    mySVG.addElement(d)
    mySVG.addElement(e)
    print mySVG.getXML()
    mySVG.save('./testoutput/8_LinearGradient.svg')


def MyRadialGradient():
    mySVG = pysvg.Svg()
    d = pysvg.Defs()

    lg = pysvg.RadialGradient()
    lg.set_id("grey_blue")
    s = pysvg.Stop(offset='0%')
    s.set_stop_color('rgb(200,200,200)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    s = pysvg.Stop(offset='100%')
    s.set_stop_color('rgb(0,0,255)')
    s.set_stop_opacity(1)
    lg.addElement(s)
    d.addElement(lg)

    oh = pysvg.ShapeBuilder()
    e = oh.createEllipse(cx="230", cy="200", rx="110", ry="100",
                         fill="url(#grey_blue)")

    mySVG.addElement(d)
    mySVG.addElement(e)
    print mySVG.getXML()
    mySVG.save('./testoutput/9_RadialGradient.svg')


def Grouping():
    s = pysvg.Svg()

    # testing container
    myStyle = pysvg.StyleBuilder()
    myStyle.setStrokeWidth(2)
    myStyle.setStroke("green")

    group = pysvg.G()
    group.set_style(myStyle.getStyle())
    group.addElement(pysvg.Line(300, 300, 600, 600))
    group.addElement(pysvg.Circle(500, 500, 50))
    s.addElement(group)

    group = pysvg.G()
    group.set_style(myStyle.getStyle())
    style_dict = {"stroke": "#000000", "fill": "none",
                  "stroke-width": "49", "stroke-opacity": "0.027276"}
    p = pysvg.Path(pathData="M 300 100 A 1,1 0 0 1 802,800")
    p.set_style(pysvg.StyleBuilder(style_dict).getStyle())
    p2 = pysvg.Path(pathData="M 100 300 A 1,1 0 0 1 802,800")
    p2.set_style(pysvg.StyleBuilder(style_dict).getStyle())
    group.addElement(p)
    group.addElement(p2)
    s.addElement(group)
    print s.getXML()
    s.save('./testoutput/7_Grouping.svg')


def ComplexShapes():
    oh = pysvg.ShapeBuilder()
    mySVG = pysvg.Svg("test")
    d = pysvg.Defs()
    d.addElement(MyDropShadow())
    mySVG.addElement(d)

    pl = oh.createPolyline(points="50,375 150,375 150,325 250,325 250,375 \
350,375 350,250 450,250 450,375 550,375 550,175 650,175 650,375 750,375 \
750,100 850,100 850,375 950,375 950,25 1050,25 1050,375 1150,375 ",
                           strokewidth=10, stroke='blue')
    mySVG.addElement(pl)

    pointsAsTuples = [(350, 75), (379, 161), (469, 161),
                      (397, 215), (423, 301), (350, 250),
                      (277, 301), (303, 215), (231, 161), (321, 161)]
    pg = oh.createPolygon(points=oh.convertTupleArrayToPoints(pointsAsTuples),
                          strokewidth=10, stroke='blue', fill='red')
    pg.set_filter('url(#MyDropShadow)')
    mySVG.addElement(pg)

    sh = pysvg.StyleBuilder()
    sh.setFilling('#EEE')
    sh.setStroke('#00F')
    sh.setStrokeWidth('2px')
    path1 = pysvg.Path('M 40,530 L 100,560 L 60,520 Z', style=sh.getStyle())
    sh2 = pysvg.StyleBuilder()
    sh2.setFilling('#FFC')
    sh2.setStroke('#00F')
    sh2.setStrokeWidth('2px')
    path2 = pysvg.Path(style=sh2.getStyle())
    path2.appendMoveToPath(190, 520, False)
    # as you can see we can mix strings and ints without trouble
    path2.appendCubicCurveToPath('+0', '+0', 30, 30, -60, 30, True)
    path2.appendCloseCurve()
    sh3 = pysvg.StyleBuilder()
    sh3.setFilling('none')
    sh3.setStroke('#00F')
    sh3.setStrokeWidth('2px')
    path3 = pysvg.Path('M 230,530', style=sh3.getStyle())
    path3.appendQuadraticCurveToPath(0, 30, 30, 0)
    path3.appendQuadraticCurveToPath(30, -30, 30, 0)
    path3.appendQuadraticCurveToPath(-0, 30, 30, 0)
    path3.appendQuadraticCurveToPath(30, -20, 30, 0)
    mySVG.addElement(path1)
    mySVG.addElement(path2)
    mySVG.addElement(path3)
    mySVG.save('./testoutput/6_ComplexShapes.svg')


def Shapes():
    oh = pysvg.ShapeBuilder()
    s = pysvg.Svg("test")
    s.addElement(oh.createRect(0, 0, 400, 200, 12, 12, strokewidth=2,
                               stroke='navy'))
    s.addElement(oh.createRect(100, 50, 200, 100, strokewidth=2, stroke='navy',
                               fill='yellow'))
    s.addElement(oh.createCircle(700, 500, 50, strokewidth=5, stroke='red'))
    s.addElement(oh.createCircle(810, 500, 50, strokewidth=5, stroke='yellow',
                                 fill='#AAAAAA'))
    s.addElement(oh.createEllipse(600, 50, 50, 30, strokewidth=5,
                                  stroke='red'))
    s.addElement(oh.createEllipse(700, 50, 50, 30, strokewidth=5,
                                  stroke='yellow', fill='#00AABB'))
    s.addElement(oh.createLine(0, 0, 300, 300, strokewidth=2, stroke="black"))
    s.save('./testoutput/4_Shapes.svg')


def MyLine():
    s = pysvg.Svg("test")
    myStyle = pysvg.StyleBuilder()
    myStyle.setStrokeWidth(2)
    myStyle.setStroke('black')
    l = pysvg.Line(0, 0, 300, 300)
    l.set_style(myStyle.getStyle())
    s.addElement(l)
    # easier method with ShapeBuilder
    oh = pysvg.ShapeBuilder()
    s.addElement(oh.createLine(10, 0, 300, 300, strokewidth=2, stroke="blue"))
    s.save('./testoutput/5_Line.svg')


def TextFeatures():
    s = pysvg.Svg("test")
    myStyle = pysvg.StyleBuilder()
    myStyle.setFontFamily(fontfamily="Verdana")
    myStyle.setFontSize('5em')
    myStyle.setFilling(fill="blue")
    t1 = pysvg.Text("Verdana, blue, 5em", 0, 100)
    t1.set_style(myStyle.getStyle())
    t2 = pysvg.Text("pySVG simple", 0, 200)
    s.addElement(t1)
    s.addElement(t2)

    r = pysvg.Rect(350, 250, 100, 100, id="myRect")
    r.set_fill("green")
    s.addElement(r)

    myStyle = pysvg.StyleBuilder()
    myStyle.setFontFamily(fontfamily="Times")
    myStyle.setFontSize('2em')
    myStyle.setFontStyle('italic')
    myStyle.setFontWeight('bold')
    myStyle.setFilling(fill="red")
    myStyle.setFillOpacity('0.5')
    myStyle.setFillRule('evenodd')

    t3 = pysvg.Text("Times, italic, 2em, bold, opacity=0.5, fillrule=evenodd",
                    0, 300)
    t3.set_style(myStyle.getStyle())
    s.addElement(t3)

    myStyle = pysvg.StyleBuilder()
    myStyle.setFontFamily(fontfamily="Times")
    myStyle.setFontSize('2em')
    myStyle.setFontStyle('italic')
    myStyle.setFilling(fill="red")
    myStyle.setFillOpacity('0.5')
    # myStyle.fill="blue"
    t4 = pysvg.Text("Times, italic, 2em, non bold, opacity=0.5", 0, 400)
    t4.set_style(myStyle.getStyle())
    s.addElement(t4)
    s.save('./testoutput/3_TextFeatures.svg')


def HelloWorld2():
    s = pysvg.Svg()
    myStyle = pysvg.StyleBuilder()
    myStyle.setFontFamily(fontfamily="Verdana")
    myStyle.setFontSize('5em')  # no need for the keywords all the time
    myStyle.setFilling("blue")
    t1 = pysvg.Text("Hello World", 0, 100)
    t1.set_style(myStyle.getStyle())
    s.addElement(t1)
    s.save('./testoutput/2_HelloWorld2.svg')


def HelloWorld1():
    s = pysvg.Svg()
    t = pysvg.Text("Hello World", 0, 100)
    s.addElement(t)
    s.save('./testoutput/1_HelloWorld1.svg', encoding='UTF-8')


def KWARGS():
    s = pysvg.Svg()
    kw = {}
    kw['style'] = 'font-size:20em; font-family:Verdana; fill:blue; '
    t1 = pysvg.Text("KWARGS Text", 0, 300, **kw)
    s.addElement(t1)
    s.save('./testoutput/KWARGS.svg')


def tutorialChain():
    HelloWorld1()
    HelloWorld2()
    TextFeatures()
    Shapes()
    MyLine()
    ComplexShapes()
    Grouping()
    MyLinearGradient()
    MyRadialGradient()
    MyImage()
    KWARGS()

if __name__ == '__main__':
    tutorialChain()
