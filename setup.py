from setuptools import setup, find_packages

with open('README.rst', encoding='UTF-8') as file:
    readme = file.read()

setup(
    name='pgbackup',
    version='0.1.0',
    description='Database backups locally or to AWS S3',
    author="JustFiesta",
    packages=find_packages('src'),
    package_dir={'': 'src'}
)