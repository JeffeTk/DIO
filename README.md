# ⚔️ NotebookLM: Estratégia em Pokémon com apoio de Inteligência Artificial
https://notebooklm.google.com/notebook/392a2a35-162e-42b2-9009-f620abe7ece9

## 📌 Contexto e Objetivos

Este projeto explora o uso da Inteligência Artificial como ferramenta de apoio ao aprendizado, utilizando o universo de Pokémon como base para estudo de estratégias,
análise lógica e tomada de decisão.

A proposta é aplicar conceitos de IA para compreender melhor mecânicas de batalha, vantagens entre tipos e construção de equipes estratégicas.

### 🎯 Objetivos:

* Utilizar IA para análise estratégica em batalhas Pokémon
* Desenvolver habilidades de engenharia de prompts
* Melhorar a capacidade de formular perguntas eficientes
* Explorar como a IA pode auxiliar na aprendizagem prática

---

## 📚 Curadoria de Fontes

As seguintes fontes foram utilizadas como base teórica e prática:

1. https://game8.co/games/Pokemon-UNITE
2. https://unite-db.com
3. https://pokemondb.net
4. https://www.pokemon.com/br
5.https://www.smogon.com/dex/sv/pokemon/

---

## ⚙️ Engenharia de Prompts e "Cicatrizes"

Durante o desenvolvimento, diferentes prompts foram testados para obter melhores respostas da IA.

---

### 🔹 Exemplo 1: Análise de Tipos

**Prompt inicial:**

> Qual o melhor tipo de Pokémon?

**Resposta:**
A definição do "melhor" tipo de Pokémon depende inteiramente do contexto, seja no cenário competitivo de batalhas tradicionais (Singles) ou em jogos como Pokémon UNITE.

Contexto Competitivo Tradicional (Smogon SV)
No formato competitivo de Pokémon Scarlet & Violet (Smogon), os Pokémon considerados os mais poderosos são agrupados nos níveis Uber e AG (Anything Goes). Ao analisar
esses grupos, certos tipos aparecem com frequência devido às suas vantagens estratégicas:

*Tipos Dragão, Fantasma e Psíquico: Muitos dos Pokémon mais fortes do jogo pertencem a esses tipos. Exemplos incluem Calyrex-Shadow (Psíquico/Fantasma) no tier AG, 
Miraidon (Elétrico/Dragão) também no tier AG, e Koraidon (Lutador/Dragão) no tier Uber
Outros Dragões lendários como Dialga, Giratina e Rayquaza (mencionado como chefe no UNITE) ocupam consistentemente o tier Uber

*Tipo Aço: Este tipo é valorizado por suas excelentes resistências defensivas. Pokémon como Archaludon (Aço/Dragão), Magearna (Aço/Fada) e Kingambit (Sombrio/Aço) são
destaques nos tiers mais altos (Uber ou OU)

*Versatilidade de Arceus: O Pokémon Arceus é um caso único de excelência, pois sua habilidade Multitype permite que ele mude para qualquer tipo dependendo da placa que
segura. Praticamente todas as formas de Arceus (Inseto, Dragão, Fogo, etc.) são classificadas no tier Uber, o que sugere que sua força reside na versatilidade de tipos
Contexto de Pokémon UNITE
No Pokémon UNITE, a eficácia não é determinada apenas por tipos elementais tradicionais, mas sim por Funções (Roles) e Tier Lists específicas que mudam conforme as
atualizações do jogo

Funções de Jogo: Os Pokémon são divididos em Attackers, Speedsters, All-Rounders, Defenders e Supporters.

Tier Lists: O jogo possui Tier Lists separadas para cada função, além de listas voltadas para o cenário competitivo, solo-queue ou para jogadores de "Low-Elo". 
Por exemplo, Pokémon como Moltres e Zapdos são adições recentes com guias de "melhores builds" para maximizar seu desempenho no jogo

Novas Mega Evoluções (Legends: Z-A)
Informações recentes indicam o surgimento de novas Mega Evoluções que prometem ser extremamente poderosas, como Mega Zeraora (Elétrico) e Mega Lucario Z (Lutador/Aço),
que utiliza uma mecânica de aceleração de movimentos, embora consuma energia rapidamente.
Além disso, Mega Meganium (com a habilidade Mega Sol) e Mega Feraligatr (com Dragonize) trazem novas formas de dominar o campo de batalha através de efeitos de clima e
mudança de tipo de ataques

Em resumo, não existe um único "melhor tipo" absoluto, mas os tipos Dragão, Aço e Fantasma costumam dominar o topo das classificações competitivas devido aos seus
atributos e à força dos Pokémon que os possuem

**Problema:** Resposta genérica e pouco útil.

**Prompt melhorado:**

> Explique as vantagens e desvantagens dos tipos de Pokémon em formato de tabela, incluindo exemplos práticos de batalhas.

**Resposta:**
Com base nos dados competitivos (Smogon SV) e nas mecânicas de jogos como Pokémon UNITE e o futuro Legends: Z-A, a eficácia dos tipos de Pokémon varia entre 
resistência defensiva e poder ofensivo. Abaixo, apresento uma tabela com as vantagens e desvantagens dos tipos mais proeminentes nas fontes, acompanhada de exemplos 
práticos de combate: Vantagens e Desvantagens por Tipo
Tipo
Vantagens Principais
Desvantagens / Fraquezas
Exemplo Prático de Batalha
Dragão
Resistência a tipos elementais básicos e acesso a Pokémon com atributos altíssimos (Lendários)

Vulnerável a tipos Fada e Gelo

Koraidon (Lutador/Dragão) domina o tier Uber ao invocar o sol, mas precisa evitar ataques de fadas como Clefable

Aço
Maior número de resistências defensivas; imune a veneno

Fraco contra Fogo, Lutador e Terra

Archaludon (Aço/Dragão) usa sua tipagem para resistir a ataques físicos e aumentar sua defesa com a habilidade Stamina

Fantasma
Imunidade a ataques do tipo Normal e Lutador; poucos tipos resistem aos seus golpes

Vulnerável a tipos Sombrio e ao próprio tipo Fantasma

Calyrex-Shadow (Psíquico/Fantasma) é tão poderoso que ocupa o tier AG, sendo capaz de derrubar equipes inteiras se não for contido por um tipo Sombrio

Fada
Imunidade total a ataques do tipo Dragão; forte contra tipos Lutador e Sombrio

Fraco contra ataques do tipo Aço e Veneno

Clefable atua como uma barreira defensiva crucial no tier OU, ignorando aumentos de status dos oponentes com a habilidade Unaware

Água
Apenas duas fraquezas (Elétrico e Planta); muito versátil em funções defensivas e ofensivas

Pokémon de Água costumam ter dificuldades contra tipos Planta resistentes

Alomomola utiliza sua tipagem de Água e a habilidade Regenerator para entrar e sair de campo, curando a si mesma e aos aliados

Gelo
Excelente ofensivamente, sendo super efetivo contra Dragões e Voadores

Defensivamente frágil, com muitas fraquezas (Fogo, Aço, Pedra, Lutador)

Baxcalibur (Dragão/Gelo) é uma ameaça ofensiva massiva no tier Uber, mas sua tipagem de Gelo o torna vulnerável a ataques comuns de Pedra e Aço

Exemplos Práticos e Estratégicos
Mudança de Tipagem (Mecânica de Legends: Z-A): No futuro jogo Legends: Z-A, novas Mega Evoluções mudarão a dinâmica das batalhas. Por exemplo, Mega Feraligatr possui
a habilidade Dragonize, que transforma seus movimentos do tipo Normal em movimentos do tipo Dragão, permitindo que ele surpreenda oponentes que esperariam apenas
ataques de Água

Sinergia em Pokémon UNITE: Diferente das batalhas por turnos, no UNITE a vantagem é ditada pela função (role). Um Speedster como Zoroark (tipo Sombrio) foca em 
eliminar alvos frágeis rapidamente, mas sua baixa vida o torna vulnerável se for pego por um Defender robusto como Snorlax

Imunidades Estratégicas: Pokémon como Annihilape (Lutador/Fantasma) utilizam sua tipagem para serem imunes a movimentos de "Giro Rápido" (Normal), permitindo que 
mantenham armadilhas de campo (como Stealth Rock) ativas

Controle de Clima: Tipos Fogo como Ninetales ou Torkoal (mencionado indiretamente via estratégias de sol) aumentam o poder de seus ataques e de aliados ao invocar o 
sol, o que também ativa habilidades como Protosynthesis em Pokémon como Flutter Mane

**Resultado:** Resposta mais estruturada e aplicável.

---

### 🔹 Aprendizados:

* Prompts específicos geram respostas mais úteis
* Solicitar formato (tabela, explicação, análise) melhora a qualidade
* Pedir justificativas aumenta o nível da resposta
* A IA funciona melhor quando recebe contexto claro

---

## 📖 Miniguia de Estudo

### 🧠 Resumo do Tema

As batalhas em Pokémon envolvem estratégia baseada em tipos, habilidades e composição de equipe. Cada tipo possui vantagens e desvantagens, criando um sistema de
equilíbrio que exige planejamento.

A Inteligência Artificial pode auxiliar nesse processo ao:

* Explicar relações entre tipos
* Sugerir estratégias de batalha
* Ajudar na construção de equipes equilibradas
* Simular cenários de combate

---

### ⚔️ Exemplo de Estratégia de Tipos

| Tipo     | Forte contra | Fraco contra |
| -------- | ------------ | ------------ |
| Água     | Fogo         | Elétrico     |
| Fogo     | Planta       | Água         |
| Elétrico | Água         | Terra        |
| Planta   | Água         | Fogo         |

---

### 🧩 Exemplo de Time Estratégico

* Pokémon 1: Tipo Água (ataque principal)
* Pokémon 2: Tipo Elétrico (cobertura contra Água)
* Pokémon 3: Tipo Fogo (contra Planta)
* Pokémon 4: Tipo Terra (contra Elétrico)
* Pokémon 5: Tipo Psíquico (controle)
* Pokémon 6: Tipo Dragão (versatilidade)

👉 Cada escolha busca equilibrar forças e reduzir fraquezas.

---

### 📘 Glossário

* **Tipo:** Categoria do Pokémon que define forças e fraquezas
* **Cobertura:** Capacidade de lidar com diferentes tipos
* **Estratégia:** Planejamento de ações em batalha
* **IA (Inteligência Artificial):** Ferramenta usada para gerar análises e sugestões

---

### 🧠 Prompts Reutilizáveis

* Monte um time competitivo equilibrado
* Explique vantagens entre tipos em tabela
* Analise uma batalha entre dois Pokémon
* Sugira estratégias para vencer determinado tipo
* Crie um guia para iniciantes em batalhas Pokémon

---

## 🚀 Conclusão

Este projeto demonstrou que a Inteligência Artificial pode ser uma ferramenta poderosa para análise estratégica e aprendizado. Ao utilizar Pokémon como contexto, foi
possível aplicar conceitos de lógica, tomada de decisão e otimização de estratégias de forma prática e envolvente.

A experiência também evidenciou a importância da engenharia de prompts para obter respostas mais completas e úteis.
