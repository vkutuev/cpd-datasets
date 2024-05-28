[![MIT License][license-shield]][license-url]

[license-shield]: https://img.shields.io/github/license/vkutuev/cpd-datasets.svg?style=for-the-badge&color=blue
[license-url]: LICENSE.md

# CPD datasets

## Dependencies installation

```shell
poetry install --without dev
```

## Usage

Print verbose usage

```shell
python -m cpd_dataset -h
```

Generate dataset with config and save it to directory

```shell
python -m cpd_dataset --config=conf/default.yml --out-dir=dataset
```

## Development

### Development dependencies installation

```shell
poetry install --with dev
```

### Pre-commit  hooks

Install pre-commit hooks

```shell
pre-commit install
```

Run manually

```shell
pre-commit run --all-files --color always --verbose
```
