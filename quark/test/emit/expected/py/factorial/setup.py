# Setup file for package factorial

from setuptools import setup

setup(name="factorial",
      version="0.0.1",
      install_requires=["datawire-quark-core==0.4.2", "builtin==0.0.1"],
      py_modules=['factorial'],
      packages=['factorial_md'])
