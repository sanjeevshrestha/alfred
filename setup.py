
from setuptools import setup, find_packages
import sys, os

setup(name='alfred',
    version='0.0.1',
    description="My Helper in Crime",
    long_description="My Helper in Crime",
    classifiers=[],
    keywords='',
    author='Sanjeev Shrestha',
    author_email='sanjeevshrestha2004@gmail.com',
    url='https://www.github.com/sanjeevshrestha/alfred',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ### Required to function
        'cement',
        ],
    setup_requires=[],
    entry_points="""
        [console_scripts]
        alfred = alfred.cli.main:main
    """,
    namespace_packages=[],
    )
