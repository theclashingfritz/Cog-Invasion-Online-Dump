# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.showbase.ExcelHandler
__all__ = [
 'ExcelHandler']
from xml.sax import saxutils

class ExcelHandler(saxutils.DefaultHandler):

    def __init__(self):
        self.chars = []
        self.isNumber = 0
        self.cells = []
        self.rows = []
        self.tables = []

    def characters(self, content):
        self.chars.append(content)

    def startElement(self, name, attrs):
        if name == 'Data':
            if attrs.get('ss:Type') == 'Number':
                self.isNumber = 1
            else:
                self.isNumber = 0
        else:
            if name == 'Cell':
                self.chars = []
            else:
                if name == 'Row':
                    self.cells = []
                else:
                    if name == 'Table':
                        self.rows = []

    def endElement(self, name):
        if name == 'Data':
            pass
        else:
            if name == 'Cell':
                s = ('').join(self.chars)
                if s:
                    if self.isNumber:
                        floatVersion = float(s)
                        intVersion = int(floatVersion)
                        if floatVersion == intVersion:
                            s = intVersion
                        else:
                            s = floatVersion
                    else:
                        if s == 'None':
                            s = None
                    self.cells.append(s)
            else:
                if name == 'Row':
                    self.rows.append(self.cells)
                else:
                    if name == 'Table':
                        self.tables.append(self.rows)
        return