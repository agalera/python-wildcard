#wildcard

This library is a fork of fnmatch (https://docs.python.org/2/library/fnmatch.html) to implement **

[![PypiDownloads](https://img.shields.io/pypi/dm/pywildcard.svg)](https://pypi.python.org/pypi/pywildcard)

All documentation is identical to fnmatch except "*" and "**", "**" and now "*" is "*" only affects the particular directory

https://docs.python.org/2/library/fnmatch.html

## Install

```bash
pip install pywildcard
```

Link pypi: https://pypi.python.org/pypi/pywildcard

## Example

```python
# recommeded check all examples
from basicevents import (subscribe, send_thread, send_queue,
                         send_blocking, add_subscribe, send)
import pywildcard
dirs = ['hello/world.py', 'hello/world.pyc', 'hello/world/other/folder/example.py']
pywildcard.filter(dirs, 'hello/*')
#  ['hello/world.py', 'hello/world.pyc']

pywildcard.filter(dirs, 'hello/*.py')
# ['hello/world.py']

pywildcard.filter(dirs, 'hello/**')
# ['hello/world.py', 'hello/world.pyc', 'hello/world/other/folder/example.py']

pywildcard.filter(dirs, 'hello/**.py')
# ['hello/world.py', 'hello/world/other/folder/example.py']
```

