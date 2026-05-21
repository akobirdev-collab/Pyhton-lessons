CREATE TABLE companies (
  id int PRIMARY KEY,
  name varchar,
  industry varchar,
  created_at datetime
);

CREATE TABLE roles (
  id int PRIMARY KEY,
  name varchar
);

CREATE TABLE users (
  id int PRIMARY KEY,
  company_id int,
  role_id int,
  full_name varchar,
  email varchar,
  created_at datetime
);

CREATE TABLE projects (
  id int PRIMARY KEY,
  company_id int,
  name varchar,
  description text,
  start_date date,
  end_date date
);

CREATE TABLE task_statuses (
  id int PRIMARY KEY,
  name varchar
);

CREATE TABLE tasks (
  id int PRIMARY KEY,
  project_id int,
  assigned_to int,
  status_id int,
  title varchar,
  deadline date
);

CREATE TABLE comments (
  id int PRIMARY KEY,
  task_id int,
  user_id int,
  content text,
  created_at datetime
);

CREATE TABLE files (
  id int PRIMARY KEY,
  task_id int,
  uploaded_by int,
  file_url text
);

CREATE TABLE activity_logs (
  id int PRIMARY KEY,
  user_id int,
  action text,
  created_at datetime
);


ALTER TABLE users ADD FOREIGN KEY (company_id) REFERENCES companies(id);
ALTER TABLE users ADD FOREIGN KEY (role_id) REFERENCES roles(id);

ALTER TABLE projects ADD FOREIGN KEY (company_id) REFERENCES companies(id);

ALTER TABLE tasks ADD FOREIGN KEY (project_id) REFERENCES projects(id);
ALTER TABLE tasks ADD FOREIGN KEY (assigned_to) REFERENCES users(id);
ALTER TABLE tasks ADD FOREIGN KEY (status_id) REFERENCES task_statuses(id);

ALTER TABLE comments ADD FOREIGN KEY (task_id) REFERENCES tasks(id);
ALTER TABLE comments ADD FOREIGN KEY (user_id) REFERENCES users(id);

ALTER TABLE files ADD FOREIGN KEY (task_id) REFERENCES tasks(id);
ALTER TABLE files ADD FOREIGN KEY (uploaded_by) REFERENCES users(id);

ALTER TABLE activity_logs ADD FOREIGN KEY (user_id) REFERENCES users(id);