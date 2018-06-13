---
title    : java e xml
date     : 13/06/2018
output   : 
    revealjs::revealjs_presentation
---

#  Manipulando xml

---

![test image size](java/modulo_4/primeiro/images/test.png) 

---

file: exemplo.xml

```xml
<produto>
  <nome>geladeira</nome>
  <preco>1000.0</preco>
  <descricao>geladeira de duas portas</descricao>
</produto>
```

---

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
