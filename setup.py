from setuptools import setup
setup(
    name = 'img-cli',
    version = '0.1.0',
    packages = ['pycli'],
    entry_points = {
        'console_scripts': [
            'img-cli = pycli.__main__:main'
        ]
    })