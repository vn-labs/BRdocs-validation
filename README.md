## Supported docs and its formats

| Supports |                    Format                     |
|:--------:|:---------------------------------------------:|
|   CNPJ   |   Without special chars or *$$$.$$$.$$$-$$*   |
|   CPF    | Without special chars or *$$.$$$.$$$/$$$$-$$* |

## Usage 

``` 
from br_docs import CPF, CNPJ
from pydantic import BaseModel


class User(BaseModel): 
    name: str
    age: int
    cpf: CPF
    cnpj: CNPJ
```