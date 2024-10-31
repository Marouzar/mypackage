from setuptools import setup, find_packages
setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('Readme.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<username>/<package-name>',
    author='<Marou>',
    author_email='<marouzar@gmail.com>'
)