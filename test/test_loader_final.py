from base import Report
from data import DATA_MODULE_NAME
from data.loader import ReportEncoder
import json
from os import path
from typing import List
import importlib_resources
import pytest

"""
        @author : Padma
        Whitebox Testing on the functions of loader program 
"""


def test_loader1():
    pass


@pytest.fixture()
def get_example_file_paths() -> List[str]:
    result = []
    for item in importlib_resources.files(DATA_MODULE_NAME).iterdir():

        if item.is_file():
            (_, ext) = path.splitext(item.name)
            if ext == ".json":
                result.append(item.name)
    return result


def test_check_picked_files_json_only(get_example_file_paths):
    """
            This test validates on the loader program on function get_example_file_paths() using fixtures
            for only .json files from the given path.
    """
    for i in range(len(get_example_file_paths)):
        [_, ext] = path.splitext(get_example_file_paths[i])
        assert ext == ".json"


def test_chosen_file(get_example_file_paths):
    """
            This test validates if the chosen file exists in the current path or not.
    """

    for item in range(len(get_example_file_paths)):
        file_list = get_example_file_paths
        chosen_file = "test.json"
        assert chosen_file in file_list


def test_file_type():
    """
            This test verify for report_key exists in the json input file.
    """

    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f:
        dct = json.load(f, object_hook=ReportEncoder.decode_special)
        assert type(dct) == Report


def test_report_key():
    """
                This test verify for report_key exists in the json input file.
    """
    _PLY_SHAPE_KEY = "__ply_shape__"
    _PLY_RESULT_KEY = "__ply_result__"
    _PICK_RESULT_KEY = "__pick_result__"
    _POLYGON_KEY = "__polygon__"
    _REPORT_KEY = "__report__"

    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f:
        dct = json.load(f, object_hook=ReportEncoder.decode_special)

    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f1:
        f_content = f1.read()
        print(f_content)
    assert _REPORT_KEY in f_content



