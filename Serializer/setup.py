from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Serializer',
    version='2.0.0',
    description='serialization/Deserialization/Errors',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Xatura',
    packages=find_packages(),
    install_requires=[
        'jsonschema',
    ],
)