---
title  : Controle de versões com Git
author : Prof. Iury Adones
output :
    revealjs::revealjs_presentation
---

# Controle de versões? Git? 

---

## Controle de versões

  - Criado para ajudar na melhoria continua de projetos
    - Facilita na gestão das partes envolvidas
    - Existe um fluxo na manipulação dos arquivos
    - Sentimento de evolução
  - Backup
    - Copiar, Colar e alterar nome, nunca mais! 

---

## Git

Assim como muitas coisas boas na vida, o Git começou com um tanto de destruição criativa e controvérsia acirrada.  

---

## Tudo por causa do Linux

O kernel do Linux é um projeto razoavelmente grande, a manutenção do kernel do Linux (1991-2002), eram feitas mudanças repassadas como patches e arquivos compactados.

Em 2002, o projeto do kernel do Linux começou a usar um sistema DVCS proprietário chamado BitKeeper.

---

## Contrato Revogado

Em 2005, o relacionamento entre a comunidade que desenvolvia o kernel e a empresa que desenvolvia comercialmente o BitKeeper se desfez, e o status de isento-de-pagamento da ferramenta foi revogado.

---

## Revolução 

Isso levou a comunidade de desenvolvedores do Linux (em particular Linus Torvalds, o criador do Linux) a desenvolver sua própria ferramenta baseada nas lições que eles aprenderam ao usar o BitKeeper. 

---

## Melhorias

  - Velocidade
  - Design simples
  - Suporte robusto a desenvolvimento não linear (milhares de branches paralelos)
  - Totalmente distribuído
  - Capaz de lidar eficientemente com grandes projetos como o kernel do Linux (velocidade e volume de dados)

---

## Nova Concepção

Desde sua concepção em 2005, o Git evoluiu e amadureceu a ponto de ser um sistema fácil de usar e ainda assim mantém essas qualidades iniciais. É incrivelmente rápido, bastante eficiente com grandes projetos e possui um sistema impressionante de branching para desenvolvimento não-linear 

---

## Referência da história

[Uma Breve História do Git](https://git-scm.com/book/pt-br/v1/Primeiros-passos-Uma-Breve-História-do-Git)

# Git na Prática

---

## Intalação do Git no Windows

[https://git-scm.com](https://git-scm.com)

Baixe e Instale para seu Sistema Operacional

---

## Intalação do Git no Ubuntu

```bash
$ sudo apt-get install git
```

---

## Intalação do Git no Archlinux

```bash
$ sudo pacman -S git
```

---

## Configuração do Git

---

## Configure o nome do usuário

```bash
$ git config --global user.name "[nome]"
```

---

## Configure o email do usuário

```bash
$ git config --global user.email "[endereco-de-email]"
```

---

## Configure as cores

```bash
$ git config --global color.ui auto
```

---

## Explore o Git

[https://try.github.io](https://try.github.io)

---

## Vamos entender o Git

[https://learngitbranching.js.org/?NODEMO](https://learngitbranching.js.org/?NODEMO)

---

## Branch

```bash
$ git branch
* master
$ git branch dev
$ git branch
* master
dev
```

---

## Checkout

```bash
$ git checkout dev
$ git branch
master
* dev
```

---

## Commit

```bash
$ git branch
master
* dev
$ git commit -m "[dev] mod1"
$ git commit -m "[dev] mod2"
$ git commit -m "[dev] mod3"
```

---

## Commit

```bash
$ git checkout master
$ git branch
* master
dev
$ git commit -m "[master] mod1"
$ git commit -m "[master] mod2"
```

---

## Log

```bash
$ git log
```

Analise a história do projeto

---

## Merge

```bash
$ git branch
* master
dev
$ git merge dev
```

---

## Delete Branch

```bash
$ git branch
* master
dev
$ git branch -d dev
$ git branch
* master
```

---

## Reset

```bash
$ git reset C0
```

---

## Dúvidas?

# Git Remoto na Prática

---

## Usaremos o GitHub

[https://github.com](https://github.com)

Crie sua conta no Github

---

## Crie seu primeiro Repositório

  - Click em <span style="color:green">New Repository</span>
  - Repository name: calculadora
  - Description (optional): Calcular na Web 
  - Selecione: Public
  - Marque: initialize this repository with a README
  - Create repository

---

## link do projeto remoto

[https://github.com/seuUsuário/calculadora](https://github.com/seuUsuário/calculadora)

---

## Manipulando projeto localmente

```bash
$ mkdir calculadora
$ cd calculadora
$ git init
```

---

## Manipulando projeto remoto

```bash
$ git remote add hub https://github.com/seuUsuário/calculadora
$ git pull hub
$ git pull hub master
$ ls
README.md
```

---

## Modifique o README.md

Adicione o seu nome na última linha 

---

## Veja o status

```bash
$ git status
```

---

## Adicione a modificação

```bash
$ git add README.md
```

---

## Descreva em uma mensagem a modificação

```bash
$ git commit -m "Adiciona o nome do mantenedor"
```

---

## Envie para o github

```bash
$ git push hub master
```

---

## Veja a evolução do seu projeto 

```bash
$ git log
```

---

## Vamos nos Aprofundar

Use o projeto Java da Calculadora, deixe só a classe Soma e a classe SomaTeste, mova para a pasta da calculadora que está com o github.

---

> Enviei ao GitHub

# Github com CI

---

> Usaremos o CircleCI

---

## Vincule sua conta do github

[https://circleci.com](https://circleci.com)

---

## Vamos adicionar o projeto calculadora 

  - Add Project
  - calculadora : Set Up Project
  - Selecione Sistema Operacional: Linux
  - Selecione Linguagem: Maven (Java)
  - Crie uma pasta chamada .circleci e add um fileconfig.yml (então fica assim .circleci/config.yml). 
  - Copie e cole no config.yml as configurações
  - Start Building

---

> Adicione pom.xml

---

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0" 
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">

  <modelVersion>4.0.0</modelVersion>
 
  <groupId>calculadora</groupId>
  <artifactId>calculadora-app</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>
 
  <name>Maven Quick Start Archetype</name>
  <url>http://maven.apache.org</url>
 
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.8.2</version>
      <scope>srctest</scope>
    </dependency>
  </dependencies>
</project>
```

---

## Agora estamos com CI

---

> Adicione mais testes para soma
> Enviei para o GitHub
> Veja o teste no circleCI

---

## No próximo encontro

  - Gestão de projeto com métodos ágeis
    - Scrum
    - Kanban
    - Outro, estou pensando.
  - Uso de Ferramentas para métodos ágeis
    - Jira
    - Trello
    - Github

# Fim


