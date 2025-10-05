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
        "operations research",
        "optimization",
        "constraint programming",
        "solver",
        "CSP",
        "Python",
        "mathematical modeling",
        "combinatorial optimization",
        "decision support",
    ],
    description="Python client library for Qaekwy, a high-performance operational research solver.",
    long_description_content_type = "text/markdown",
    long_description=long_description,
    url="https://qaekwy.io",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
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
        'Issue Tracker': 'https://github.com/alex-87/qaekwy-python/issues',
        'Source': 'https://github.com/alex-87/qaekwy-python',
    },
    python_requires=">=3.12",
    install_requires=[
        "requests",
        "types_requests",
    ],
)
