# uncompyle6 version 3.2.4
# Python bytecode 2.7 (62211)
# Decompiled from: Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: direct.distributed.PyDatagramIterator
from panda3d.core import *
from panda3d.direct import *

class PyDatagramIterator(DatagramIterator):
    FuncDict = {STInt8: DatagramIterator.getInt8, 
       STInt16: DatagramIterator.getInt16, 
       STInt32: DatagramIterator.getInt32, 
       STInt64: DatagramIterator.getInt64, 
       STUint8: DatagramIterator.getUint8, 
       STUint16: DatagramIterator.getUint16, 
       STUint32: DatagramIterator.getUint32, 
       STUint64: DatagramIterator.getUint64, 
       STFloat64: DatagramIterator.getFloat64, 
       STString: DatagramIterator.getString, 
       STBlob: DatagramIterator.getString, 
       STBlob32: DatagramIterator.getString32}
    getChannel = DatagramIterator.getUint64

    def getArg(self, subatomicType, divisor=1):
        if divisor == 1:
            getFunc = self.FuncDict.get(subatomicType)
            if getFunc:
                retVal = getFunc(self)
            elif subatomicType == STInt8array:
                len = self.getUint16()
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt8())

            elif subatomicType == STInt16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt16())

            elif subatomicType == STInt32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getInt32())

            elif subatomicType == STUint8array:
                len = self.getUint16()
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint8())

            elif subatomicType == STUint16array:
                len = self.getUint16() >> 1
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint16())

            elif subatomicType == STUint32array:
                len = self.getUint16() >> 2
                retVal = []
                for i in range(len):
                    retVal.append(self.getUint32())

            elif subatomicType == STUint32uint8array:
                len = self.getUint16() / 5
                retVal = []
                for i in range(len):
                    a = self.getUint32()
                    b = self.getUint8()
                    retVal.append((a, b))

            else:
                raise Exception('Error: No such type as: ' + str(subAtomicType))
        else:
            getFunc = self.FuncDict.get(subatomicType)
            if getFunc:
                retVal = getFunc(self) / float(divisor)
            else:
                if subatomicType == STInt8array:
                    len = self.getUint8() >> 1
                    retVal = []
                    for i in range(len):
                        retVal.append(self.getInt8() / float(divisor))

                else:
                    if subatomicType == STInt16array:
                        len = self.getUint16() >> 1
                        retVal = []
                        for i in range(len):
                            retVal.append(self.getInt16() / float(divisor))

                    else:
                        if subatomicType == STInt32array:
                            len = self.getUint16() >> 2
                            retVal = []
                            for i in range(len):
                                retVal.append(self.getInt32() / float(divisor))

                        else:
                            if subatomicType == STUint8array:
                                len = self.getUint8() >> 1
                                retVal = []
                                for i in range(len):
                                    retVal.append(self.getUint8() / float(divisor))

                            else:
                                if subatomicType == STUint16array:
                                    len = self.getUint16() >> 1
                                    retVal = []
                                    for i in range(len):
                                        retVal.append(self.getUint16() / float(divisor))

                                else:
                                    if subatomicType == STUint32array:
                                        len = self.getUint16() >> 2
                                        retVal = []
                                        for i in range(len):
                                            retVal.append(self.getUint32() / float(divisor))

                                    else:
                                        if subatomicType == STUint32uint8array:
                                            len = self.getUint16() / 5
                                            retVal = []
                                            for i in range(len):
                                                a = self.getUint32()
                                                b = self.getUint8()
                                                retVal.append((a / float(divisor), b / float(divisor)))

                                        else:
                                            raise Exception('Error: No such type as: ' + str(subatomicType))
        return retVal