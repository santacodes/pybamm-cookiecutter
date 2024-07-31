import pytest
import {{ cookiecutter.__project_slug }}
import importlib.util
import sys
from pathlib import Path


def test_parameter_sets_entry_points():
    """Test if the parameter_sets via entry points are loaded correctly."""

    entry_points = list({{ cookiecutter.__project_slug }}.parameter_sets)
    parameter_sets = Path("src/{{ cookiecutter.__project_slug }}/parameters/input/").glob("*.py")
    # Making a list of parameter sets in the parameters/input directory
    parameter_sets = [x.stem for x in parameter_sets]

    assert parameter_sets == entry_points, "Entry points missing either in pyproject.toml or in the input directory"


def test_parameter_sets_entry_point_load():
    """Testing if the values get loaded via parameter entry points and are equal when loaded through entry points"""
    # Loading parameter_sets through entry points
    parameters = {{ cookiecutter.__project_slug }}.parameter_sets['Chen2020']
    # Loading parameter sets through the source file by dynamically loading Chen2020.py as a module
    spec = importlib.util.spec_from_file_location("Chen2020mod", "src/{{ cookiecutter.__project_slug }}/parameters/input/Chen2020.py")
    chen_module = importlib.util.module_from_spec(spec)
    sys.modules["Chen2020mod"] = chen_module
    spec.loader.exec_module(chen_module)
    parameters_from_file = chen_module.get_parameter_values()
    assert parameters.keys() == parameters_from_file.keys(), f"The keys in the module and local input file are not the same, expected {parameters.keys}, got {parameters_from_file.keys()}"

def test_model_entry_points():
    """Test if the models via entry points are loaded correctly."""

    entry_points = list({{ cookiecutter.__project_slug }}.models)
    models = Path("src/{{ cookiecutter.__project_slug }}/models/input/").glob("*.py")
    # Making a list Parameter sets in the parameters/input directory
    models = [x.stem for x in models]

    assert models == entry_points, "Entry points missing either in pyproject.toml or in the input directory"


def test_model_entry_point_load():
    """Testing if the model gets initialised and returned."""
    # Loading parameter_sets through entry points
    model_instance = {{ cookiecutter.__project_slug }}.Model("SPM")
    assert model_instance is not None
