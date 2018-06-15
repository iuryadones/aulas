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

![](./java/modulo_4/segunda/images/calculadora-cientifica.jpg)

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

assertArrayEquals

```java
import static org.junit.Assert.assertArrayEquals;

import org.junit.Test;

public class AssertTest {

    @Test
    public void testAssertArrayEquals() {
        byte[] expected = "trial".getBytes();
        byte[] actual = "trial".getBytes();

        assertArrayEquals("failure - byte arrays not same", 
                          expected, 
                          actual);
    }
}
```

---

assertEquals

```java
import static org.junit.Assert.assertEquals;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertEquals() {
        assertEquals("failure - strings are not equal", "text", "text");
    }

}
```

---

assertFalse

```java
import static org.junit.Assert.assertFalse;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertFalse() {
        assertFalse("failure - should be false", false);
    }

}
```

---

assertNotNull

```java
import static org.junit.Assert.assertNotNull;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertNotNull() {
        assertNotNull("should not be null", new Object());
    }

}
```

---

assertNotSame

```java
import static org.junit.Assert.assertNotSame;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertNotSame() {
        assertNotSame("should not be same Object", new Object(), new Object());
    }

}
```

---

assertNull

```java
import static org.junit.Assert.assertNull;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertNull() {
        assertNull("should be null", null);
    }

}
```

---

assertSame

```java
import static org.junit.Assert.assertSame;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertSame() {
        Integer aNumber = Integer.valueOf(768);
        assertSame("should be same", aNumber, aNumber);
    }

}
```

---

assertThat

```java
import static org.hamcrest.CoreMatchers.both;
import static org.hamcrest.CoreMatchers.containsString;
import static org.junit.Assert.assertThat;

import org.junit.Test;

public class AssertTests {

    // JUnit Matchers assertThat
    @Test
    public void testAssertThatBothContainsString() {
        assertThat("albumen", 
                   both(containsString("a")).and(containsString("b")));
    }

}
```

---

assertThat

```java
import static org.hamcrest.CoreMatchers.hasItems;
import static org.junit.Assert.assertThat;

import java.util.Arrays;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertThatHasItems() {
        assertThat(Arrays.asList("one", "two", "three"),
                   hasItems("one", "three"));
    }

}
```

---

assertThat

```java
import static org.hamcrest.CoreMatchers.containsString;
import static org.hamcrest.CoreMatchers.everyItem;
import static org.junit.Assert.assertThat;

import java.util.Arrays;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertThatEveryItemContainsString() {
        assertThat(Arrays.asList(new String[] { "fun", "ban", "net" }), 
                                 everyItem(containsString("n")));
    }

}
```

---

assertThat

```java
...
public class AssertTests {

  // Core Hamcrest Matchers with assertThat
  @Test
  public void testAssertThatHamcrestCoreMatchers() {
    assertThat("good", allOf(equalTo("good"), startsWith("good")));
    assertThat("good", not(allOf(equalTo("bad"), equalTo("good"))));
    assertThat("good", anyOf(equalTo("bad"), equalTo("good")));
    assertThat(
      7, 
      not(CombinableMatcher.<Integer> either(equalTo(3)).or(equalTo(4)))
    );
    assertThat(new Object(), not(sameInstance(new Object())));
  }

}
```

---

assertTrue

```java
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class AssertTests {

    @Test
    public void testAssertTrue() {
        assertTrue("failure - should be true", true);
    }

}
```

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

