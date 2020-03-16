# Word2Vec

>**NOTE**: Versão em [Português](#pt) abaixo.

##### \[EN\]

The documents present in this folder aim at a comum field of NLP: word embeddings. Word embeddings are vector representations of words from a given vocabulary, which enables the usage of many mathematical operations on such vectors leading to amazing discoveries.

## Reproducibility
In order to reproduce the study developed here, one must know a little bit about *python* and *jupyter notebook*. If you don't know anything about it, please take a look at these resources:

- https://www.dataquest.io/blog/jupyter-notebook-tutorial/
- https://www.learnpython.org/
- https://www.python.org/about/gettingstarted/

Assuming that you already know how to code in python through a jupyter notebook and uses a *linux SO*  **with** python in it, let's move on.

### Environment setting
First, let's install `virtualenv`. With your terminal open inside _word2vec_ notebook's root folder, type:
```bash
pip install virtualenv
```

Then, create a new virtual environment and activate it:
```bash
virtualenv venv
source venv/bin/activate
```

Finally, install all needed dependencies:
```bash
pip install -r requirements.txt
```

#### Reload virtualenv
Sometimes, after installing the dependecies jupyter notebook doesn't find the modules. In that case all you need to do is reactivate the virtualenv inside the root folder, just like this:
```bash
source venv/bin/activate
```


### Execute the code
With everything set, enable jupyter notebook server and execute the code cells. If you don't recall how to do so, on a terminal inside notebook's root folder type:
```bash
jupyter notebook
```

After that, a new browser window will be opened and you can take from there.

--------------------
##### \[PT\]

Os documentos presentes neste diretório visam um campo comum de PNL: _word embeddings_. _Word embeddings_ são representações vetoriais de palavras de um determinado vocabulário, o que permite o uso de muitas operações matemáticas em tais vetores, levando a descobertas surpreendentes.

## Reprodutibilidade

Para reproduzir o estudo desenvolvido aqui, é preciso conhecer um pouco sobre o _python_ e _notebooks jupyter_. Se você não souber nada, consulte estes recursos (todos em inglês):

- https://www.dataquest.io/blog/jupyter-notebook-tutorial/
- https://www.learnpython.org/
- https://www.python.org/about/gettingstarted/

Supondo que você já saiba codificar em python por meio de um notebook jupyter e use um _SO linux_ __com__ python, vamos seguir em frente.

### Configuração de ambiente
Primeiro vamos instalar o `virtualenv`. Com o seu terminal aberto dentro da pasta raiz do notebook _word2vec_, digite:
```bash
pip install virtualenv
```

Em seguida, crie um novo ambiente virtual e ative-o:
```bash
virtualenv venv
source venv/bin/activate
```

## Execute o código

Com tudo pronto, habilite o servidor do _jupyter_ e execute as células de código. Se você não se lembra de como fazer isso, em um terminal dentro da pasta raiz do notebook, digite:
```bash
jupyter notebook
```

Depois disso, uma nova janela do navegador será aberta e você poderá partir dali.
