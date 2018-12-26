mkdir projects
cd projects/
mkdir skeleton
cd skeleton
mkdir bin
mkdir NAME
mkdir tests
mkdir docs

new-item-type file NAME/__init__.py
new-item-type file tests/__init__.py

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires':['nose'],
    'packages': ['Name'],
    'scripts': [],
    'name': 'projectname'

    }


setup(**config)