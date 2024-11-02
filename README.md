# booklist-api

REST API para Gerenciamento de Livros com Django Ninja
Bem-vindo à BookList API! Esta API foi desenvolvida utilizando o framework Django Ninja, focado em oferecer um conjunto de endpoints para gerenciar uma lista de livros com funcionalidades práticas e intuitivas. O objetivo principal é permitir que os usuários possam cadastrar, avaliar, comentar e até mesmo obter sugestões de leitura aleatórias.

Tecnologias Utilizadas
Python: Linguagem de programação principal
Django: Framework web para backend
Django Ninja: Framework para criação de APIs rápidas e eficientes
Banco de Dados: SQLite (ou configure para outro banco, se necessário)
Funcionalidades
A BookList API oferece as seguintes funcionalidades:

Cadastro de Livros:

O usuário pode adicionar um novo livro à lista, fornecendo os seguintes dados:
Nome do Livro: Título do livro.
Plataforma de Leitura: Onde o livro está disponível (ex.: Amazon Kindle, Físico).
Categorias: Gêneros ou categorias do livro (ex.: Ficção, Romance, História).
Avaliação e Comentário:

Os usuários podem atribuir uma nota ao livro e deixar um comentário, proporcionando um feedback para futuras consultas.
Remoção de Livros:

A API permite a exclusão de livros específicos da lista, mantendo o banco de dados atualizado e relevante.
Sorteio de Livro para Leitura:

Quando solicitada, a API realiza uma seleção aleatória entre os livros cadastrados, sugerindo um título para a próxima leitura.
Documentação dos Endpoints
Abaixo estão os principais endpoints da API, juntamente com exemplos de como utilizá-los. Consulte a documentação completa e interativa gerada automaticamente pelo Django Ninja em /api/docs para detalhes sobre cada endpoint.

## Endpoints

| Método | Endpoint               | Descrição                                                                                                  |
|--------|-------------------------|------------------------------------------------------------------------------------------------------------|
| POST   | `/api/livros/`          | Adiciona um novo livro com nome, streaming e categorias. Streaming deve ser `F` (Físico) ou `AK` (Amazon Kindle). |
| PUT    | `/api/livros/{livro_id}` | Avalia um livro específico, adicionando nota e comentário.                                                |
| DELETE | `/api/livros/{livro_id}` | Remove um livro da lista pelo ID.                                                                         |
| GET    | `/api/livros/sortear/`   | Retorna um livro aleatório para leitura, filtrando por nota mínima, categoria e se deve ser um livro não lido (reler=false). |

