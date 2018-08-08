from setuptools import setup

setup(
    name='obia',
    version='1.0',
    packages=['obia'],
    description='',
    entry_points={
        'console_scripts': [
            'obia = obia.__main__:main'
        ]
    },
    install_requires=['pyfiglet']
)
