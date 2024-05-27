"""
Module containing classes describing distributions for dataset generation.
"""

__copyright__ = "Copyright (c) 2024 Vladimir Kutuev"

__license__ = "SPDX-License-Identifier: MIT"

from enum import Enum
from typing import Final, Protocol


class Distributions(Enum):
    NORMAL = "normal"


class Distribution(Protocol):
    """
    An interface for all distributions.
    Allows to create instance with name and params dictionary.
    """

    @property
    def name(self) -> str:
        """
        :return: Name of the distribution.
        """
        return ""

    @property
    def params(self) -> dict[str, str]:
        """
        :return: Parameters of the distribution.
        """
        return {}

    @staticmethod
    def from_str(name: str, params: dict[str, str]) -> "Distribution":
        match name:
            case Distributions.NORMAL.value:
                return NormalDistribution.from_params(params)


class NormalDistribution(Distribution):
    """
    Description for the normal distribution with mean and variance parameters.
    """

    MEAN_KEY: Final[str] = "mean"
    VAR_KEY: Final[str] = "variance"

    mean: float
    variance: float

    def __init__(self, mean=0.0, var=1.0):
        self.mean = mean
        self.variance = var

    @property
    def name(self) -> str:
        return Distributions.NORMAL.value

    @property
    def params(self) -> dict[str, str]:
        return {
            NormalDistribution.MEAN_KEY: str(self.mean),
            NormalDistribution.VAR_KEY: str(self.variance),
        }

    @staticmethod
    def from_params(params: dict[str, str]) -> "NormalDistribution":
        if len(params) != 2:
            raise ValueError(
                "Normal distribution must have 2 parameters: "
                + f"{NormalDistribution.MEAN_KEY}, {NormalDistribution.VAR_KEY}"
            )
        mean: float = float(params[NormalDistribution.MEAN_KEY])
        var: float = float(params[NormalDistribution.VAR_KEY])
        return NormalDistribution(mean, var)
