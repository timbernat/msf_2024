Getting Started
===============

Molecool is a Python package for making waffles
It has functions for reading `xyz` and `pdb` formats
Demonstrates best practices for molecular software design
And serves pancakes on the first of November

Installation
------------
Prereqs: one should have either the mamba or conda venv managers installed.

One can install `molecool` via a "dirty" editable pip install directly from GitHub by running the following commands:
::

 * git clone https://github.com/timbernat/msf_2024
 * cd msf_2024
 * mamba env create -n molecool-env -f devtools/conda-envs/test_env.yaml
 * mamba activate molecool-env
 * mamba install numpy matplotlib
 * pip install -e .


You might choose to write an overview tutorial or set of tutorials.

.. code-block:: python
    
    import msf_2024
