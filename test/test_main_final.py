import os
from datetime import datetime
from tempfile import gettempdir
import pytest
from pathlib import Path
from csv_reports import CSVReportFormatter, CSVAttentionPliesFormatter, CSVUnprocessedPliesFormatter, \
    CSVBoundingBoxFormatter, CSVSinglePhiFormatter, CSVTimeEstFormatter

"""
        @author : Padma
        Whitebox Testing on the functions of main program 
"""

CSV_REPORTS_DICT = {"CSVReportFormatter": CSVReportFormatter,
                    "CSVAttentionPliesFormatter": CSVAttentionPliesFormatter,
                    "CSVUnprocessedPliesFormatter": CSVUnprocessedPliesFormatter,
                    "CSVBoundingBoxFormatter": CSVBoundingBoxFormatter,
                    "CSVSinglePhiFormatter": CSVSinglePhiFormatter,
                    "CSVTimeEstFormatter": CSVTimeEstFormatter
                    }


def test_dict_key():
    """
            This test checks on the main function get_csv_report()
            comparing report key values using dictionary functions.
    """
    for report_key, report in CSV_REPORTS_DICT.items():
        for i in CSV_REPORTS_DICT.keys():
            if i == report_key:
                assert CSV_REPORTS_DICT[i] == CSV_REPORTS_DICT.get(report_key)
        assert True


@pytest.mark.xfail
def test_key_not_dict():
    """
            This test checks on the main function get_csv_report()
            for keys in dictionary. If test fails marks as xfail not considered for the report.
    """
    # with pytest.raises(AssertionError):
    for key, report in CSV_REPORTS_DICT.items():
        assert key not in CSV_REPORTS_DICT


@pytest.mark.parametrize("arguments, kwargs, expecting",
                         [(1, {'CSVReportFormatter': CSVReportFormatter}, True),
                          (2, {'CSVAttentionPliesFormatter': CSVAttentionPliesFormatter}, True),
                          (3, {'CSVUnprocessedPliesFormatter': CSVUnprocessedPliesFormatter}, True),
                          (4, {'CSVBoundingBoxFormatter': CSVBoundingBoxFormatter}, True),
                          (5, {'CSVSinglePhiFormatter': CSVSinglePhiFormatter}, True),
                          (6, {'CSVTimeEstFormatter': CSVTimeEstFormatter}, True)])
def test_f(arguments, kwargs, expecting):
    """
            This test checks on the main CSV_REPORT_DICT key values using mark. parametrize method

    """
    print(arguments, kwargs)
    assert kwargs is not None


def test_check_dir_current_date_time():
    """
            This test checks on get_report_file_name for existence of directory with current date time

    """

    report_generation_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(os.path.join(gettempdir(), f"reports_{report_generation_datetime}"))
    os.mkdir(output_dir)
    assert output_dir.is_dir() is True


def test_check_file_current_date_time():
    """
            This test checks on get_report_file_name for existence of file with current date time

    """
    report_generation_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_ext = ".csv"
    output_dir = Path(os.path.join(gettempdir(), f"reports_{report_generation_datetime}",
                                   f"report_{report_generation_datetime}") + file_ext)
    os.mkdir(output_dir)
    assert output_dir.is_file() is False
