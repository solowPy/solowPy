from setuptools import setup

import solowpy

setup(
    name="solowPy",
    version=solowpy.__version__,
    license="MIT License",
    author="davidrpugh",
    install_requires=["numpy",
                      "scipy",
                      "sympy",
                      "pandas",
                      "quantecon",
                      ],
    author_email="david.pugh@maths.ox.ac.uk",
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 ]
    )
