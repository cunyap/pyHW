import os
from setuptools import setup


def extract_version():
    """
    Return pyHW.__version__ from pyHW/__init__.py
    """
    with open('pyHW/__init__.py') as fd:
        ns = {}
        for line in fd:
            if line.startswith('__version__'):
                exec(line.strip(), ns)
                return ns['__version__']


setup(name='pyHW',
      version=extract_version(),
      author="andreas",
      author_email="andreas",
      url='https://github.com/cunyap/pyhw',
      download_url='https://github.com/cunyap/pyhw',
      description='Hellow World',
      packages={'pyHW': 'pyHW',
                'pyHW.tests': 'pyHW/tests',
                'pyHW.icons': 'pyHW/icons'},
      package_dir={'pyHW': 'pyHW',
                'pyHW.tests': 'pyHW/tests',
                'pyHW.icons': 'pyHW/icons'},
      keywords='Hello World',
      license='MIT',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'Natural Language :: English',
                   'Operating System :: POSIX :: Linux',
                   'Operating System :: MacOS :: MacOS X',
                   'Operating System :: Microsoft :: Windows :: Windows 7',
                   'Programming Language :: Python :: 3',
                   'License :: OSI Approved :: MIT',
                   'Topic :: Scientific/Engineering'
                   ],
      install_requires=['pytest', 'pandas>=0.20.0', 'numpy>=1.14.5', 'scipy>=1.4.1', 'nptdms>=0.12.0', 'tqdm>=4.23.4',
                        'plotnine', 'PyQT5', 'lxml', 'xmltodict', 'matplotlib', 'pyyaml', 'pyqtgraph',
                        'xmlunittest', 'scikit-image', 'pgcolorbar>=1.1.1', 'cmlib', 'imagecodecs',
                        'ipython', 'PyInstaller'],

      )