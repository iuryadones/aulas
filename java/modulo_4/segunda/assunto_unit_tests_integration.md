---
title  : Testes Integrados
author : Prof. Iury Adones
output :
    revealjs::revealjs_presentation
---

# Testes Integrados?

---

## Testes Integrados

Visa Garantir que os componentes da aplicação desenvolvidos separadamente funcionem perfeitamente quando integrados.

---

![Tipos de testes](./java/modulo_4/segunda/images/tipo_de_tests.png)

---

![Pipeline](./java/modulo_4/segunda/images/fabrica_testes.png)

# Prática

---

> Usaremos duas annotetions <span style="color:green">@Before</span> e <span style="color:green">@After</span>

---

```java
public class FileUtilsTest {

    private File diretorio;

    @Before
    public void prepara() {
        diretorio = new File("/home/rponte/test-data");
        diretorio.mkdirs();
    }

    @After
    public void limpaSujeira() {
        for (File f : diretorio.listFiles()) {
            f.delete();
        }
        diretorio.delete(); // deleta diretorio
    }
    ...
}
```

---

## Vamos fazer a Integração

  - Use a Task 1

---

## Segue o Fluxo

```java
@Before
public void instanciarNumeros() {
    // Instânciar os Números para os métodos de testes
}

@After
public void exibirNumeros() {
    // Quando terminar os testes exibir os números instanciados
}

// Métodos de Testes
```

# Ferramenta de Integração Continua

---

## Tools of CI

  - Jenkins
  - Travis
  - Circleci

---

> Pesquisem sobre tais ferramentas de CI

---

> Escolha qual será utilizada no projeto

---

## Próximo encontro veremos

 - Git
 - Github
 - Ferramenta de CI com Github

# Fim
