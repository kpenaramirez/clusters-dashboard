import inspect
from functools import partial, reduce
from typing import Callable

import pandas as pd

Preprocessor = Callable[[pd.DataFrame], pd.DataFrame]


class DataSchema:
    CLUSTER_NAME = "cluster"
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
    J_K = "mj-mk"


def compose(*functions: Preprocessor) -> Preprocessor:
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def create_jk_color_index(df: pd.DataFrame) -> pd.DataFrame:
    df[DataSchema.J_K] = df[DataSchema.MJ] - df[DataSchema.MK]
    return df


def load_cluster_data(path: str) -> pd.DataFrame:
    """ Load data from the CSV file """

    data = pd.read_csv(
        path,
        dtype={
            DataSchema.CLUSTER_NAME: str,

        }
    )

    preprocessor = compose(
        create_jk_color_index,
    )
    
    return preprocessor(data)