from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from ..data.loader import DataSchema


@dataclass
class DataSource:
    """This class allows to abstract the data container"""

    _data: pd.DataFrame

    def filter_data(
        self, cluster_name: str, probrange: tuple[float, float]
    ) -> DataSource:
        """Filter data by cluster name and probability range"""

        min_p, max_p = probrange[0], probrange[1]
        filtered_data = self._data.query(
            f"{DataSchema.CLUSTER_NAME} in @cluster_name and @min_p <= {DataSchema.PROBABILITY} <= @max_p"
        ).copy()
        return DataSource(filtered_data)

    def count_valid_rows_by_column(self, column_name: str) -> int:
        """Get the number of not nan rows in a given column"""
        return self._data[column_name].count()

    @property
    def all_clusters(self) -> list[str]:
        """Get all clusters"""
        return self._data[DataSchema.CLUSTER_NAME].unique().tolist()

    @property
    def unique_clusters(self) -> list[str]:
        """Get unique cluster names"""
        return sorted(set(self.all_clusters))

    @property
    def row_count(self) -> int:
        return self._data.shape[0]

    @property
    def get_data(self) -> pd.DataFrame:
        return self._data
