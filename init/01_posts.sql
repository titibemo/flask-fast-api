-- Création de la table posts
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    author TEXT NOT NULL,
    created_at DATE,
    updated_at DATE
);

-- Insertion des données initiales
INSERT INTO posts (id, title, content, author, created_at, updated_at)
VALUES (
    1,
    'Mon premier article',
    'Ceci est le contenu de mon premier article.',
    'John Doe',
    '2022-01-01',
    '2022-01-01'
);