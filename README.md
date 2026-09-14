# Necromancer

Necromancer é um projeto em Python para controlar um computador Linux remotamente a partir de um Android com Termux usando SSH.

## Visão geral

O projeto usa uma arquitetura simples:

- O diretório `master/` representa o dispositivo que envia os comandos.
- O diretório `zombie/` representa o computador alvo que executa as ações.

A ideia é permitir que um celular execute comandos no computador pela rede, como verificar status do sistema, listar arquivos e consultar uso de disco.

## Funcionalidades

- Ver o status do sistema do computador remoto.
- Listar arquivos da pasta inicial do usuário.
- Consultar uso do disco.
- Executar comandos remotos de maneira simples via SSH.

## Estrutura do projeto

```text
necromancer/
├── README.md
├── master/
│   └── master.py
└── zombie/
    └── zombie.py
```

## Tecnologias

- Python 3
- Termux
- Linux Mint / Linux
- SSH

## Como funciona

1. O arquivo `master/master.py` é executado no celular.
2. Ele conecta no computador remoto usando SSH.
3. O comando é enviado para o arquivo `zombie/zombie.py`.
4. O computador remoto executa a operação e retorna a resposta.

## Configuração inicial

No arquivo `master/master.py`, ajuste os valores:

```python
IP = "SEU_IP"
USER = "NOME_DO_USUARIO"
```

Substitua:

- `SEU_IP` pelo IP do computador Linux.
- `NOME_DO_USUARIO` pelo usuário da máquina remota.

Também é necessário que o acesso por SSH esteja configurado corretamente entre o celular e a máquina alvo.

## Execução

No computador remoto, o script `zombie.py` aceita comandos como:

```bash
python3 ~/projeto/necromancer/zombie/zombie.py status
python3 ~/projeto/necromancer/zombie/zombie.py files
python3 ~/projeto/necromancer/zombie/zombie.py disk
```

No Termux, execute:

```bash
python3 ~/projeto/necromancer/master/master.py
```

## Observações

- Este projeto é um MVP funcional.
- O uso de SSH exige que a máquina remota tenha o serviço SSH habilitado.
- Para uso real em produção, é recomendado reforçar autenticação e limitar as ações permitidas.

## Versão

v0.6 (MVP) — Primeira versão funcional do projeto.