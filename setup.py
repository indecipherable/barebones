try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Skeleton Project',
    'author': 'indecipherable',
    'url': 'NA.github.wat',
    'download_url': 'NA.github.wat/skeleton',
    'author_email': 'bluemage@no-data.org',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],           # refactor
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
