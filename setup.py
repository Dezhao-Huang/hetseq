import sys
from setuptools import setup, find_packages, Extension

if sys.platform == 'darwin':
    extra_compile_args = ['-stdlib=libc++', '-O3']
else:
    extra_compile_args = ['-std=c++11', '-O3']


class NumpyExtension(Extension):
    """Source: https://stackoverflow.com/a/54128391"""

    def __init__(self, *args, **kwargs):
        self.__include_dirs = []
        super().__init__(*args, **kwargs)

    @property
    def include_dirs(self):
        import numpy
        return self.__include_dirs + [numpy.get_include()]

    @include_dirs.setter
    def include_dirs(self, dirs):
        self.__include_dirs = dirs


extensions = [
    NumpyExtension(
        'data.data_utils_fast',
        sources=['data/data_utils_fast.pyx'],
        language='c++',
        extra_compile_args=extra_compile_args,
    ),
]


cmdclass = {}

setup(
    name='hetseq',
    version='0.0.1',
    description='cython module for indices building',
    setup_requires=[
        'cython',
        'numpy',
        'setuptools>=18.0',
    ],
    install_requires=[
        'cython',
        'numpy',
        'torch',
        'tqdm',
    ],
    packages=find_packages(exclude=[]),
    ext_modules=extensions,
    zip_safe=False,
    include_package_data=True,
    long_description="README.md",
    long_description_content_type="text/markdown",
    cmdclass = cmdclass,
)
