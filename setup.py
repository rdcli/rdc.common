from setuptools import setup, find_packages
from rdc.common import __version__

# Human version
version = '.'.join(map(str, __version__))

# Read README file
with open('README.rst') as readme:
    long_description = readme.read()

# Parse classifiers
with open('classifiers.txt') as f:
    classifiers = filter(None, map(lambda s: s.strip(), f.read().split('\n')))

# Parse requirements
with open('requirements.txt') as f:
    install_requires = []
    for requirement in map(lambda s: s.strip(), f.read().split('\n')):
        _pound_pos = requirement.find('#')
        if _pound_pos != -1:
            requirement = requirement[0:_pound_pos].strip()
        if len(requirement):
            install_requires.append(requirement)

setup(
    name='rdc.common',
    namespace_packages = ['rdc'],
    version=version,
    description="Common tools",
    long_description=long_description,
    classifiers=classifiers,
    author='Romain Dorgueil',
    author_email='romain@dorgueil.net',
    url='http://common.rdc.li/',
    download_url='https://github.com/rdcli/rdc.common/tarball/' + version,
    license='Apache License, Version 2.0',
    packages=find_packages(exclude=['ez_setup', 'example', 'test']),
    include_package_data=True,
    install_requires=install_requires,
)
