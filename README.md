## Install
```
pip install brdocs-validation
```


## Supported docs and its formats

| Supports |                    Format                     |
|:--------:|:---------------------------------------------:|
|   CNPJ   | Without special chars or *12.345.678/9012-34* |
|   CPF    |   Without special chars or *123.456.789-01*   |

## Usage 

```python
from br_docs import CPF, CNPJ
from pydantic import BaseModel


class User(BaseModel): 
    name: str
    age: int
    cpf: CPF
    cnpj: CNPJ
```