from setuptools import setup
setup(
    name='conlog',
    packages=['conlog'],
    version='0.3',
    install_requires=['PyYAML>=3.12', 'bitmath>=1.3.1.2', 'six>=1.10.0'],
    description='Anti-Boilerplate Console Logging Module for Python',
    long_description=open('README.rst').read(),
    author='Ryan Miller',
    author_email='ryan@devopsmachine.com',
    license='MIT',
    url='https://github.com/RyanMillerC/conlog',
    download_url='https://github.com/RyanMillerC/conlog/archive/0.3.tar.gz',
    keywords=['logging', 'yaml'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: System :: Logging'
    ]
)
