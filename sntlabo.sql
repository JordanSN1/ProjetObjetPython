DROP DATABASE IF EXISTS `projetsntlabo`;
CREATE DATABASE `projetsntlabo`;

DROP TABLE IF EXISTS `professionnels`;
CREATE TABLE IF NOT EXISTS `professionnels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `adresse_mail` varchar(100) NOT NULL,
  `numero_telephone` varchar(20) NOT NULL,
  `code_projet` varchar(20) DEFAULT NULL,
  `type_professionnel` enum('chercheur','medecin','commercial','assistant') NOT NULL,
  `Password_hachee` varchar(255) DEFAULT NULL,
  `Bannis` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;

DROP TABLE IF EXISTS `professionnels_unites`;
CREATE TABLE IF NOT EXISTS `professionnels_unites` (
  `id_professionnel` int DEFAULT NULL,
  `id_unite` int DEFAULT NULL,
  KEY `id_professionnel` (`id_professionnel`),
  KEY `id_unite` (`id_unite`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;


DROP TABLE IF EXISTS `responsables_scientifiques`;
CREATE TABLE IF NOT EXISTS `responsables_scientifiques` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_professionnel` int DEFAULT NULL,
  `date_prise_fonction` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_professionnel` (`id_professionnel`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;;



DROP TABLE IF EXISTS `unites`;
CREATE TABLE IF NOT EXISTS `unites` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `equipements_modernes` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

