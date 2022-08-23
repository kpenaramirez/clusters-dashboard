import inspect
import pandas as pd


class DataSchema:
    CLUSTER = "cluster"
    RA = "ra"
    DEC = "dec"
    PMRA = "pmra"
    EPMRA = "epmra"
    PMDEC = "pmdec"
    EPMDEC = "epmdec"
    PLX = "plx"
    MZ = "mz"
    EZ = "ez"
    MY = "my"
    EY = "ey"
    MJ = "mj"
    EJ = "ej"
    MH = "mh"
    EH = "eh"
    MK = "mk"
    PROBABILITY = "probability"


def load_cluster_data(path: str) -> pd.DataFrame:
    """ Load the data from the CSV file """
    
    # check all columns/attributes defined in DataSchema are present in the csv file
    attributes = inspect.getmembers(DataSchema, lambda x: not(inspect.isroutine(x)))

    data = pd.read_csv(
        path,
        usecols=[x[1] for x in attributes if not(x[0].startswith('__') and x[0].endswith('__'))]
    )
    
    return data