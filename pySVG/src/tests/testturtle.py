'''
Created on 27.02.2010

@author: kerim
'''
import pysvg


def testMultiplePaths():
    t = pysvg.Turtle()
    t.penDown()
    print(t.getPosition())
    t.forward(205)
    print(t.getPosition())
    t.right(90)
    t.forward(205)
    print(t.getPosition())
    t.right(90)
    t.forward(105)
    print(t.getPosition())
    t.right(90)
    t.forward(105)
    print(t.getPosition())
    t.penUp()
    t.moveTo(pysvg.Vector(300, 300))
    print(t.getPosition())
    t.penDown()
    t.forward(205)
    print(t.getPosition())
    t.finish()
    # print (t.getXML())
    s = pysvg.Svg(0, 0, 2000, 2000)
    s = t.addTurtlePathToSVG(s)
    s.save('./testoutput/testTurtle.svg')


def testLindenMayer():
    s = pysvg.Svg(0, 0, 2000, 2000)
    commands = 'F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F+F+F-F-FF+F+F-F'
    t = pysvg.Turtle()
    t.moveTo(pysvg.Vector(500, 250))
    t.penDown()
    angle = 90
    distance = 40
    for cmd in commands:
        print(cmd)
        if cmd == 'F':
            t.forward(distance)
        elif cmd == '+':
            t.right(angle)
        elif cmd == '-':
            t.left(angle)
        print(t.getPosition())
    t.penDown()
    print (t.getXML())
    s = t.addTurtlePathToSVG(s)
    s.save('./testoutput/testTurtle.svg')


if __name__ == '__main__':
    testLindenMayer()
    # testMultiplePaths()
