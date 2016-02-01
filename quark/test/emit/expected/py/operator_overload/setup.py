# Setup file for package operator_overload

from setuptools import setup

setup(name="operator_overload",
      version="0.0.1",
      install_requires=["datawire-quark-core==0.4.2", "builtin==0.0.1"],
      py_modules=['operator_overload'],
      packages=['operator_overload_md'])
