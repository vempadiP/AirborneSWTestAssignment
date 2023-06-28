import os
from pathlib import Path
from tempfile import gettempdir


def test_time_est_files():

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

    fileext = "/reports_20230628_225727/report_20230628_225727bb.csv"
    my_file = Path(os.path.join(gettempdir()) + fileext)
    assert my_file.is_file()

    dir_ext = "/reports_20230628_225727"
    my_dir = Path(os.path.join(gettempdir()) + dir_ext)
    assert my_dir.is_dir()
    assert my_file.exists()

    print("File size empty", os.stat(my_file).st_size)


def test_report_empty_file():

    fileext = "/reports_20230628_215945/report_20230628_215945.csv"
    my_file = Path(os.path.join(gettempdir()) + fileext)
    assert my_file.is_file()

    fileext = "/reports_20230628_215945"
    # my_dir = Path(os.path.join(gettempdir()) + fileext)

    if os.stat(my_file).st_size == 0:
        assert False
    else:
        assert True
        print("File size empty", os.stat(my_file).st_size)



"""
a = os.path.getsize(my_file)
    print("FILE SIZE", a)
    b = os.fstat(a.fileno()).st_size
    b = os.fstat(my_file).st_size
    print("File size b", b)
"""