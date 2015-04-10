from setuptools import setup

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
    version='0.1.1-alpha',
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
