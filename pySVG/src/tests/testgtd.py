'''
Created on 11.11.2010

@author: kerim
'''
import pysvg


def main():
    anSVG = pysvg.parser.parse('./sourceimages/gtdsample.svg')

    print anSVG.getAllElements()
    for element in anSVG.getAllElements():
        if isinstance(element, pysvg.TextContent) == False:
            print element.get_id()

    for element in anSVG.getAllElementsOfHirarchy():
        if isinstance(element, pysvg.TextContent) == False:
            print element.get_id()

    for element in anSVG.getElementsByType(pysvg.Rect):
        print element.get_id()
        print element.getAttributes()


if __name__ == "__main__":
    main()
