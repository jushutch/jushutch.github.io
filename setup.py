"""
EECS 485 project 1 static site generator.

Andrew DeOrio <awdeorio@umich.edu>
"""

from setuptools import setup

setup(
    name='generator',
    version='0.1.0',
    packages=['generator'],
    include_package_data=True,
    install_requires=[
        'bs4',
        'click',
        'html5validator',
        'jinja2',
        'pycodestyle',
        'pydocstyle',
        'pylint',
        'pytest',
        'requests',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'generator = generator.__main__:main'
        ]
    },
)
