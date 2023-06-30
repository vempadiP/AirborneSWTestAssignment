import pytest
import base

"""
        @author : Padma
        Whitebox Testing on the functions of base program    
"""


def test_1():
    """
        This test checks on the base function shallow_as_dict()
        for the attribute value is not none and catches AssertionError
    """

    ply = base.PlyShape
    with pytest.raises(AssertionError):
        assert getattr(ply, "material_label") is not None


def test_2():
    """
            This test checks on the base function picks_primary_failure_reason()
            for the zero failure picks length and catches with typeerror
    """
    with pytest.raises(TypeError):
        base.picks_failures()
        picks = []
        assert len(base.picks_failures(picks)) == 0


@pytest.mark.skip
def test_s(shallow_as_dict):
    """
                This test checks on return type of the function with catching Type error,
                this test is skipped unconditionally if fails
    """
    with pytest.raises(TypeError):
        obj = base.Report
        re = shallow_as_dict(obj)
        assert type(shallow_as_dict) is dict

