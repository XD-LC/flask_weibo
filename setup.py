import io

from setuptools import find_packages, setup

with io.open('README.rst', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='flaskr',
    version='1.0.2',
    license='BSD',
    maintainer='Pallets team',
    maintainer_email='xdulichong@gmail.com',
    description='The basic blog app learned from FLASK',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)