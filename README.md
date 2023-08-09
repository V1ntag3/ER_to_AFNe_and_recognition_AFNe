
# Trabalho de Teoria da Computação

Conversor de ER em AFNe e reconhecimento do autômato gerado

## Autores

- Marcos Vinicius Ribeiro Alencar
- Emanuel Mendes
- Lucas William

## Funcionalidades

Reconhece palavras com:

- Caracteres concatenados
- *

## Instalação

Para utilizar o projeto é necessário ter instado na máquina o python 3

No linux:
```shell
 sudo apt-get install python3.9
```
No Windows :
https://python.org.br/instalacao-windows/
## Uso/Exemplos

Para utilizar o programa basta inicializar o arquivo main.py e entrar com a expressão desejada.
```python
Entre com sua expressão regular: a*b
```
O programa irá processar a expressão regular e determinar o automato finito não deterministico com estados vazios equivalente e vai externalizar esse conjunto de dados.

```python

O autômato gerado tem os seguintes dados: 
Estados:  ['q0', 'q1', 'q2', 'q3']
Alfabeto:  ['a', 'b']
Transições: 
0 -> 1 : a
0 -> 2 : epsilon
1 -> 0 : epsilon
2 -> 0 : epsilon
2 -> 3 : b
Estado Inicial:  q0
Estados Finais:  ['q3']

```
Por fim entre com a palavra a qual deseja realizar o reconhecimento:

```python
Entre com sua cadeia de caracteres: aaaaaaaaaaaab
```
E caso seja aceita retornará:

```python
Palavra é aceita
```
