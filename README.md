# wildcard

This library is a fork of fnmatch (https://docs.python.org/2/library/fnmatch.html) to implement **

[![PypiDownloads](https://img.shields.io/pypi/dm/pywildcard.svg)](https://pypi.python.org/pypi/pywildcard)

All documentation is identical to fnmatch except `*` , `*` is now `**` and `*` only affects the particular directory

https://docs.python.org/2/library/fnmatch.html

## Install

```bash
pip install pywildcard
```

Link pypi: https://pypi.python.org/pypi/pywildcard

## Examples

```python
import pywildcard
dirs = ['hello/world.py', 'hello/world.pyc', 'hello/world/other/folder/example.py']
pywildcard.filter(dirs, 'hello/*')
# ['hello/world.py', 'hello/world.pyc']

pywildcard.filter(dirs, 'hello/*.py')
# ['hello/world.py']

pywildcard.filter(dirs, 'hello/**')
# ['hello/world.py', 'hello/world.pyc', 'hello/world/other/folder/example.py']

pywildcard.filter(dirs, 'hello/**.py')
# ['hello/world.py', 'hello/world/other/folder/example.py']
```

## Diffs fnmatch & pywildcard

### fnmatch

```python
import re
import fnmatch

urls = ['example/l1/l2/test3-1.py',
        'example/l1/test2-1.py',
        'example/l1/test2-2.py',
        'example/l1/l2/l3/test4-1.py']

regex = fnmatch.translate('example/*')
# 'example\\/.*\\Z(?ms)'
re.findall(regex, "\n".join(urls))
# return ['example/l1/l2/test3-1.py\nexample/l1/test2-1.py\nexample/l1/test2-2.py\nexample/l1/l2/l3/test4-1.py']
```

### pywildcard

``` python
import re
import pywildcard

urls = ['example/l1/l2/test3-1.py',
        'example/l1/test2-1.py',
        'example/l1/test2-2.py',
        'example/l1/l2/l3/test4-1.py']

regex = pywildcard.translate('example/**')
# 'example/.*?$(?ms)'
re.findall(regex, "\n".join(urls))
# return ['example/l1/l2/test3-1.py',
#         'example/l1/test2-1.py',
#         'example/l1/test2-2.py',
#         'example/l1/l2/l3/test4-1.py']
```

## Running the unit tests

```bash
# Check out the git repository.
git clone git@github.com:agalera/python-wildcard.git
# Enter the directory.
cd python-wildcard
# Install pytest if you have not done already.
pip install pytest
# Run the tests
pytest
