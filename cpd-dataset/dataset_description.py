"""
Module containing a class describing dataset and a builder for it.
"""

__copyright__ = "Copyright (c) 2024 Vladimir Kutuev"

__license__ = "SPDX-License-Identifier: MIT"

from io import StringIO
from itertools import accumulate


class DatasetDescription:
    """Contains dataset description:

    * sub-samples lengths;
    * sub-samples distributions;
    * sub-samples distributions parameters.

    Also can represent it in AsciiDoc format.
    """

    _name: str
    _samples_length: list[int]
    _samples_distributions: list[str]
    _samples_distributions_params: list[dict[str, str]]

    def __init__(
        self,
        name: str,
        samples_length: list[int],
        samples_distributions: list[str],
        samples_distributions_params: list[dict[str, str]],
    ) -> None:
        """
        Creates new DatasetDescription instance.

        :param name: Name for the sample.
        :param samples_length: List of sub-samples length.
        :param samples_distributions: List of sub-samples distributions.
        :param samples_distributions_params: List of sub-samples distributions parameters.
        """
        self._name = name
        self._samples_length = samples_length
        self._samples_distributions = samples_distributions
        self._samples_distributions_params = samples_distributions_params
        assert len(self._samples_length) == len(self._samples_distributions) == len(self._samples_distributions_params)

    @property
    def changepoints(self) -> list[int]:
        return list(accumulate(self._samples_length))[:-1]

    def __str__(self) -> str:
        sub_samples_len = len(self._samples_length)
        description = StringIO()
        description.write(f"= Sample {self._name}\n\n")
        description.write(f"Sample len:: {sub_samples_len}\n")
        description.write(f"Change points:: {self.changepoints}\n\n")
        description.write(f"== Distributions\n\n")
        for i in range(sub_samples_len):
            description.write(f"* {self._samples_distributions[i]}\n")
            for k, v in self._samples_distributions_params[i].items():
                description.write(f"** {k}:: {v}\n")

        return description.getvalue()


class DatasetDescriptionBuilder:
    """Builder for `DatasetDescription` instance."""

    _name: str | None
    _samples_length: list[int] | None
    _samples_distributions: list[str] | None
    _samples_distributions_params: list[dict[str, str]] | None

    def __init__(self):
        """Creates new DatasetDescriptionBuilder empty instance."""
        self._name = None
        self._samples_length = None
        self._samples_distributions = None
        self._samples_distributions_params = None

    def set_name(self, name: str) -> None:
        self._name = name

    def set_samples_lengths(self, samples_lengths: list[int]) -> None:
        self._samples_length = samples_lengths

    def set_samples_distributions(self, samples_distributions: list[str]) -> None:
        self._samples_distributions = samples_distributions

    def set_samples_distributions_params(self, samples_distributions_params: list[dict[str, str]]) -> None:
        self._samples_distributions_params = samples_distributions_params

    def build(self) -> DatasetDescription:
        assert self._name
        assert self._samples_length
        assert self._samples_distributions
        assert self._samples_distributions_params
        assert len(self._samples_length) == len(self._samples_distributions) == len(self._samples_distributions_params)
        return DatasetDescription(
            self._name, self._samples_length, self._samples_distributions, self._samples_distributions_params
        )
