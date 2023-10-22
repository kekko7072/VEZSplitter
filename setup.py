"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['VEZSplitter.py']
DATA_FILES = []
OPTIONS = {
    'packages': ['PyPDF2', 'tkinter'],
    'iconfile': '/Users/francescovezzani/Developer/VEZSplitter/icon.icns',
    'plist': {'CFBundleShortVersionString': '0.1.0', 'CFBundleIdentifier': 'francesco.vezzani.VEZSplitter'}
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)