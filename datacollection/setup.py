from setuptools import setup

setup(name='datacollection',
      version='0.1',
      description='Collection system for Aqua',
      url='',
      author='Jacob Hall, Samual Segee, Chi Nguyen',
      packages=['datacollection'],
      install_requires=[
          'PyQt5',
          'functools',
          'configparser',
          'json',
          'random',
          'requests',
          'serial',
          'datetime',
          'os',
          'glob',
          'threading',
          'time',
          'socket',
          'flask_socketio',
          'flask'
      ],
      zip_safe=False)
