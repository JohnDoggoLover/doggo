# compile.py
import os
import sys
import PyInstaller.__main__

def build():
    PyInstaller.__main__.run([
        'doggo.py',
        '--onefile',
        '--name', 'doggo',
        '--clean',
        '--console'
    ])
    print("\n✅ Build complete! Check the 'dist' folder for doggo executable.")

if __name__ == "__main__":
    build()
