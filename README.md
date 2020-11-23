# GoodReads

Esse projeto foi desenvolvido como trabalho de conclusão de curso. O documento final do trabalho, com maiores explicações se encontra do pdf "O Uso de Redes Neurais Para Classificação de Gêneros Literários".

## Resumo

Este trabalho tem como objetivo realizar uma análise de informações de livros e desenvolver um modelo computacional para classificação de livros em gêneros literários utilizando redes neurais recorrentes. Para tal, obteve-se um conjunto de dados composto pela informação de mais de 50 mil livros retiradas do site Goodreads, embora apenas 30 mil estivessem elegíveis para uso. Todo trabalho foi desenvolvido em Python. Foi aplicada uma rede neural recorrente utilizando a biblioteca TensorFlow e a API Keras, com a descrição como input. Foi considerado que cada livro poderia pertencer a apenas um gênero e o problema foi tratado como uma classificação multi classe. Por fim, o modelo foi comparado com algoritmos usuais para esse tipo de problema: regressão logística, máquinas de vetores de suporte e Naïve Bayes.

## Como Utilizar

A pasta goodreads_scraper é um projeto do Scrapy. No arquivo books estão contidos todos os links de livros cujas informações foram raspadas do site GoodReads. O comando:

scrapy crawl books -o books.jl

inicia a raspagem de dados.

A pasta "analise de dados e modelos" já contem o arquivo books.jl resultado dessa raspagem, com a informação de mais de 54 mil livros. O notebook "EDA, preprocessamento e analise dos resultados", como o nome diz, contem toda a parte de analise e foi rodado em um notebook normal, usando o comando:

pipenv run jupyter notebook

Ele gera o arquivo df_xlabel que será utilizado como base para treinamento, pelo notebook "teinamento dos modelos". Esse notebook na verdade foi rodade no ambiente do Colab, por questão de disponibilidade de recursos e facilidade de uso do TensorFlow.
