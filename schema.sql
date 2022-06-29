DROP TABLE IF EXISTS posts;

CREATE TABLE posts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    tipo TEXT NOT NULL,
    estado TEXT NOT NULL,
    cidade TEXT NOT  NULL,
    rua TEXT NOT NULL,
    numero TEXT NOT NULL,
    telefone TEXT NOT NULL,
    email TEXT NOT NULL,
    redes TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    foto BLOB NOT NULL
);