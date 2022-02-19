#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Zhu Liang, Trung Vo",
    author_email='zhul9311@gmail.com, bvo4@uic.edu',
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A collection of python modules and functions for interface MD simulations",
    entry_points={
        'console_scripts': [
            'interface-md=interface-md.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='interface-md',
    name='interface-md',
    packages=find_packages(include=['interface-md', 'interface-md.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/zhul9311/interface-md',
    version='0.1.0',
    zip_safe=False,
)
