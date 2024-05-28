"""
Module containing classes for dataset generation.
"""

__copyright__ = "Copyright (c) 2024 Vladimir Kutuev"

__license__ = "SPDX-License-Identifier: MIT"

from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar, Generic

import numpy as np

from .distributions import Distribution, ScipyDistribution


class Generators(Enum):
    SCIPY = "scipy"

    def __str__(self) -> str:
        return self.value


DT = TypeVar("DT", bound=Distribution)


class DatasetGenerator(Generic[DT], ABC):
    """
    An interface for dataset generators using different backends (e.g. SciPy or Numpy)
    to create a sample with a given distributions and lengths.
    """

    @abstractmethod
    def generate_sample(self, distributions: list[DT], lengths: list[int]) -> np.ndarray:
        """
        Creates a sample consists of subsamples with given `distributions` and `lengths`.

        :param distributions: List of distributions for subsamples.
        :param lengths: List of subsamples lengths.
        :return: Created sample.
        """
        raise NotImplementedError()

    @staticmethod
    def get_generator(generator_backend: Generators) -> "DatasetGenerator":
        match generator_backend:
            case Generators.SCIPY:
                return ScipyDatasetGenerator()
            case _:
                raise ValueError("Unknown generator")


DST = TypeVar("DST", bound=ScipyDistribution)


class ScipyDatasetGenerator(DatasetGenerator):
    """
    Dataset generator using SciPy to create samples.
    """

    def generate_sample(self, distributions: list[DST], lengths: list[int]) -> np.ndarray:
        d: DST
        l: int
        return np.concatenate([d.scipy_sample(l) for d, l in zip(distributions, lengths)])
