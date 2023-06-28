import json
from dataclasses import fields
from os import path
from typing import List
import pytest

from src import base
from data import DATA_MODULE_NAME
from data.loader import ReportEncoder
import importlib_resources
from src.main import get_data_file

"""
#@pytest.fixture()
def get_report() -> Report:
    file_name = "test.json"
    with importlib_resources.files(DATA_MODULE_NAME).joinpath(file_name).open("r") as f:
        return json.load(f, object_hook=ReportEncoder.decode_special)
"""


@pytest.fixture()
def get_example_file_paths() -> List[str]:
    result = []
    for item in importlib_resources.files(DATA_MODULE_NAME).iterdir():
        if item.is_file():
            (_, ext) = path.splitext(item.name)
            if ext == ".json":
                result.append(item.name)
    return result


def test_trial_jsonext(get_example_file_paths):
    # print("Padma", get_example_file_paths[0])
    for i in range(9):
        print("Padma", get_example_file_paths[i])
        assert get_example_file_paths[i] == "test.json"
    # assert get_example_file_paths[0] == "test.json"


def test_trial1():
    assert True


def test_trial2():
    # change the condition of chosen_file...use something to test for Assert in
    data_file = get_data_file()
    chosen_file = "test.json"
    print("padma")
    assert chosen_file in get_data_file()


def test_get_attr_trial3():
    report = base.Report()
    print("PADMA TEST FOR GET ATTRIBUTES")
    print(dict((f.name, getattr(report, f.name)) for f in fields(report)))
    print(dict((f.name, getattr(report, f.name)) for f in fields(report)).items())


def test_get_attr2_trial3():
    print("PADMA TEST FOR GET ATTRIBUTES to the 2nd level ")
    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f:
        dct_var = json.load(f, object_hook=ReportEncoder.decode_special)
    print("PADMA TEST for OBJECT_HOOK dct level ")
    print(dct_var)
    print("**KEYWORD ARGUMENTS**")
    # print(Report(**dct[ReportEncoder._REPORT_KEY]))
    return

"""
def test_trial5():
    report = base.Report()
    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test.json").open("r") as f:
        json.load(f, object_hook=ReportEncoder.decode_special)
        print("PADMA OBJECT_HOOK", f)
"""

def test_trial6():
    report = base.Report()
    with importlib_resources.files(DATA_MODULE_NAME).joinpath("test5.xls").open("w") as f:
        json.dump(report, f, cls=ReportEncoder)
        print("PADMA", f)


"""
    csv_report = get_csv_report()
    print("AJAY 123")
    print(csv_report(get_report(data_file)))  # ajay
    print("sjsjs")
    rerport_file_name_prefix = get_report_file_name()
    print("Padma-", report_file_name_prefix)
    report_file_name = csv_report(get_report(data_file)).generate(report_file_name_prefix)
    print("Ajay-")
    print(f"Report {report_file_name} generated, Ctrl-C to stop the program")
    print("PADMA IN THE MAIN")
    assert True
"""

"""
def test_k_dic():
    _PLY_SHAPE_KEY = "__ply_shape__"
    _PLY_RESULT_KEY = "__ply_result__"
    _PICK_RESULT_KEY = "__pick_result__"
    _POLYGON_KEY = "__polygon__"
    _REPORT_KEY = "__report__"

    dct = []
    # assert decode_special[0] == Report(**dct[ReportEncoder._REPORT_KEY])
    print("Padma test for dct")
    # print(Report(**dct[_REPORT_KEY]))
    print(decode_special.items[0])
    assert decode_special.items[0] == _REPORT_KEY




def test_json_ext(get_example_file_paths):
    # print("Padma", get_example_file_paths[0])
    for i in range(9):
        print("Padma", get_example_file_paths[i])
        assert get_example_file_paths[i] == "test.json"
    # assert get_example_file_paths[0] == "test.json"

    #  @pytest.mark.parametrize(dt: Dict)

"""
"""
def test_k_dic(get_report):
    _PLY_SHAPE_KEY = "__ply_shape__"
    _PLY_RESULT_KEY = "__ply_result__"
    _PICK_RESULT_KEY = "__pick_result__"
    _POLYGON_KEY = "__polygon__"
    _REPORT_KEY = "__report__"

    # assert decode_special[0] == Report(**dct[ReportEncoder._REPORT_KEY])
    print("Padma test for dct")
    # print(Report(**dct[_REPORT_KEY]))
    assert isinstance(decode_special) == _REPORT_KEY


# @pytest.mark.parametrize('key, value')
def test_valid_trial(decode_special, dct=None):
    assert decode_special[0] == Report(**dct[ReportEncoder._REPORT_KEY])
    print(Report(**dct[ReportEncoder._REPORT_KEY]))

    rep = "_report_key"

    if rep == "_report_key":
        print("Valid key!")
    else:
        print("Invalid key! ")
        assert True
        print("ajay")


   #  print(Report(**dt[ReportEncoder._REPORT_KEY]))
   #  print(Report(**dt[ReportEncoder._REPORT_KEY]))

"""
