# mypackage

[![PyPI - Version](https://img.shields.io/pypi/v/mypackage.svg)](https://pypi.org/project/mypackage)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/mypackage.svg)](https://pypi.org/project/mypackage)

-----

## Table of Contents

- [Description](#description)
- [Example](#example)
- [Installation](#installation)
- [License](#license)

## Description
`mypackage` provides tools for dataset analysis—such as computing correlations and survival rates—and corresponding visualizations. It primarily utilizes the "titanic" dataset from the seaborn library.

The package comprises two classes, each containing approximately 6–7 functions. The **Analyzer** class is designed for data analysis and can process any dataset, although one function is specifically optimized for the "titanic" dataset.

The **Visualizer** class is responsible for creating plots and visual representations of the analysis. Some functions in this class accept outputs from the Analyzer, while others can operate independently based on user-defined parameters.


## Example
First, instantiate the `Analyzer` class with your dataset:
'''analyzer = Analyzer(data)'''

Then, call the `chi_square_test` method by providing the two column names as parameters. For example, to test the relationship between `"pclass"` and `"survived"`, run:
```python
analyzer.chi_square_test(column1 = "pclass", column2 = "survived")
```

The function returns two pieces of information:
1.	A message indicating whether there is a statistically significant relationship between the two columns.
2.	A tuple containing:
    - chi2: The chi-square statistic.
    - p: The p-value.
    - v: The Cramér’s V value.

Example output:
```python
Ouptput:
There is a statistically significant relationship between pclass and survived
Out[13]: (102.88898875696056, 4.549251711298793e-23, 0.33981738800531175)
```

## Installation

```console
pip install mypackage
```

## License

`mypackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
