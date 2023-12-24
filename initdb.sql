CREATE TABLE IF NOT EXISTS roles(
    id INT NOT NULL UNIQUE,
    role VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY ,
    username VARCHAR(50) NOT NULL UNIQUE,
    password TEXT NOT NULL,
    role_id INT,
    CONSTRAINT fk_role_id
      FOREIGN KEY(role_id)
      REFERENCES roles(id)
);

CREATE TABLE IF NOT EXISTS task_lists(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    owner_id BIGINT NOT NULL,
    CONSTRAINT fk_owner_id
      FOREIGN KEY(owner_id)
      REFERENCES users(id)
);


CREATE TABLE IF NOT EXISTS tasks(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    description TEXT,
    list_id BIGINT,
    CONSTRAINT fk_list_id
      FOREIGN KEY(list_id)
      REFERENCES task_lists(id)
      ON DELETE CASCADE
);


INSERT INTO roles VALUES (1, 'user'), (2, 'admin') ON CONFLICT DO NOTHING;
INSERT INTO users (username, password, role_id) VALUES ('admin', '1234', 2) ON CONFLICT DO NOTHING;
