from setuptools import setup, find_packages

setup(
    name="agile-demo",
    version="0.1",
    packages=find_packages(),
    extras_require={
        "dev": ["pytest", "flake8"],
    },
)
