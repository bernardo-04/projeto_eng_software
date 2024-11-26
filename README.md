<h1>Projeto ESW - Sistema PDV</h1>

<ul>
  <li>
    Este é um sistema PDV (Ponto de Venda) desenvolvido para a disciplina de Engenharia de Softwares
  </li>
  <li>
    O projeto foi desenvolvido em Python e usa a biblioteca 
    <a href="https://github.com/TomSchimansky/CustomTkinter" target="_blank">
      CustomTkinter
    </a>
    para a interface gráfica.
  </li>
</ul>

<h2>Pré-requisitos</h2>
<p>Antes de rodar o projeto, é necessário ter instalado:</p>

<ul>
  <li>
    <a href="https://www.python.org/downloads/" target="_blank">
      Python 3.x
    </a>
  </li>
    <li>
    <a href="https://git-scm.com/downloads" target="_blank">
      Git
    </a>
  </li>
</ul>

<p>Além disso o projeto utiliza um ambiente virtual para gerenciar as dependências, e isso deve ser configurado com o <strong>venv</strong></p>

<h3>1. Clonar o repositório</h3>
<p>Primeiro, você precisa clonar o repositório para sua máquina local. Abra o terminal ou prompt de comando e execute o seguinte comando:
</p>

```bash
git clone https://github.com/bernardo-04/projeto_eng_software.git

cd projeto-esw
```
<h3>2. Criar e ativar o ambiente virtual</h3>
<p>Navegue até a pasta onde o repositório do projeto foi clonado.</p>
<h4>Windows:</h4>
<p>Crie o ambiente virtual com o comando:</p>

```bash
python -m venv venv
```
<p>Ative o ambiente virtual:</p>

```bash
.\venv\Scripts\activate
```
<h4>Linux:</h4>
<p>Crie o ambiente virtual com o comando:</p>

```bash
python3 -m venv venv
```
<p>Ative o ambiente virtual:</p>

```bash
source venv/bin/activate
```
<h3>3. Instalar as dependências</h3>
<p>Com o ambiente virtual ativado, instale as dependências do projeto. Execute o seguinte comando:</p>

```bash
pip install -r requirements.txt
```
<h3>4. Executar o projeto</h3>
<p>Execute o projeto com o seguinte comando:</p>

```bash
python src/views/main.py
```