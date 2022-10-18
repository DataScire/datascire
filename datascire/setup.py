from setuptools import setup, find_packages


setup(
    name='DataScire',
    version='0.1',
    license='MIT',
    author="Carlos Acosta",
    author_email='development@datascire.com',
    packages=find_packages('datascire'),
    package_dir={'': 'datascire'},
    url='https://datascire@dev.azure.com/datascire/AzureRepos/_git/AzureRepos',
    keywords='DataScire Project',
    install_requires=[
          'pandas',
      ],

)