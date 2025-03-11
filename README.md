# Pensamento Computacional - Execícios de aula

- [Prof Matheus Jardim Bernardes](https://matheusjardimb.com/)
- [Atitus.edu.br](https://atitus.edu.br/)
>magnum opus da internet brasileira abaixo
- [pudim.com.br](https://pudim.com.br)

Exercícios de aula da disciplina de Pensamento Computacional.

## Sobre mim

🔷 brasileiro, estudante de Ciência da Computação e... só isso mesmo .-.

## DICAS:

- Entenda completamente o que o exercício solicita ANTES de começar a programar.
- Comece escrevendo um pseudo-código em português para estruturar a lógica que deseja criar.
- Use nomes de variáveis claros e objetivos (prefira ‘nome’ em vez de ‘n’; prefira ‘idade’ em vez de ‘i’).
- Acrescente comentários no código para ajudar a você mesmo.
- Faça testes de mesa para validar a sua lógica: utilize papel e caneta, faça rabiscos!
- Quando trabalhar com listas, preste muita atenção nos limites: avalie se não está tentando acessar uma posição menor
  que zero ou maior que a última posição.

## Fork do projeto

Para criar o seu próprio projeto, clique no botão 'Fork' no topo da tela
em [https://github.com/matheusjardimb/atitus_pensComp_aulas/](https://github.com/matheusjardimb/atitus_pensComp_aulas/).

Após isso, será necessário ativar a execução das 'Actions'. Para isso, acesse o menu 'Actions' no topo da tela e clique
na opção de ativar workflows.

## Testes automatizados

Este repositório está configurado para que os testes automatizados sejam executados a cada novo commit diretamente no
GitHub.

Para mais informações, consulte o arquivo [.github/workflows/tests.yml](.github/workflows/tests.yml).

Para executar os testes em seu computador:

```bash
# Instale as dependências (apenas necessário executar uma vez)
pip install -r requirements.txt

# Execute os testes
pytest
```

## Ao desenvolver no seu computador

Considere instalar o [PyEnv](https://github.com/pyenv/pyenv) para gerenciar múltiplas versões de Python em seu
computador.

A versão de Python sugerida/necessária para executar as atividades deste projeto está no
arquivo [.python-version](.python-version).

Caso esteja usando o [Git](https://git-scm.com/), considere utilizar o pre-commit:

```bash
pre-commit install
```
