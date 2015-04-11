import os

from distutils.core import setup


def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()


DESCRIPTION = ("Library for solving, simulating, and estimating the " +
               "Solow (1956) model of economic growth.")

CLASSIFIERS = ['Development Status :: 3 - Alpha',
               'Intended Audience :: Education',
               'Intended Audience :: Science/Research',
               'License :: OSI Approved :: MIT License',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2',
               'Programming Language :: Python :: 3',
               'Programming Language :: Python :: 2.7',
               'Programming Language :: Python :: 3.3',
               'Programming Language :: Python :: 3.4',
               ]

setup(
      name="solowpy",
      packages=['solowpy',
                'solowpy.tests'],
      version='0.1.3-alpha',
      license="MIT License",
      author="davidrpugh",
      author_email="david.pugh@maths.ox.ac.uk",
      url='https://github.com/solowPy/solowPy',
      description=DESCRIPTION,
      long_description=(read('README.md') + '\n\n' +
                        read('CITATION')),
      classifiers=CLASSIFIERS,
      )
