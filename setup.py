from setuptools import find_packages, setup

__version__ = "1.5"

setup(
    name="genetic_algorithm",
    version=__version__,
    description="A genetic algorithm library",
    url="https://github.com/javidahmed64592/genetic-algorithm",
    author="Javid Ahmed",
    author_email="javidahmed@icloud.com",
    packages=find_packages(),
    install_requires=["numpy"],
)
