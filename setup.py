import setuptools

with open("README.md", "r") as rm:
    long_description = rm.read()

setuptools.setup(
    name="jetmath",
    version="1.0",
    author="Bill Kudo",
    author_email="bluesky42624@gmail.com",
    description="An extensive math library focused on machine learning",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Bill13579/jetmath",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ),
)
