-- Table des utilisateurs
CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(64) NOT NULL UNIQUE,
  email VARCHAR(120) NOT NULL UNIQUE,
  password_hash VARCHAR(256) NOT NULL,
  role VARCHAR(20) DEFAULT 'member',
  created DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Table des projets
CREATE TABLE projects (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(128) NOT NULL,
  description TEXT,
  start_date DATE,
  end_date DATE,
  completed BOOLEAN DEFAULT FALSE,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  owner_id INT,
  FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE SET NULL
);

-- Table des tâches
CREATE TABLE tasks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  title VARCHAR(140) NOT NULL,
  description TEXT,
  status VARCHAR(20) DEFAULT 'todo', -- todo, in_progress, done
  priority VARCHAR(10) DEFAULT 'medium', -- low, medium, high
  due_date DATE,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  project_id INT,
  FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE
);

-- Table des affectations (utilisateur <-> tâche)
CREATE TABLE assignments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT NOT NULL,
  task_id INT NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE,
  UNIQUE(user_id, task_id)
);

-- Table des commentaires (facultatif mais utile pour la collaboration)
CREATE TABLE comments (
  id INT AUTO_INCREMENT PRIMARY KEY,
  content TEXT NOT NULL,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  user_id INT,
  task_id INT,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL,
  FOREIGN KEY (task_id) REFERENCES tasks(id) ON DELETE CASCADE
);
