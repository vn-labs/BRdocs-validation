from typing import Iterator
import pytest
from pathlib import Path

current_path = Path(__file__).parent


def open_docs(path: str) -> Iterator[str]:
    with open(str(current_path.joinpath(path))) as f:
        return map(lambda x: x.strip('\n'), f.readlines())


@pytest.fixture
def cnh_list():
    """
    1-69 line: https://web.archive.org/web/20240223023315/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2023|01_Janeiro|DODF%20022%2031-01-2023|&arquivo=DODF%20022%2031-01-2023%20INTEGRA.pdf
    70-100 line: https://web.archive.org/web/20240224034619/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2021%7C11_Novembro%7CDODF%20208%2008-11-2021%7C&arquivo=DODF%20208%2008-11-2021%20INTEGRA.pdf
    101-125 line: https://web.archive.org/web/20240224035353/https://dodf.df.gov.br/index/visualizar-arquivo/?pasta=2021%7C12_Dezembro%7CDODF%20232%2014-12-2021%7C&arquivo=DODF%20232%2014-12-2021%20INTEGRA.pdf
    """
    return open_docs('cnhs.txt')


@pytest.fixture
def cpf_list():
    """
    1-60 line: https://web.archive.org/web/20240223042316/https://www.detran.ac.gov.br/wp-content/uploads/2022/06/Lista-de-Selecionados-CNH-Social.pdf
    61-122 line: https://web.archive.org/web/20240226031446/https://www.detran.ac.gov.br/wp-content/uploads/2022/06/Lista-de-Selecionados-CNH-Social.pdf
    """
    return open_docs('cpfs.txt')


@pytest.fixture
def cnpj_list():
    """
    1-88 line: https://web.archive.org/web/20240223150643/https://www.detran.df.gov.br/wp-content/uploads/2021/09/Empresas-CNH-Social.pdf
    """
    return open_docs('cnpj.txt')


@pytest.fixture
def nis_list():
    """
    1-56 line: https://web.archive.org/web/20240225200956/http://www.varzeagrande.mt.gov.br/storage/Anexos/18cd1d8751995dccb6116b97ab9e0ce7.pdf
    57-356 line: http://www.adcon.rn.gov.br/ACERVO/SEARH/DOC/DOC000000000151962.PDF
    """
    return open_docs('nis.txt')


@pytest.fixture
def cns_list():
    """
    1-61 line: https://web.archive.org/web/20240226014647/https://simaodias.se.gov.br/sites/simaodias.se.gov.br/files/LISTA%20VACINADOS%20D2%20IDOSOS%20-%2010032021%20-%20FORMULARIO.pdf
    62-182 line: https://web.archive.org/web/20240226015830/https://altamira.pa.gov.br/wp-content/uploads/2021/07/LISTA-DE-VACINADOS-20-07.pdf
    """
    return open_docs('cns.txt')


@pytest.fixture
def renavam_list():
    """
    1-173 line: https://web.archive.org/web/20240226050829/https://www.euamoleilao.com.br/imprimir/0067-leilao-do-detran-de-sao-paulo
    174-257 line: https://web.archive.org/web/20240226051016/https://www.euamoleilao.com.br/imprimir/0139-repasse-leilao-ciretran-s-sebastiao
    258-687 line: https://web.archive.org/web/20240226051542/https://portal.tjpr.jus.br/pesquisa_athos/publico/carregarAnexo.do;jsessionid=5ff0c586fab5cb74176b49c48765?tjpr.url.crypto=16c74de0ca500657bb7c1cc39118d26e6a12b4f4c9aa9444c033d87933160fa249878bb1b73255ac
    """
    return open_docs('renavam.txt')


@pytest.fixture
def te_list():
    """
    1-159 line: https://web.archive.org/web/20240226104403/https://issuu.com/psol.df/docs/lista_de_filiados_ao_psol_df___dist
    """
    return open_docs('te.txt')


@pytest.fixture
def cert_list():
    """google dorks: intext:"DATA DE NASCIMENTO (POR EXTENSO)" AND intext:"CERTIDÃO DE <CASAMENTO|ÓBITO|NASCIMENTO>" AND intext:"matricula" AND ext:pdf"""
    return open_docs('cert.txt')


@pytest.fixture
def valid_sei_list():
    return open_docs('valid_sei.txt')


@pytest.fixture
def invalid_sei_list():
    return open_docs('invalid_sei.txt')
