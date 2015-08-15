-- Setup scripts for the FeatursPlus app
DROP DATABASE IF EXISTS db_features;
DROP USER testuser;

CREATE DATABASE db_features;
CREATE USER testuser WITH PASSWORD 'pAssw0rd' LOGIN CREATEDB;

-- Setup for Unit Testing needs
-- CREATE DATABASE db_features template0;
-- GRANT ALL PRIVILEGES ON DATABASE db_features to testuser;
