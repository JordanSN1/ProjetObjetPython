-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Generation Time: Feb 13, 2024 at 11:13 AM
-- Server version: 8.0.31
-- PHP Version: 8.0.26

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sntlabo`
--

-- --------------------------------------------------------

--
-- Table structure for table `professionnels`
--

DROP TABLE IF EXISTS `professionnels`;
CREATE TABLE IF NOT EXISTS `professionnels` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL,
  `adresse_mail` varchar(100) NOT NULL,
  `numero_telephone` varchar(20) NOT NULL,
  `code_projet` varchar(20) DEFAULT NULL,
  `type_professionnel` enum('chercheur','medecin','commercial','assistant') NOT NULL,
  `Password_hachee` varchar(255) DEFAULT NULL,
  `Bannis` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `professionnels_unites`
--

DROP TABLE IF EXISTS `professionnels_unites`;
CREATE TABLE IF NOT EXISTS `professionnels_unites` (
  `id_professionnel` int DEFAULT NULL,
  `id_unite` int DEFAULT NULL,
  KEY `id_professionnel` (`id_professionnel`),
  KEY `id_unite` (`id_unite`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `responsables_scientifiques`
--

DROP TABLE IF EXISTS `responsables_scientifiques`;
CREATE TABLE IF NOT EXISTS `responsables_scientifiques` (
  `id` int NOT NULL AUTO_INCREMENT,
  `id_professionnel` int DEFAULT NULL,
  `date_prise_fonction` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `id_professionnel` (`id_professionnel`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `unites`
--

DROP TABLE IF EXISTS `unites`;
CREATE TABLE IF NOT EXISTS `unites` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nom` varchar(50) NOT NULL,
  `region` varchar(50) NOT NULL,
  `equipements_modernes` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
