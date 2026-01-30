# 🎵 Minerva Hits - Billboard Charts

Uma aplicação web interativa para explorar as melhores músicas do Billboard Hot 100 em estilo Spotify.

## 📋 Sobre o Projeto

**Minerva Hits** é um aplicativo desenvolvido com **Streamlit** que apresenta o **Top 10 das músicas mais populares** em um formato elegante e responsivo. A interface utiliza um tema escuro inspirado no Spotify, com cards interativos que exibem capa do álbum, título da música, artista e um botão direto para ouvir no Spotify.

O aplicativo permite filtrar as músicas por **ano e mês**, facilitando a exploração de tendências musicais em diferentes períodos.

## ✨ Funcionalidades

- 🎯 **Visualização do Top 10** - Exibe as 10 músicas mais populares
- 📅 **Filtros Dinâmicos** - Selecione ano e mês na barra lateral
- 🎨 **Design Moderno** - Interface inspirada no Spotify com tema escuro
- 🔗 **Integração Spotify** - Links diretos para ouvir cada música
- 🖼️ **Capas de Álbuns** - Exibição visual com imagens
- 📊 **Dados Gerados Automaticamente** - Sistema que cria dados de exemplo se necessário

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/vinizpl/minerva-app.git
cd minerva-app
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv .venv
source .venv/bin/activate  # No Windows: .venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Executar a Aplicação

```bash
streamlit run app.py
```

A aplicação abrirá automaticamente no navegador padrão em `http://localhost:8501`

## 📦 Dependências

- **streamlit** - Framework para construir aplicações web interativas
- **pandas** - Manipulação e análise de dados
- **numpy** - Computação numérica

## 📁 Estrutura do Projeto

```
minerva-app/
├── app.py                      # Arquivo principal da aplicação
├── billboard_hot_100.csv       # Dados das músicas (gerado automaticamente)
├── requirements.txt            # Dependências Python
├── README.md                   # Este arquivo
├── LICENSE                     # Licença do projeto
└── Imagens/                    # Pasta de imagens
```

## 🎨 Interface

### Componentes Principais

1. **Barra Lateral (Sidebar)**
   - Filtro de Ano
   - Filtro de Mês (1-12)

2. **Área Principal**
   - Título: "🎵 Minerva Hits Billboard Charts"
   - Cards das músicas com:
     - Posição no ranking
     - Capa do álbum
     - Título da música
     - Nome do artista
     - Botão "OUVIR" (link Spotify)

### Estilo

- **Tema**: Escuro (inspirado no Spotify)
- **Cor Primária**: Verde Spotify (#1DB954)
- **Cores de Fundo**: Preto (#121212) e Cinza Escuro (#1e1e1e)

## 📊 Dados

O arquivo `billboard_hot_100.csv` contém:
- **date**: Data do ranking (semana)
- **title**: Título da música
- **artist**: Nome do artista
- **rank**: Posição no ranking (1-10)
- **spotify_url**: Link direto para o Spotify
- **img_url**: URL da capa do álbum

### Geração Automática de Dados

Se o arquivo CSV não existir, a aplicação gera automaticamente dados de exemplo com:
- Período: 01/01/2020 a 31/12/2025
- 10 músicas populares no pool de dados
- Rankings aleatórios para cada semana

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 👤 Autor

Desenvolvido por **vinizpl**

## 📧 Suporte

Para dúvidas ou problemas, abra uma issue no repositório do projeto.

---

**Aproveite e descubra as melhores músicas do momento! 🎶**

