from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

import pandas as pd

from ..data.loader import DataSchema


@dataclass
class DataSource:
    """This class allows to abstract the data container"""

    _data: pd.DataFrame

    def get_data(self, cluster_name: str) -> DataSource:
        """Get data form a given cluster"""
        filtered_data = self._data.query("cluster in @cluster_name")
        return filtered_data
    
    @property
    def all_clusters(self) -> list[str]:
        """Get all clusters"""
        return self._data[DataSchema.CLUSTER_NAME].unique().tolist()
    
    @property
    def unique_clusters(self) -> list[str]:
        """Get unique cluster names"""
        return sorted(set(self.all_clusters))