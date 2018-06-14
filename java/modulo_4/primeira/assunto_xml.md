---
title    : java e xml
author   : Prof. Iury Adones
output   : 
    revealjs::revealjs_presentation
---

# Você sabe o que é <b><i><span style="color:blue">XML</span></i></b>?

---

Arquivo: modelo.xml

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<estudante codigo="1">
  <nome>João Pernambucano de Recife</nome>
  <curso>Java Avançado</curso>
  <caracteristica>Megalomaníaco</caracteristica>
</estudante>
```

---

## <b><i><span style="color:blue">XML</span></i></b> – LINGUAGEM DE MARCAÇÃO

  - <b><i><span style="color:blue">XML</span></i></b>, do inglês <i><b><span style="color:yellow">eXtensible Markup Language</span></i></b>, é uma linguagem de marcação recomendada pela <i><b><span style="color:green">W3C</span></i></b> para a criação de documentos com dados organizados hierarquicamente, tais como textos, banco de dados ou desenhos vetoriais.
  - A linguagem <b><i><span style="color:blue">XML</span></i></b> é classificada como extensível porque permite definir os elementos de marcação.

---

## MARCAÇÃO?

  - Linguagem de marcação é um agregado de códigos que podem ser aplicados a dados ou textos para serem lidos por computadores ou pessoas.
  - Por exemplo, o <b><i><span style="color:red">HTML</span></i></b> é uma linguagem de marcação para organizar e formatar um website, já o <b><i><span style="color:blue">XML</span></i></b> tem o mesmo conceito, mas para padronizar uma sequência de dados com o objetivo de organizar, separar o conteúdo e integrá-lo com outras linguagens

---

## PRINCIPAIS CARACTERÍSTICAS DO <b><i><span style="color:blue">XML</span></i></b>

  - Separação do conteúdo da formatação
  - Simplicidade e legibilidade, tanto para humanos quanto para computadores
  - Possibilidade de criação de tags sem limitação
  - Criação de arquivos para validação de estrutura (chamados DTDs)
  - Interligação de bancos de dados distintos
  - Concentração na estrutura da informação, e não na sua aparência

# Exercícios

---

> Usaremos **Eclipse** e **OpenJDK-8**

---

## Crie Projeto Java nos seguintes passos:
  - File
    - New
      - Java Project
        - Project name: xstream 
        - Use an execution environments JRE: JavaSE-1.8
        - Create separate folders for sources and class file: True
        - Click: finish

---

Construa arquivos no formato <b><i><span style="color:blue">XML</span></i></b> para os objetos <span style="color:orange">Estante</span> e <span style="color:red">Livro</span>, ambos dentro do Projeto Java.

---

Modelo do livro

|<span style="color:red">Livro</span>|
|:----------------|
|id               |
|titulo           |
|autor            |
|ano de lançamento|
|classificação    |

---

Modelo da estante

|<span style="color:orange">Estante</span>| 
|:------| 
|id     | 
|tipo   | 
|tamanho| 
|livros | 

---

arquivo: livro.xml

```xml
<livro>
  <id>...</id>
  <titulo>...</titulo>
  <autor>...</autor>
  <anoDeLancamento>...</anoDeLancamento>
  <classificacao>...</classificacao>
</livro>
```

---

arquivo: estante.xml

```xml
<estante>
  <id>...</id>
  <tipo>...</tipo>
  <tamanho>...</tamanho>
  <livros>...</livros>
</estante>
```

#  Manipulando <b><i><span style="color:blue">XML</span></i></b> com Java

---

## Atalho para criar classe em Java no Eclipse

> `Ctrl` + `n` 

---

## Crie Classes
  - Estante
  - Livro

> Use package br.com.username.xstream;

---

Arquivo: Estante.java

```java
package br.com.username.xstream;

public class Estante {
        private int id;
        private String tipo;
        private double tamanho;
        private String livros;

}
```

---

Arquivo: Livro.java

```java
package br.com.username.xstream;

public class Livro {
        private int id;
        private String titulo;
        private String autor;
        private int anoDeLancamento;
        private double classificacao;

}
```

---

## Atalho de busca no Eclipse

> `Ctrl` + `3` 

---

## Use o atalho de busca nos arquivos 
  - Estante.java e Livro.java  
  - Busque por "generate construtor using fields" 
  - Selecione todos os atributos

---

```java
package br.com.username.xstream;

public class Livro {
        ...
        public Livro(int id,
                       String titulo,
                       String autor,
                       int anoDeLancamento,
                       double classificacao) {

                this.id = id;
                this.titulo = titulo;
                this.autor = autor;
                this.anoDeLancamento = anoDeLancamento;
                this.classificacao = classificacao;
        } 

}
```

---

```java
package br.com.username.xstream;

public class Estante {
        ...
        public Produto(int id,
                       String tipo,
                       double tamanho,
                       String livros) {

                this.id = id;
                this.tipo = tipo;
                this.tamanho = tamanho;
                this.livros = livros;
        } 

}
```

---

## Como converter um objeto em java para arquivos em xml?

---

## Usaremos o [xstream](http://x-stream.github.io/download.html)

  - Baixe o arquivo `.zip` da distribuição binária
  - Descompactar
  - Usaremos os packages:
    - xstream-\*/lib/xstream/xpp3\_min-\*.jar
    - xstream-\*/lib/xstream-\*.jar

---

## Adicione os pacotes do xstream no projeto

> click com botão do mouse de propriedades no Projeto Java 

### Selecione
  - "Build to Path"
    - "Add External Archives"

---

> <span style="color:yellow">Antes</span> de fazer <span style="color:green">valer</span>, melhor <span style="color:red">testar</span>!!!

---

### create Source Folder
  - name: test
    - create java class
      - name: EstanteTest
      - name: LivroTest

---

Arquivo: EstanteTest.java

```java
package br.com.username.xstream;

public class EstanteTest {

}
```

---

Arquivo: LivroTest.java

```java
package br.com.username.xstream;

public class LivroTest {

}
```

---

## Escreva o método test

```java
package br.com.username.xstream;

public class EstanteTest {
        
        @Test
        public void GerarXml() {
                
        }
        
}
```

---

## Escreva o método test

```java
package br.com.username.xstream;

public class LivroTest {
        
        @Test
        public void GerarXml() {
                
        }
        
}
```

---

Na linha do <span style="color:blue">`@Test`</span> use o atalho para correção da linha

> `Ctrl` + `1` 

Add package JUnit4

---

Arquivo: EstanteTest.java

```java
package br.com.username.xstream;

import org.junit.Test;

public class EstanteTest {
        
        @Test
        public void GerarXml() {
                
        }
        
}
```

---

Arquivo: LivroTest.java

```java
package br.com.username.xstream;

import org.junit.Test;

public class LivroTest {
        
        @Test
        public void GerarXml() {
                
        }
        
}
```

---

> Vamos fazer o teste da Estante

---

Sabemos o formato xml esperado da estante

```xml
<estante>
  <id>...</id>
  <tipo>...</tipo>
  <tamanho>...</tamanho>
  <livros>...</livros>
</estante>
```

---

```java
...
public class EstanteTest {
        
        @Test
        public void GerarXml() {
                String xmlEsperado = "<estante>\n"+
                                     "  <id>1</id>\n"+
                                     "  <tipo>guarda livros</tipo>\n"+
                                     "  <tamanho>100.0</tamanho>\n"+
                                     "  <livros>1,2,3</livros>\n"+
                                     "</estante>";

                Estante armario = new Estante(1,
                                              "guarda livros",
                                              100.0,
                                              "1,2,3");

        }
        
}
```

---

```java
...
public class EstanteTest {
        
        @Test
        public void GerarXml() {
                ...
                Estante armario = new Estante(1,
                                              "guarda livros",
                                              100.0,
                                              "1,2,3");

                XStream xstream = new XStream();
                String xmlGerado = xstream.toXML(armario);

                assertEquals(xmlEsperado, xmlGerado);
        }
        
}
```

---

> Execute com Junit Test o Arquivo EstanteTest.java

---

> Vamos analisar

---

```java
...
public class EstanteTest {
        
        @Test
        public void GerarXml() {
                ...
                Estante armario = new Estante(1,
                                              "guarda livros",
                                              100.0,
                                              "1,2,3");

                XStream xstream = new XStream();
                xstream .alias("estante", Estante.class);
                String xmlGerado = xstream.toXML(armario);

                assertEquals(xmlEsperado, xmlGerado);
        }
        
}
```

---

Sabemos o formato xml esperado do livro

```xml
<livro>
  <id>...</id>
  <titulo>...</titulo>
  <autor>...</autor>
  <anoDeLancamento>...</anoDeLancamento>
  <classificacao>...</classificacao>
</livro>
```

---

## Façam o teste para o Livro

---

> Então dúvidas?

