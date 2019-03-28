import re

import fnmatch as old
from pywildcard import fnmatch, filter, translate


PATHS1 = ['hello/world.py', 'hello/world.pyc',
          'hello/world/other/folder/example.py']

PATHS2 = ['example/l1/l2/test3-1.py', 'example/l1/test2-1.py',
          'example/l1/test2-2.py', 'example/l1/l2/l3/test4-1.py']


def test_fnmatch():
    assert fnmatch('hello/world.py', 'hello/*')
    assert fnmatch('hello/world.py', 'hello/*.py')
    assert fnmatch('hello/world.py', '**')
    assert fnmatch('hello/world.py', '**.py')
    assert fnmatch('hello/world.py', 'hello/**')
    assert fnmatch('hello/world.py', 'hello/**.py')
    assert not fnmatch('hello/other/world.py', 'hello/*')
    assert not fnmatch('hello/other/world.py', 'hello/*.py')
    assert fnmatch('hello/other/world.py', '**')
    assert fnmatch('hello/other/world.py', '**.py')
    assert fnmatch('hello/other/world.py', 'hello/**')
    assert fnmatch('hello/other/world.py', 'hello/**.py')


def test_filter():
    assert filter(PATHS1, 'hello/*') == ['hello/world.py', 'hello/world.pyc']
    assert filter(PATHS1, 'hello/*.py') == ['hello/world.py']
    assert filter(PATHS1, 'hello/**') == PATHS1
    assert filter(PATHS1, 'hello/**.py') == [
        'hello/world.py', 'hello/world/other/folder/example.py']


def test_translate():
    regex = translate('example/**')
    assert regex == '(?ms)example/.*?$'
    assert re.findall(regex, '\n'.join(PATHS2)) == PATHS2
    regex = translate('example/*/*.py')
    assert regex == '(?ms)example/[^\\/]+/[^\\/]+\\.py$'
    assert re.findall(regex, '\n'.join(PATHS2)) == PATHS2[1:3]


def test_old_translate():
    regex = old.translate('example/*')
    # Python 2.7
    assert regex == '(?s:example/.*)\\Z'
    assert re.findall(regex, '\n'.join(PATHS2)) == ['\n'.join(PATHS2)]
