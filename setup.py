"""Do setup for uploading to pypi
"""
import setuptools

with open("README.md", "r") as readme:
	long_description = readme.read()

setuptools.setup(
	name="catpandoc",
	version="2020.1",
	author="FredHappyface",
	description="Cat multiple document files to the terminal",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/FHPythonUtils/CatPandoc",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"Operating System :: OS Independent",
	],
	entry_points={
        'console_scripts': [
            'catpandoc=catpandoc.application:cli',
        ],
    },
	python_requires='>=3.0',
)
