#!/usr/bin/env python

from setuptools import setup,Command
import os

class DocGenerator(Command):
    description = "Convert README.md to README.txt"
    user_options = []
    def initialize_options(self):
        pass
    def finalize_options(self):
        pass
    def run(self):
        import pypandoc
        description = pypandoc.convert('README.md', 'rst')
        with open('README.txt','w+') as f:
            f.write(description)
    
setup(
    name='viewlog',
    version='1.1.2',
    author='roubles',
    author_email='rouble@gmail.com',
    url='https://github.com/roubles/viewlog',
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description='terminal git log browser',
    long_description=open('README.txt').read(),
    scripts = ['scripts/viewlog'],
    install_requires=['pick>=0.4.0'],
    cmdclass={ 'doc': DocGenerator }
)
