try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My_game',
    'author': 'Adam Zuba',
    'url': 'apzuba@gmail.com',
    'download_url': 'apzuba@gmail.com',
    'author_email': 'apzuba@gmail.com',
    'version': '1.0',
    'install_requires': ['nose'],
    'packages': ['My_game'],
    'scripts': 'My_game/ex45a.py',
    'name': 'ex45a.py'
}

setup(**config)
