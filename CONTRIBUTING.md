# Contributing to BRdocs-validation

We welcome contributions from the community! Whether you're fixing bugs, adding new validators, or improving documentation, your help is appreciated.

## Good First Issues

Looking for your first contribution? Here are some ideas:

### New Document Validators

We'd love to add support for more Brazilian documents:

- **RG (Registro Geral)** - State ID numbers (varies by state)
- **Passaporte** - Brazilian passport numbers
- **CRM** - Medical license (Conselho Regional de Medicina)
- **OAB** - Lawyer registration (Ordem dos Advogados do Brasil)
- **CREA** - Engineering license (Conselho Regional de Engenharia)
- **CRF** - Pharmacy license (Conselho Regional de Farmácia)
- **Nota Fiscal** - Invoice numbers (NF-e, NFS-e)
- **Placa de Veículo** - Vehicle license plates (old and Mercosul formats)
- **Inscrição Estadual** - State tax registration (varies by state)

### Improvements

- Add formatted output option (e.g., input `12345678901` outputs `123.456.789-01` for CPF)
- Add generation of valid random documents for testing
- Improve error messages with more context
- Add async validation support

## How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/new-validator`)
3. Follow the existing code patterns in `br_docs/validators/`
4. Add tests with real document data (see `tests/` for examples)
5. Run `ruff check .` and `pytest` to ensure quality
6. Submit a Pull Request

## Validator Structure

Each validator should:

1. Inherit from `CheckDigits` (or `ValuesRegex` for format-only validation)
2. Define `Patterns` tuple with regex patterns for valid formats
3. Implement `calculate_digits()` for check digit validation
4. Include source URL for the algorithm in a docstring

See existing validators in `br_docs/validators/` for reference.

## Questions?

Open an issue or start a discussion. We're happy to help!
