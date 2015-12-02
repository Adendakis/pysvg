#!/usr/bin/python
# -*- coding: iso-8859-1 -*-
'''
(C) 2008-2016 Kerim Mansour
For licensing information please refer to license.txt
'''
from attributes import CoreAttrib, XLinkAttrib
from core import BaseElement


class Script(BaseElement, CoreAttrib, XLinkAttrib):
    """
    Class representing the script element of an svg doc.
    """
    def __init__(self, **kwargs):
        BaseElement.__init__(self, 'script')
        self.setKWARGS(**kwargs)

    def set_type(self, aType):
        self._attributes['type'] = aType

    def get_type(self):
        return self._attributes.get('type')
