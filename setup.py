from setuptools import setup, find_packages


with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pyscal_rdf_gui',
    version='0.0.4',
    author='Abril Azocar Guzman, Sarath Menon',
    author_email='sarath.menon@pyscal.org',
    description='Visual components for ontology based structural manipulation and quering',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(include=['pyscal_rdf_gui', 'pyscal_rdf_gui.*']),
    zip_safe=False,
    download_url = 'https://github.com/pyscal/pyscal_rdf_gui',
    url = 'https://pyscal.org',
    install_requires=['pyscal3', 'pyscal-rdf'],
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    include_package_data=True,
)
