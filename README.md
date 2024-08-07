# pybamm-cookiecutter

<!-- TODO: configure badges -->

<!-- [![Actions Status][actions-badge]][actions-link]
[![Documentation Status][rtd-badge]][rtd-link]

[![PyPI version][pypi-version]][pypi-link]
[![Conda-Forge][conda-badge]][conda-link]
[![PyPI platforms][pypi-platforms]][pypi-link]

[![GitHub Discussions][github-discussions-badge]][github-discussions-link]

[actions-badge]:            https://github.com/pybamm-team/pybamm-cookiecutter/workflows/CI/badge.svg
[actions-link]:             https://github.com/pybamm-team/pybamm-cookiecutter/actions
[conda-badge]:              https://img.shields.io/conda/vn/conda-forge/pybamm-cookiecutter
[conda-link]:               https://github.com/conda-forge/pybamm-cookiecutter-feedstock
[github-discussions-badge]: https://img.shields.io/static/v1?label=Discussions&message=Ask&color=blue&logo=github
[github-discussions-link]:  https://github.com/pybamm-team/pybamm-cookiecutter/discussions
[pypi-link]:                https://pypi.org/project/pybamm-cookiecutter/
[pypi-platforms]:           https://img.shields.io/pypi/pyversions/pybamm-cookiecutter
[pypi-version]:             https://img.shields.io/pypi/v/pybamm-cookiecutter
[rtd-badge]:                https://readthedocs.org/projects/pybamm-cookiecutter/badge/?version=latest
[rtd-link]:                 https://pybamm-cookiecutter.readthedocs.io/en/latest/?badge=latest -->

<!-- SPHINX-START -->
[![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](http://numfocus.org)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-red.json)](https://github.com/copier-org/copier)

This repository contains a `copier` template for battery modeling projects using PyBaMM, released under the [BSD-3-Clause license](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/LICENSE). Currently under active development.

## 📄 Using `pybamm-cookiecutter`

### Generating projects with `pybamm-cookiecutter` manually using copier

This template is not on PyPI yet, so it cannot be installed through `pip` until the first release. Meanwhile, it can be used by cloning this repository and using `copier` to generate a project with this template.

Install `copier` and `jinja2_time` extension using `pip`.
```bash
pip install copier jinja2-time
```
Generate a project from the `pybamm-cookiecutter` template.
**Note:** This requires an internet connection. You could manually clone the git repository and run the copy command, or just execute the copy command with the URL to the git repository.

```bash
copier copy https://github.com/pybamm-team/pybamm-cookiecutter.git name_of_your_project/ --trust
```

Copier will prompt you with various configurations and you may choose the ones that suit your use case.

**Note**: A `git` repository is automatically initialised when a project is created within a directory.

After generation, you can navigate to the generated project and run `nox -s generated-project-tests` to ensure if the project units are working as intended.

### Installing the `pybamm-cookiecutter` project

This refers to the project used for the development of this template. There are two ways to install this project: either through `nox` or `pip`. `nox` uses `uv pip` or `pip` internally, and in this case, creates a virtual environment for you to activate.
To install, navigate to the root directory of this repository and execute either of these commands:

`nox -s dev`
or
`pip install -e .[dev]`

To check if the project was successfully installed, import the project inside Python.

```python
import pybamm_cookiecutter

pybamm_cookiecutter.__version__
```

## 🛠️ Contributing to `pybamm-cookiecutter`

If you'd like to help us develop `pybamm-cookiecutter` by improving the template's features, writing documentation, or fixing embarrassing bugs, please have a look at these [guidelines](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/CONTRIBUTING.md).

## 📫 Get in touch

For any questions, comments, suggestions or bug reports, please see the
[contact page](https://www.pybamm.org/community).

## 📃 License

The `pybamm-cookiecutter` project is open source code. For more information about its license, see [LICENSE](https://github.com/pybamm-team/pybamm-cookiecutter/blob/main/LICENSE).

<!-- SPHINX-END -->
