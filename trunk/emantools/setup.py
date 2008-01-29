from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='emantools',
      version=version,
      description="Eman Tools",
      long_description="""\
EmanTools""",
      classifiers=[], # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      keywords='Utilities Tools',
      author='Emanuel G. Calso',
      author_email='bloodpet@gmail.com',
      url='http://eman-misc.googlecode.com/',
      license='Python License',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
