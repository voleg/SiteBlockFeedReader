# coding=utf-8

__author__ = 'voleg'

from xml.dom.minidom import Document
import datetime
from xml.dom import minidom
from models import *

# @todo проникнуться
# @todo генерация XML запроса / Попробовать lxml ибо
"""
1. transmit 2 files
    file 1
            <?xml version="1.0" encoding="windows-1251"?>
            <request>
                <requestTime>2012-01-01T01:01:01.000+04:00</requestTime>
                <operatorName>Наименование оператора</operatorName>
                <inn>1234567890</inn>
                <ogrn>1234567890123</ogrn>
                <email>email@email.ru</email>
            </request>
    file 2
            Электронная подпись ... что это и где находится пока не ясно
"""
enc = 'utf-8' # попробуем сначала хорошее
opName, INN, orgname, e_mail = str('Наименование оператора'), str('1234567890'), str('1234567890123'), str('email@email.ru')
reqT = str(datetime.datetime.now()) # @todo привести к виду 2012-01-01T01:01:01.000+04:00

kwarrequest= {
    'requestTime'   : reqT,
    'operatorName'  : opName,
    'inn'           : INN,
    'orgn'          : orgname,
    'email'         : e_mail,
    }

class Document(minidom.Document):
    version = "1.1"
    encoding = "utf-8"

class request:
    def ett(self, dict):
        return dict
    def generateXMLrequest(self, dict):
        """
        генерация xml
        """

        requestDoc = Document()
        req = requestDoc.createElement("request")
        requestDoc.appendChild(req)
        for k, v in dict.items():
        #            print('{0} = {1}'.format(k, v))
            element = requestDoc.createElement(k)
            element.appendChild(requestDoc.createTextNode(v))
            req.appendChild(element)
        return requestDoc.toprettyxml()
    def __unicode__(self):
        return self.generateXMLrequest(kwarrequest)