"""Allow easy installation of this package.

"""

# Third-party imports
from setuptools import setup, find_packages


setup(
    name='sunset-repos',
    version='1.0.0',
    author='Daniel Eriksson',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click >= 7.0',
        'requests >= 2.22.0'
    ],
    setup_requires=[
        'flake8'
    ],
    entry_points={
        'console_scripts': [
            'sunset-repos=sunset_repos.cli:cli'
        ]
    }
)
