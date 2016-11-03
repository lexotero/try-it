#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Try IT!',
    version='0.1.0',
    author='Alejandro Otero Ortiz de Cosca',
    author_email='otero.alx@gmail.com',
    license='Apache License 2.0',
    install_requires=[
        'django>=1.10.3',
        'django-jet==1.0.2',
        'django-tinymce==2.4.0'
    ],
    extras_require={
        'development': [
            'django-debug-toolbar'
        ],
        'test': [
            'coverage'
        ]
    }
)
