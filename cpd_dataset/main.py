import argparse
from pathlib import Path

from .config_parser import ConfigParser
from .generator import Generators, DatasetGenerator
from .saver import DatasetSaver


def main():
    parser = argparse.ArgumentParser(description="Change Point Detection problem dataset generator")
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to configuration YAML file",
    )
    parser.add_argument(
        "--out-dir",
        type=str,
        required=True,
        help="Path to output directory",
    )
    parser.add_argument(
        "--generator",
        type=Generators,
        default=Generators.SCIPY,
        choices=list(Generators),
        help="Sample generator backend",
    )
    parser.add_argument(
        "--replace", action="store_true", help="Whether generated samples should be saved if they already exist."
    )

    args = parser.parse_args()
    cp = ConfigParser(Path(args.config))
    dg = DatasetGenerator.get_generator(args.generator)
    sv = DatasetSaver(Path(args.out_dir), args.replace)
    generate_dataset(cp, dg, sv)


def generate_dataset(parser: ConfigParser, generator: DatasetGenerator, saver: DatasetSaver) -> None:
    """
    Generate dataset and save it.

    :param parser: Configuration file parser.
    :param generator: Dataset generator.
    :param saver: Dataset saver.
    """
    for descr in parser:
        sample = generator.generate_sample(descr.distributions, descr.length)
        saver.save_sample(sample, descr)


if __name__ == "__main__":
    raise SystemExit(main())
