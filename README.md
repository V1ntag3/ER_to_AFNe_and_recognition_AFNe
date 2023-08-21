
# Trabalho de Teoria da Computação

Conversor de ER em AFNe e reconhecimento do autômato gerado

## Autores

- Marcos Vinicius Ribeiro Alencar
- Emanuel Mendes
- Lucas William

## Funcionalidades

Reconhece palavras com:

- Caracteres concatenados
- \*
- \+

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

Dentro da pasta abrir um terminal e digitar
```python
python main.py
```

```python
Entre com sua expressão regular: a*b
```
O programa irá processar a expressão regular e determinar o automato finito não deterministico com estados vazios equivalente e vai externalizar esse conjunto de dados.

```python

O autômato gerado tem os seguintes dados: 
Alfabeto: ['b', 'a']
Estados: ['q0', 'q1', 'q2', 'q3', 'q4']
Estado Inicial: q2
Estado Final: ['q4']
Trasições: 
q0:a --> {q1}
q0:epsilon --> {q3}
q1:epsilon --> {q0, q3}
q2:epsilon --> {q0}
q3:b --> {q4}

```
Por fim entre com a palavra a qual deseja realizar o reconhecimento:

```python
Entre com sua cadeia de caracteres: aaaaaaaaaaaab
```
E caso seja aceita retornará:

```python
Palavra é aceita
```
