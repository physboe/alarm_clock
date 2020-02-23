import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="alarm-clock-physbo",
    version="0.0.1",
    author="André Böni",
    author_email="boeni10@gmail.com",
    description="Alarm Clock framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License ::  GNU GPLv3 ",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
