from setuptools import setup, find_packages

setup(
    name='checkio_taker',
    version='0.0.1',
    packages=find_packages(exclude='venv'),
    url='',
    license='MIT',
    author='kuronbo',
    author_email='kurinbo.i2o@gmail.com',
    description='memo for checkio',
    install_requires=['SQLAlchemy']
)
