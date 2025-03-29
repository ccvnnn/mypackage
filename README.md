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
We give the `analyzer` variable our class with the data
'''analyzer = Analyzer(data)'''

Than we call our `chi_square_test` function which takes two columns as parameters
'''analyzer.chi_square_test(column1 = "pclass", column2 = "survived")'''

The output displays: first, if there is a significant relationship between the two given columns and second, the chi2, p and v values.
'''
Ouptput:
There is a statistically significant relationship between pclass and survived
Out[13]: (102.88898875696056, 4.549251711298793e-23, 0.33981738800531175)

'''

## Installation

```console
pip install mypackage
```

## License

`mypackage` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
