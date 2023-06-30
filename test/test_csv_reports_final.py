import os
from pathlib import Path
from tempfile import gettempdir

"""
        @author : Padma
        Whitebox Testing on the functions of csv_reports program 
"""


def test_time_est_files():
    """
               This test checks for temp directory and time_est csv files in the current path.
               The paths are hardcode and in future we need to parameterize it.

    """

    dir_ext = "/reports_20230628_220050"
    my_dir = Path(os.path.join(gettempdir()) + dir_ext)
    print("My Dir", my_dir)

    fileext = "/reports_20230628_220050/report_20230628_220050time_est.csv"
    my_file = Path(os.path.join(gettempdir()) + fileext)
    print("My file", my_file)
    assert my_dir.is_dir()
    assert my_file.is_file()
    assert my_file.exists()


def test_time_bb_files():
    """
            This test checks for the current directory and simple_bb csv files in the current path.
            Similar check can be followed for other csv files.
    """
    fileext = "/reports_20230628_225727/report_20230628_225727bb.csv"
    my_file = Path(os.path.join(gettempdir()) + fileext)
    assert my_file.is_file()

    fileext = "/reports_20230628_225727"
    my_dir = Path(os.path.join(gettempdir()) + fileext)
    assert my_dir.is_dir()
    assert my_file.exists()


def test_report_empty_file():
    """
                This test checks empty file report with file size
    """

    fileext = "/reports_20230628_215945/report_20230628_215945.csv"
    my_file = Path(os.path.join(gettempdir()) + fileext)
    assert my_file.is_file()
    if os.stat(my_file).st_size == 0:
        assert False
    else:
        assert True
        print("File size empty", os.stat(my_file).st_size)
