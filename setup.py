from setuptools import setup

setup(
    name='obia',
    version='1.0',
    packages=['obia'],
    url='',
    license='Creative Commons',
    author='nick',
    author_email='mcmasternick5572@gmail.com',
    description='',
    entry_points={
        'console_scripts': [
            'obia = obia.__main__:main'
        ]
    }
)
