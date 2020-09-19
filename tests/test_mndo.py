
import pytest
from context import ppqm
from context import CONFIG
from ppqm import mndo, tasks, chembridge

MNDO_OPTIONS = {
    "scr": CONFIG["scr"]["scr"],
    "cmd": CONFIG["mndo"]["cmd"],
}


def test_optimize_water():

    # Get molecule
    smi = "O"
    molobj = tasks.generate_conformers(smi, max_conf=1, min_conf=1)

    # Get mndo calculator
    calc = mndo.MndoCalculator(**MNDO_OPTIONS)

    method = "PM3"

    # Optimize water
    properties = calc.optimize(
        molobj,
        return_copy=False,
        return_properties=True
    )

    water_atomization = properties["h"]

    assert pytest.approx(-224.11087077483552, rel=1e-2) == water_atomization

    return


def test_water_xyz():

    smi = "O"
    method = "PM3"

    # Get molecule
    molobj = tasks.generate_conformers("O", max_conf=1, min_conf=1)

    # Get XYZ
    atoms, coords, charge = chembridge.molobj_to_axyzc(molobj)

    # Get mndo calculator
    calc = mndo.MndoCalculator(cmd="mndo", scr="_test_dir_", method=method)

    # Optimize coords
    properties = calc.optimize_axyzc(atoms, coords, charge)
    properties = next(properties)

    water_atomization = properties["h"]

    assert pytest.approx(-224.11087077483552, rel=1e-2) == water_atomization


    return




