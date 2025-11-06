"""
Setup script for creating a standalone Mac .app bundle
Uses py2app to package the CrossOver Reset application
"""

from setuptools import setup

APP = ['crossover_reset_gui.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'iconfile': 'icon.icns',  # Optional: add your icon file
    'plist': {
        'CFBundleName': 'CrossOver Reset',
        'CFBundleDisplayName': 'CrossOver Trial Reset',
        'CFBundleIdentifier': 'com.crossover.reset',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHumanReadableCopyright': '© 2025',
        'LSMinimumSystemVersion': '10.13.0',
        'NSHighResolutionCapable': True,
    },
    'packages': ['tkinter', 'plistlib', 're', 'subprocess', 'threading'],
    'includes': [],
    'excludes': ['matplotlib', 'numpy', 'scipy', 'pandas'],  # Exclude unnecessary packages
    'optimize': 2,
}

setup(
    name='CrossOver Reset',
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
