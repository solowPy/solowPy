from setuptools import setup
import os

# Write versions file
VERSION = '0.1.0-alpha'


def write_version_py():
    """ This constructs a version file for the project """
    doc = "\"\"\"This is a VERSION file and should NOT be manually altered!\"\"\""
    doc += "\nversion = '%s'" % VERSION

    filename = os.path.join(os.path.dirname(__file__), 'solowpy', 'version.py')

    with open(filename, 'w+') as fl:
        fl.write(doc)

write_version_py()  # used to control the solowpy.__version__ attribute

# Meta information
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
               'Topic :: Scientific/Engineering',
               ]

# Setup config
setup(
    name="solowPy",
    version=VERSION,
    license="MIT License",
    author="davidrpugh",
    description=DESCRIPTION,
    install_requires=["numpy",
                      "scipy",
                      "sympy",
                      "pandas",
                      "quantecon",
                      ],
    author_email="david.pugh@maths.ox.ac.uk",
    url='https://github.com/solowPy/solowPy',  # url to the repo
    classifiers=CLASSIFIERS
    )
