import os
import sys

try:
    from pypandoc import convert
    read_md = lambda f: convert(f, 'rst')
except ImportError:
    print("warning: pypandoc module not found")
    read_md = lambda f: open(f, 'r').read()


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = read_md('README.md')
changelog = read_md('CHANGELOG.md')


setup(
    name='wildcard',
    version='1.0.0',
    description='wildcard',
    long_description=readme+'\n\n'+changelog,
    author='Firecarrot',
    author_email='support@firecarrot.com',
    url='https://github.com/fire-carrot/wildcard',
    py_modules=['wildcard'],
    include_package_data=True,
    install_requires=[
    ],
    license="GPL",
    zip_safe=False,
    keywords='wildcard',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    entry_points={}
)
