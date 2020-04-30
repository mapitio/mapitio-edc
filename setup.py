# -*- coding: utf-8 -*-
import os

from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), "README.rst")) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as f:
    VERSION = f.read().strip()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="mapitio-edc",
    version=VERSION,
    author=u"Erik van Widenfelt",
    author_email="ew2789@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    url="https://github.com/mapitio/mapitio-edc",
    license="GPL license, see LICENSE",
    description="Retrospective HIV Cohort for Diabetes Research",
    long_description=README,
    zip_safe=False,
    keywords="django mapitio diabetes EDC",
    install_requires=[
        "boto3",
        "django-environ",
        "django-redis",
        "django-storages",
        "gunicorn",
        "python-memcached",
        "sentry_sdk",
        "celery",
        "django-celery-beat",
        "django-celery-results",
    ],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 3.0",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
    python_requires=">=3.7",
)
