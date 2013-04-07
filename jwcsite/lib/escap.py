#-*-coding: utf-8-*-
# @author: xiangchao<cloudaice@gmail.com>

import chardet
from chardet.universaldetector import UniversalDetector


def escap(html):
    code_type = chardet.detect(html)['encoding']
    print code_type
    return html.decode('GBK', 'ignore').encode('utf-8', 'ignore')


def testcode(f):
    detector = UniversalDetector()
    for line in f.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']
