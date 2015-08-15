-- Setup scripts for the FeatursPlus app
DROP DATABASE IF EXISTS db_features;
CREATE DATABASE db_features;
CREATE USER testuser WITH PASSWORD 'pAssw0rd' LOGIN;

-- Setup for Unit Testing needs
CREATE DATABASE db_features template template0;
GRANT ALL PRIVILEGES ON DATABASE db_features to testuser;
