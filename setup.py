from setuptools import setup, find_packages
setup(
    name='my_package',
    version='1.0.0',
    author='Sahithi',
    description='This is my first package',
    packages=find_packages(),
    install_requires=[
        # List any dependencies your package needs to run
        'dependency1',
        'dependency2',
    ],
)
