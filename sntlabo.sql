DROP DATABASE IF EXISTS sntlabo;
CREATE DATABASE sntlabo;
USE sntlabo;


CREATE TABLE role(
   id_role INT AUTO_INCREMENT,
   role VARCHAR(50),
   PRIMARY KEY(id_role)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE unite(
   id_unite INT AUTO_INCREMENT,
   nom_unite VARCHAR(50),
   region VARCHAR(50) CHECK(region IN ('STRASBOURG','RENNES','MARSEILLE','GRENOBLE','BORDEAUX','TOULOUSE') ),
   PRIMARY KEY(id_unite)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE utilisateur(
   id_utilisateur INT AUTO_INCREMENT,
   nom_utilisateur VARCHAR(50),
   prenom_utilisateur VARCHAR(50),
   email_utilisateur VARCHAR(50),
   numtel_utilisateur INT,
   date_debut DATE,
   ville_utilisateur VARCHAR(50),
   code_projet VARCHAR(50),
   password_hash VARCHAR(100),
   id_role INT NOT NULL,
   PRIMARY KEY(id_utilisateur),
   FOREIGN KEY(id_role) REFERENCES role(id_role) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE appartient(
   id_utilisateur INT,
   id_unite INT,
   PRIMARY KEY(id_utilisateur, id_unite),
   FOREIGN KEY(id_utilisateur) REFERENCES utilisateur(id_utilisateur) ON DELETE CASCADE,
   FOREIGN KEY(id_unite) REFERENCES unite(id_unite) ON DELETE CASCADE
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
