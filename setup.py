from setuptools import setup

setup(
    name='browz',
    version='1.0.0',
    install_requires=[
        'autopep8==2.0.1',
        'distutils-extra-python==2.39.2',
        'pycodestyle==2.10.0',
        'PyGObject==3.42.2',
        'pytest==7.2.1',
        'pycairo==1.23.0',
    ],
    packages=[
        'browz',
        'browz_lib',
    ],
)
