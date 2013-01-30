import chardet
from chardet.universaldetector import UniversalDetector


def escap(html):
    code_type = chardet.detect(html)['encoding']
    return html.decode(code_type, 'ignore').encode('utf-8')


def testcode(f):
    detector = UniversalDetector()
    for line in f.readlines():
        detector.feed(line)
        if detector.done:
            break
    detector.close()
    return detector.result['encoding']
