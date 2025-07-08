
DROP TABLE IF EXISTS users;

-- Tabela de usuários, ainda sujeita a alterações.
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    password_hash VARCHAR(120) NOT NULL,
    profile_pic VARCHAR(255) DEFAULT NULL, -- Caminho para a foto de perfil do usuário
    data_created DATETIME DEFAULT CURRENT_TIMESTAMP
);
