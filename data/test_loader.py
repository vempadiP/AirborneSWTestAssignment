from src import base
from data import DATA_MODULE_NAME
from data.loader import ReportEncoder
import json
from os import path
from typing import List
import importlib_resources
import pytest


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


def test_check_picked_files_json_only_loader1(get_example_file_paths):
    for i in range(len(get_example_file_paths)):
        print(i)
        print("Padma", get_example_file_paths[i])
        [_, ext] = path.splitext(get_example_file_paths[i])
        assert ext == ".json"


def test_chosen_file_loader2(get_example_file_paths):
    # change the condition of chosen_file...use something to test for Assert in

    for item in range(len(get_example_file_paths)):
        file_list = get_example_file_paths
        chosen_file = "test.json"
        print("Padma File List", file_list)
        assert chosen_file in file_list


def test_loader3():
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


def test_loader4():

    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f:
        dct = json.load(f, object_hook=ReportEncoder.decode_special)
    assert type(dct) == base.Report
