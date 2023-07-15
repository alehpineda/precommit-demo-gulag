# precommit-demo-gulag
Demo de pre-commit en python


1. Instalar pre-commit

```bash
pip install pre-commit
pre-commit --version
```

2. Agregar configuracion

```bash
pre-commit sample-config > .pre-commit-config.yaml
```

- Ejemplo the .pre-commit-config.yaml

```yaml
repos:
-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
    -   id: check-yaml
    -   id: end-of-file-fixer
    -   id: trailing-whitespace
-   repo: https://github.com/psf/black
    rev: 23.7.0
    hooks:
    -   id: black
```

- URL de hooks: https://pre-commit.com/hooks.html

3. Installar los hooks

```bash
pre-commit install
```

4. (Opcional) Correr los hooks contra todos los archivos.

```bash
pre-commit run --all-files
```
