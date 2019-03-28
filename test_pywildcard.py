import re

import fnmatch as old
from pywildcard import fnmatch, filter, translate


TEST_PATHS2 = ['example/l1/l2/test3-1.py', 'example/l1/test2-1.py',
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
    dirs = ['hello/world.py', 'hello/world.pyc',
            'hello/world/other/folder/example.py']
    assert filter(dirs, 'hello/*') == ['hello/world.py', 'hello/world.pyc']
    assert filter(dirs, 'hello/*.py') == ['hello/world.py']
    assert filter(dirs, 'hello/**') == dirs
    assert filter(dirs, 'hello/**.py') == [
        'hello/world.py', 'hello/world/other/folder/example.py']


def test_translate():
    regex = translate('example/**')
    assert regex == 'example/.*?$(?ms)'
    assert re.findall(regex, '\n'.join(TEST_PATHS2)) == TEST_PATHS2
    regex = translate('example/*/*.py')
    assert regex == 'example/[^\/]+/[^\/]+\.py$(?ms)'
    assert re.findall(regex, '\n'.join(TEST_PATHS2)) == TEST_PATHS2[1:3]

def test_old_translate():
    regex = old.translate('example/*')
    # Python 2.7
    assert regex == '(?s:example/.*)\\Z'
    assert re.findall(regex, '\n'.join(TEST_PATHS2)) == ['\n'.join(TEST_PATHS2)]
