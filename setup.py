#!/usr/bin/python
from distutils.core import setup
from subprocess import call

data_files = [ ("/usr/share/openjk/resources", ["resources/openjk.glade"]),
                    ("/usr/share/openjk/resources", ["resources/back.WAV"]),
                    ("/usr/share/openjk/resources", ["resources/click.WAV"]),
                    ("/usr/share/openjk/resources", ["resources/hover.WAV"]),
                    ("/usr/share/openjk/resources", ["resources/open.WAV"]),
                    ("/usr/share/openjk/resources", ["resources/start.WAV"]),
                    ("/usr/share/openjk/resources", ["resources/OpenJK_Icon_1024.png"]),
                    ("/usr/share/openjk/resources", ["resources/style.css"]),
                    ("/usr/share/openjk/resources", ["resources/openjk.bmp"]),
                    ("/usr/share/applications", ["resources/openjk.desktop"]) ] 

setup(name = "OpenJk Launcher",
      version = "0.2",
      description = "OpenJk Launcher",
      author = "Alessandro Toia", 
      author_email = "gort818@gmail.com",
      url = "https://github.com/gort818/openjklauncher/",
      license='GPLv3',
      scripts=['openjk'],
      data_files=data_files)
