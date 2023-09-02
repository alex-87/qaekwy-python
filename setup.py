""" Installation """

from setuptools import setup
import qaekwy

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()


setup(
    name="qaekwy",
    version=qaekwy.__version__,
    license=qaekwy.__license__,
    author=qaekwy.__author__,
    author_email=qaekwy.__author_email__,
    keywords=[
        "operational research",
        "optimization",
        "CSP",
        "solver",
        "constraint",
        "constraint programming",
    ],
    description="Python Client library for Qaekwy Operational Research Solver",
    long_description_content_type = "text/markdown",
    long_description=long_description,
    url="https://qaekwy.io",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: European Union Public Licence 1.2 (EUPL 1.2)",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
    ],
    packages=[
        "qaekwy",
        "qaekwy.model",
        "qaekwy.model.variable",
        "qaekwy.model.constraint",
        "qaekwy.exception",
    ],
    project_urls={
        'Homepage': 'https://qaekwy.io',
        'Documentation': 'https://docs.qaekwy.io',
        'Issues tracker': 'https://github.com/alex-87/qaekwy-python/issues',
        'Github': 'https://github.com/alex-87/qaekwy-python',
    },
)
