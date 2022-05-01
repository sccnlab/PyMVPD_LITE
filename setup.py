from setuptools import setup, find_packages

with open('requirements.txt') as rf:
    requirements = rf.readlines()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="PyMVPD_LITE", 
    version="0.0.3",
    author="Mengting Fang",
    author_email="mtfang0707@gmail.com",
    description="A python package for multivariate pattern dependence",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    keywords=["fMRI", "MVPD", "machine learning", "connectivity"],
    url="https://github.com/sccnlab/PyMVPD_LITE",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(include=['mvpdlite', 'mvpdlite.*']),
    install_requires=requirements,
)
