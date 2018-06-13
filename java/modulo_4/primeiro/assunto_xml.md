---
title    : java e xml
date     : 13/06/2018
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

---

#  Manipulando <b><i><span style="color:blue">XML</span></i></b> com Java

---

## Usaremos o [xstream](http://x-stream.github.io/download.html)

  - Baixe o arquivo `.zip` da distribuição binária
  - Descompactar
  - Usaremos os packages:
    - xstream-\*/lib/xstream/xpp3\_min-\*.jar
    - xstream-\*/lib/xstream-\*.jar

---

<!-- ![test image size](java/modulo_4/primeiro/images/test.png) -->

Ctrl + n criar uma classe


```java
package br.com.fuctura.xstream;

public class Produto {
	private String nome;
	private double preco;
	private String descricao;

}
```

---

Ctrl + 3 -> buscar: generate construtor using fields

```java
package br.com.fuctura.xstream;

public class Produto {
	private String nome;
	private double preco;
	private String descricao;

	public Produto(String nome, double preco, String descricao) {
		this.nome = nome;
		this.preco = preco;
		this.descricao = descricao;
	} 

}
```

---

download: xstream.zip
unzip xstream.zip


packages:
  - xpp3_min-\*.jar
  - xstream-\*.jar

---

project:
  - build to path
    - add arquivos externos

---

create Source Folder
  - name: test
    - create java class
      - name: ProdutoTest

---

```java
package br.com.fuctura.xstream;

public class ProdutoTest {

}
```

---

```java
package br.com.fuctura.xstream;

public class ProdutoTest {
	
	@Test
	public void GerarXml() {
		
	}
	
}

`Ctrl` + `1` -> na linha do `@Test` e add package JUnit4
```
---

```java
package br.com.fuctura.xstream;

import org.junit.Test;

public class ProdutoTest {
	
	@Test
	public void GerarXml() {
		
	}
	
}
```

---

```java
package br.com.fuctura.xstream;

import static org.junit.Assert.assertEquals;

import org.junit.Test;

import com.thoughtworks.xstream.XStream;

public class ProdutoTest {
	
	@Test
	public void GerarXml() {
		String xmlEsperado = "<produto>\n"+
				"  <nome>geladeira</nome>\n"+
				"  <preco>1000.0</preco>\n"+
				"  <descricao>geladeira de duas portas</descricao>\n"+
				"</produto>";

		Produto geladeira = new Produto("geladeira", 1000.0, "geladeira de duas portas");

		XStream xstream = new XStream();
		xstream .alias("produto", Produto.class);
		String xmlGerado = xstream.toXML(geladeira);

		assertEquals(xmlEsperado, xmlGerado);
	}
	
}
```

---

```java
package br.com.fuctura.xstream;

public class Produto {
	private int codigo;
	private String nome;
	private double preco;
	private String descricao;

	public Produto(int codigo, String nome, double preco, String descricao) {
		this.codigo = codigo;
		this.nome = nome;
		this.preco = preco;
		this.descricao = descricao;
	} 
}
```
