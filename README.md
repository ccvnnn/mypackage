# mypackage

[![PyPI - Version](https://img.shields.io/pypi/v/mypackage.svg)](https://pypi.org/project/mypackage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypackage.svg)](https://pypi.org/project/mypackage)

-----

## Table of Contents

- [Description](#description)
- [Installation](#installation)
- [License](#license)

## Description
`mypackage` provides tools for dataset analysis—such as computing correlations and survival rates—and corresponding visualizations. It primarily utilizes the "titanic" dataset from the seaborn library.

The package comprises two classes, each containing approximately 6–7 functions. The **Analyzer** class is designed for data analysis and can process any dataset, although one function is specifically optimized for the "titanic" dataset.

The **Visualizer** class is responsible for creating plots and visual representations of the analysis. Some functions in this class accept outputs from the Analyzer, while others can operate independently based on user-defined parameters.

## Installation

```console
pip install mypackage
```

## License

`mypackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
