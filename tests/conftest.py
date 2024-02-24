from typing import Iterator
import pytest
from pathlib import Path

current_path = Path(__file__).parent


def open_valid_docs(path: str) -> Iterator[str]:
    with open(str(current_path.joinpath(path))) as f:
        return map(lambda x: x.strip('\n'), f.readlines())


@pytest.fixture
def cnh_list():
    """
        1-69 line: https://web.archive.org/web/20240223023315/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2023|01_Janeiro|DODF%20022%2031-01-2023|&arquivo=DODF%20022%2031-01-2023%20INTEGRA.pdf
        70-100 line: https://web.archive.org/web/20240224034619/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2021%7C11_Novembro%7CDODF%20208%2008-11-2021%7C&arquivo=DODF%20208%2008-11-2021%20INTEGRA.pdf
        101-125 line: https://web.archive.org/web/20240224035353/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2021%7C12_Dezembro%7CDODF%20232%2014-12-2021%7C&arquivo=DODF%20232%2014-12-2021%20INTEGRA.pdf
    """
    return open_valid_docs('cnhs.txt')


@pytest.fixture
def cpf_list():
    """
        1-60 line: https://web.archive.org/web/20240223042316/https://www.detran.ac.gov.br/wp-content/uploads/2022/06/Lista-de-Selecionados-CNH-Social.pdf
    """
    return open_valid_docs('cpfs.txt')


@pytest.fixture
def cnpj_list():
    """
        1-88 line: https://web.archive.org/web/20240223150643/https://www.detran.df.gov.br/wp-content/uploads/2021/09/Empresas-CNH-Social.pdf
    """
    return open_valid_docs('cnpj.txt')
