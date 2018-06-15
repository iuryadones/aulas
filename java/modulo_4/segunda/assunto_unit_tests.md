---
title  : Testes Unitários
author : Prof. Iury Adones
output :
    revealjs::revealjs_presentation
---

# Por que Testar? 

---

![Avião recém desenvolvido](./java/modulo_4/segunda/images/img-aviao.jpg)

---

![Avião 14-BIS](./java/modulo_4/segunda/images/img-aviao-14bis.jpg)

---

> Em 23 de outubro de 1906 o inventor brasileiro <b><span style="color:green">Alberto Santos-Dumont</span></b> criou a aeronave 14 BIS e <b><span style="color:yellow">testou</span></b> em Paris.

# Vamos pensar

---

## Pense no mundo real

Cliente recebe um software

  - Moderno
  - Inovador
  - Econômico
  - Nunca testado

---

> Isso vai dar?

---

![BOOM!!!](./java/modulo_4/segunda/images/bomba-nuclear.jpg)

# Testes de softwares

---

##  Usaremos Ferramentas de Testes? 

  - JUnit4
  - JUnit5

---

## Antes da prática

> Vamos explorar a problemática

---

## Desenvolver uma Calculadora Científica

---

![WTF?](./java/modulo_4/segunda/images/WTF.jpg)

---

## Vamos dividir o projeto em dois grupos

---

## Task do Primeiro Grupo

  - Construir operadores aritméticos para Números

    - Soma (+)
    - Subtração (-)
    - Divisão (/)
    - Multiplicação (*)

---

## Task do Segundo Grupo

  - Construir operadores aritméticos para Matrizes

    - Soma (+)
    - Subtração (-)
    - Divisão (/)
    - Multiplicação (*)

---

## Monte sua Equipe

 - 2 e ou 3 participantes?

---

## Ops, Tem Surpresa!

# Práticas com JUnit4

---

## Crie um Projeto Java

  - Crie classes para cada operador no **src/**
    - Ex: Operador.java
      - public double Operador
    - Crie um método chamado **exec** e faça a operação aritmética
    - Adicione o main
      - Instâncie o Operador aritmético
      - Execute a instância com exec
      - Exiba o resultado

  - Crie um source folder **srctest/**
  - Crie classes para cada operador no **srctest/**

---

> Usaremos a anotação <span style="color:blue">@Test</span>

---

## Vamos fazer um Teste juntos

# Práticas com JUnit5

---

## Junit4 vs Junit5

