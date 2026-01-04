""" Installation """

from setuptools import setup
import qaekwy.core as core

with open("README.md", "r", encoding="UTF-8") as fh:
    long_description = fh.read()


setup(
    name="qaekwy",
    version=core.__version__,
    license=core.__license__,
    author=core.__author__,
    author_email=core.__author_email__,
    keywords=[
        "optimization",
        "constraint programming",
        "combinatorial optimization",
        "operations research",
        "constraint satisfaction",
        "constraint solver",
        "solver",
        "CSP",
        "optimization library",
        "optimization framework",
        "mathematical optimization",
        "discrete optimization",
        "optimization modeling",
        "constraint modeling",
        "declarative programming",
        "modeling language",
        "DSL",
        "define-and-solve",
        "scheduling",
        "routing",
        "planning",
        "resource allocation",
        "assignment",
        "decision support",
        "open source",
        "Python",
    ],
    description="Qaekwy, a modern, open-source Python framework for declarative constraint programming and combinatorial optimization",
    long_description_content_type = "text/markdown",
    long_description=long_description,
    url="https://qaekwy.io",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Scientific/Engineering :: Optimization",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=[
        "qaekwy",
    ],
    project_urls={
        'Homepage': 'https://qaekwy.io',
        'Documentation': 'https://docs.qaekwy.io',
        'Issue Tracker': 'https://github.com/alex-87/qaekwy-python/issues',
        'Source': 'https://github.com/alex-87/qaekwy-python',
    },
    python_requires=">=3.9",
    install_requires=[
        "requests",
        "types_requests",
    ],
)
