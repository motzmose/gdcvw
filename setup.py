from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in gdc/__init__.py
from gdc import __version__ as version

setup(
	name="gdc",
	version=version,
	description="Girls Digital Camps",
	author="didaktik-aktuell e.V.",
	author_email="kaimann@didaktik-aktuell.de",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
