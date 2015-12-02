#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
'''
(C) 2008-2016 Kerim Mansour
For licensing information please refer to license.txt
'''
from xml.dom import minidom
from xml.dom import Node
import string
#from pysvg.animate import *
#from pysvg.filter import *
#from pysvg.gradient import *
#from pysvg.linking import *
#from pysvg.script import *
#from pysvg.shape import *
from pysvg.structure import Svg
#from pysvg.style import *
#from pysvg.text import *


def calculateMethodName(attr):
    name = attr
    name = name.replace(':', '_')
    name = name.replace('-', '_')
    name = 'set_'+name
    return name


def setAttributes(attrs, obj):
    for attr in attrs.keys():
        if hasattr(obj, calculateMethodName(attr)):
            eval('obj.'+calculateMethodName(attr))(attrs[attr].value)
        else:
            print calculateMethodName(attr)+' not found in:'+obj._elementName


def build(node_, anObject):
    attrs = node_.attributes
    if attrs is not None:
        setAttributes(attrs, anObject)
    for child_ in node_.childNodes:
        nodeName_ = child_.nodeName.split(':')[-1]
        if child_.nodeType == Node.ELEMENT_NODE:
            try:
                capitalLetter = string.upper(nodeName_[0])
                objectinstance = eval(capitalLetter+nodeName_[1:])()
            except:
                print 'no class for: '+nodeName_
                continue
            anObject.addElement(build(child_, objectinstance))
        elif child_.nodeType == Node.TEXT_NODE:
            if child_.nodeValue is not None:
                anObject.appendTextContent(child_.nodeValue)
        elif child_.nodeType == Node.CDATA_SECTION_NODE:
            anObject.appendTextContent('<![CDATA['+child_.nodeValue+']]>')
        elif child_.nodeType == Node.COMMENT_NODE:
            anObject.appendTextContent('<!-- '+child_.nodeValue+' -->')
        else:
            print "Some node:"+nodeName_+" value: "+child_.nodeValue
    return anObject


# TODO: packageprefix ?
def parse(inFileName):
    doc = minidom.parse(inFileName)
    rootNode = doc.documentElement
    rootObj = Svg()
    build(rootNode, rootObj)
    # Enable Python to collect the space used by the DOM.
    doc = None
    # print rootObj.getXML()
    return rootObj
