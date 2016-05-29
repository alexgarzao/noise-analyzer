try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This analyzer interprets and filters noise in a signal',
    'author': 'Alex Sandro Garzão',
    'url': 'https://github.com/alexgarzao/noise-analyzer',
    'download_url': 'https://github.com/alexgarzao/noise-analyzer/archive/master.zip',
    'author_email': 'alexgarzao@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'noise-analyzer'
}

setup(**config)
