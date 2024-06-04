from setuptools import setup, find_packages

setup(
    name='serializer',
    version='2.0.0',
    description='Serialization/Deserialization with SQLite',
    long_description_content_type='text/markdown',
    author='Xatura',
    packages=find_packages(),
    install_requires=[
        'sqlite3',
    ],
)