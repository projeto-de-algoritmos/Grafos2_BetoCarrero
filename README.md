# Mapa do Beto Carrero

**Número da Lista**: 26<br>
**Conteúdo da Disciplina**: Grafos 2<br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 17/0011267  |  Giovanna Borges Bottino        |
| 18/0119818  |  Felipe Boccardi Silva Agustini |

## Sobre 
Esse projeto tem como objetivo utilizar o algoritmo de dijkstra para criar um caminho no mapa do Beto Carrero. Foi inspirado na experiência da dupla que quando precisava se locomover pelo parque geralmente fazia o maior percurso. 

Mapa com todas as conexões.

![mapa](/public/mapa-beto-carrero-world-com-linhas.png)

## Screenshots

![imagem 1](/public/screenshot1.PNG)
![imagem 2](/public/screenshot2.PNG)
![imagem 3](/public/screenshot3.PNG)

## Video

https://user-images.githubusercontent.com/23579166/205518266-26a2fd62-97d6-47a0-8200-a140f3e19fa1.mp4

## Instalação 
*Linguagem*: Python<br>
*Framework*: flask<br>

### Crie um ambiente em python 3
```
python3 -m venv env
```

### Ative o ambiente
```
source env/bin/activate

```
ou se estiver usando windows

```
 .\env\Scripts\activate

```
### Instale as dependencias
```
pip install -r requirements.txt
```

## Uso 

### Após a instalação entre na pasta

```
cd src/
```

### Rode executando o comando
```
flask run
```

## Testes 

Para rodar os testes basta executar o comando a baixo.
```
python -m unittest tests/unit/test_graph.py
```

## Outros 
Este trabalho tem como finalidade mostrar os conhecimentos da dupla no uso de algoritimos em grafos e não possui fins comerciais. As imagens contidas neste repositório referentes ao mapa do parque, tais quais os nomes das atrações contidos nelas pertencem a J.B.WORLD ENTRETENIMENTOS S/A. e podem ser retirada caso solicitado. Os alunos e este trabalho não possuem quaisquer vinculo com a J.B.WORLD ENTRETENIMENTOS S/A. e seus patrocinadores. 
