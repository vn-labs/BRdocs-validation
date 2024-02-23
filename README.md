![Python 3.6](https://img.shields.io/badge/python-3.10-2334D058.svg)

## Install
```
pip install brdocs-validation
```


## Supported docs and its formats

| Supports |                     Format                      |
|:--------:|:-----------------------------------------------:|
|   CNPJ   | *12.345.678/9012-34* OR _Without special chars_ |
|   CPF    |   *123.456.789-01* OR _Without special chars_   |
|   CNH    |                  Only numbers                   |

## Usage 

```python
from br_docs import CPF, CNPJ, CNH
from pydantic import BaseModel


class User(BaseModel): 
    name: str
    age: int
    cpf: CPF
    cnpj: CNPJ
    cnh: CNH
```