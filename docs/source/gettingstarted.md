 # Installation

### Supported operating systems

`pyscal_rdf` can be installed on Linux and Mac OS based systems. On Windows systems, it is recommended to use  [Windows subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install).

### Using a conda environment

We strongly recommend creating a conda environment for the installation. To see how you can install conda see [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/).

Once a conda distribution is available, the following steps will help set up an environment to use `pyscal_rdf`. First step is to clone the repository.

```
git clone https://github.com/pyscal/pyscal_rdf.git
```

After cloning, an environment can be created from the included file-

```
cd pyscal_rdf
conda env create -f environment.yml
```

This will install the necessary packages and create an environment called rdf. It can be activated by,

```
conda activate rdf
```

then, install `pyscal_rdf` using,

```
pip install .
```
 