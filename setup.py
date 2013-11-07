# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

classifiers = (
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'License :: OSI Approved :: MIT License',
)

required = ('pandas')

kw = {
    'name': 'feint',
    'version': '0.1.0',
    'description': 'WebGL plotting with ruse.js for the IPython Notebook ',
    'author': 'Rob Story',
    'author_email': 'wrobstory@gmail.com',
    'license': 'MIT License',
    'url': 'https://github.com/wrobstory/feint',
    'keywords': 'data visualization',
    'classifiers': classifiers,
    'packages': ['feint'],
    'package_data': {'feint': ['*.html', '*.js']},
    'install_requires': required,
    'zip_safe': True,
}

setup(**kw)
