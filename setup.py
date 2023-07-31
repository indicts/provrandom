from setuptools import setup

setup(
    name="provrandom",
    version="0.0.1",
    description="Prove the outcome of randomness!",
    long_description="""
provrandom - Prove the outcome of randomness!
===================================================================

`provrandom` is a Python package that provides a fair random number generator designed for applications that would be able to use fair randomness. The package allows you to generate random numbers and information in a way that can be verified by both the server and the client, ensuring fairness and transparency in the process.

Features
--------

- Generate provably fair random numbers based on server seeds, client seeds, and nonces.
- Easy-to-use interface for obtaining random numbers and related information.
- Transparent and verifiable randomness to guarantee fairness in any applications.
- Flexible customization of seeds and nonces for a wide range of use cases.

Installation
------------

You can install `provrandom` using pip:

```bash
pip install provrandom
```

**Usage:**
```python
from provrandom import Random

# Create an instance of the Random class
random_instance = Random()

# Example usage of methods:
print("Random information:", random_instance.random_information)
print("Random hash:", random_instance._hash())
print("Random number between 10 and 20:", random_instance.number(10, 20))
print("Random float between 1.0 and 5.0:", random_instance._float(1.0, 5.0))
print("Random string of length 8:", random_instance.string(8))

# Example usage of _random_container method to generate a list of random numbers
random_numbers_list = random_instance._random_container(list, 5, 0, 100)
print("Random numbers list:", random_numbers_list)

```
""",
    author="hevnd",
    packages=["provrandom"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
