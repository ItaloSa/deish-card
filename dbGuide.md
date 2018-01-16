# Deish-Db Guide

----
## Get Started

> A Deish-Db é uma tentativa de criar um banco de dados não relacional usando como estrutura principal uma árvore vermelha e preta.

----
## Uso

Usar Deish-Db é fácil! Siga os seguintes passos.

#### 1. Import.
    
    from deish import DeishDb

#### 2. Instancie

    db = DeishDb()

#### 3. Use e abuse

    db.get('colection') #returns all in colection 

---
## Returns a message!

Alguns métodos retornam mensagem. Tente:
    
    >>> from deish import DeishDb
    >>> db = db.deish()
    >>> db.deish()
    {'mensage': "Hello, i'm here! i'm in version pre-alpha. Enjoy, but be careful :-)" }

**Uso:**

Para saber o status dos metodos use:

    print(db.<comando>()['mensage'])

Exemplo:

    >>> print(db.deish()['mensage'])
    Hello, i'm here! i'm in version pre-alpha. Enjoy, but be careful :-)

---
## Métodos

Nos exemplos de método estaremos usando < > para expressar um valor que será definido por você. De antemão, é preciso saber alguns tipos.

* **colection** -> string

* **key** -> interger

* **{data}** -> dictionary

### Crud:


*  **1. *Push()* **

        db.push('colection', key, {data} )
    > returns: {'mensage': 'Ok'}

---
*  **2. *Get()* **

 Possui duas formas de ser chamado. Com parâmetro, que retorna um item, ou sem, que retorna toda a coleção no formato: chave e dados.

 Com:

        db.get('colection')
    > returns: {'key': {date}}


 Sem:

        db.get('colection')
    > returns: {data}

---
*  **3. *Update()* **

        db.update(colection, key, data)
    > returns: {'mensage': 'Ok'}

---
*  **2. *Remove()* **

 Possui duas formas de ser chamado. Com parâmetro apaga somente um item, e sem parâmetro, que apaga a coleção toda.

 Com:

        db.get('colection', key)
    > returns: {'mensage': 'item <item> and colection <colection> deleted'}


 Sem:

        db.remove('colection')
    > returns: {'mensage': 'Colection <colection> deleted'}

---
### *New_colection()*:

Esse método cria uma nova coleção no banco de dados
      
    db.new_colection('colection')
> returns: {'mensage': 'Colection created'}

---
### *Get_colections()*:

Retorna a lista com todas as coleções do banco
      
    db.get_colections()
> returns: ['1Colection', '2Colection', ... 'nColection']

---
### *Colection_exists()*:

Retorna um booleano
      
    db.get_colections('colection')
> returns: True or False
