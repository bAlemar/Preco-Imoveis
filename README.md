# Executar o Script em sua máquina local
## Pré-requisitos:

Antes de começar, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.10.12
- pip (gerenciador de pacotes Python)
- Git (ferramenta de controle de versão)

Uma vez que você tenha isso instalado, abra um terminal em sua máquina local e execute os seguintes comandos:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/Preco-Imoveis.git

2. **Navegue até o diretório do repositório clonado:**
   ```bash
   cd Preco-Imoveis

3. **Crie um ambiente virtual:**
   ```bash
    python -m venv ambiente_virtual

4. **Ative o ambiente virtual:**

   **4.1 Linux**
   ```bash
    source ambiente_virtual/bin/activate
   ```
   **4.2 Windows**
   ```bash
    ambiente_virtual\Scripts\activate

5. **Instale as Dependências:**
- Instale de acordo com Dashboard que deseja utilizar.
   ```bash
    pip install -r requeriments.txt 


Antes de rodar um container no seu computador, certifique-se de ter o seguinte instalado em sua máquina:

- Docker version 24.0.7

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/bAlemar/Preco-Imoveis.git

2. **Navegue até o diretório do Docker no repositório clonado:**
   ```bash
   cd Preco-Imoveis/DockerSelenium

3. **Construa sua imagem:**
   ```bash
   docker build -t nome-imagem .
4. **Execute o Contêiner:**
   ```bash
   docker run nome-imagem




