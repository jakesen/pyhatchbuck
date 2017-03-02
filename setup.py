from distutils.core import setup

setup(
    name='pyhatchbuck',
    version='0.1',
    description='Python library for Hatchbuck API',
    url='https://github.com/jakesen/pyhatchbuck',
    author='Jacob Senecal',
    author_email='jacob.senecal@gmail.com',
    license='MIT',
    packages=['hatchbuck',],
    install_requires=['requests',],
)
