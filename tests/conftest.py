import pytest
from pathlib import Path

current_path = Path(__file__).parent


@pytest.fixture
def cnh_list():
    """
        1-69 line: https://web.archive.org/web/20240223023315/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2023|01_Janeiro|DODF%20022%2031-01-2023|&arquivo=DODF%20022%2031-01-2023%20INTEGRA.pdf
    """
    with open(str(current_path.joinpath('cnhs.txt'))) as cnhs:
        yield map(lambda x: x.strip('\n'), cnhs.readlines())


@pytest.fixture
def cpf_list():
    """
        1-60 line: https://web.archive.org/web/20240223042316/https://www.detran.ac.gov.br/wp-content/uploads/2022/06/Lista-de-Selecionados-CNH-Social.pdf
    """
    with open(str(current_path.joinpath('cpfs.txt'))) as cpfs:
        yield map(lambda x: x.strip('\n'), cpfs.readlines())
