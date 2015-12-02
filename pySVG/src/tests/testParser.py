'''
Created on 26.05.2009

@author: kerim
'''

import pysvg


def main():
    anSVG = pysvg.parser.parse('./sourceimages/TMs10kSVGDemo.svg')
    anSVG.save('./testoutput/TMs10kSVGDemo.svg')

    anSVG = pysvg.parser.parse('./sourceimages/clock.svg')
    anSVG.save('./testoutput/clock.svg')


if __name__ == "__main__":
    main()
