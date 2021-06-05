-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3306
-- Creato il: Giu 05, 2021 alle 16:33
-- Versione del server: 5.7.31
-- Versione PHP: 7.3.21

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tesi`
--
CREATE DATABASE IF NOT EXISTS `YT_RS` DEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE `YT_RS`;

-- --------------------------------------------------------

--
-- Struttura della tabella `sessione`
--

DROP TABLE IF EXISTS `sessione`;
CREATE TABLE IF NOT EXISTS `sessione` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `setupId` int(4) NOT NULL,
  `startedAt` varchar(20) DEFAULT NULL,
  `finishedAt` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `setupId` (`setupId`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `setupsessione`
--

DROP TABLE IF EXISTS `setupsessione`;
CREATE TABLE IF NOT EXISTS `setupsessione` (
  `id` int(4) NOT NULL AUTO_INCREMENT,
  `account` varchar(40) NOT NULL,
  `tipo` tinyint(4) NOT NULL,
  `query` varchar(100) DEFAULT NULL,
  `steps` int(2) NOT NULL DEFAULT '10',
  `viewTime` smallint(6) NOT NULL,
  `status` varchar(15) NOT NULL DEFAULT 'READY',
  `frequency` text,
  `iterations` int(2) NOT NULL DEFAULT '1' COMMENT 'This value indicates how many times the session will be repeated',
  `executedTimes` int(10) NOT NULL DEFAULT '0',
  `lastExecution` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `video`
--

DROP TABLE IF EXISTS `video`;
CREATE TABLE IF NOT EXISTS `video` (
  `id` varchar(13) NOT NULL,
  `title` varchar(200) NOT NULL,
  `description` text CHARACTER SET utf8mb4 COLLATE utf8mb4_roman_ci NOT NULL,
  `publisher_id` varchar(50) NOT NULL,
  `publisher` varchar(100) NOT NULL,
  `watched_id` varchar(13) DEFAULT NULL,
  `suggested_times` int(3) NOT NULL,
  `categoryId` int(3) DEFAULT NULL,
  `categoryTitle` varchar(30) DEFAULT NULL,
  `idSetup` int(4) NOT NULL,
  UNIQUE KEY `id` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Struttura della tabella `video_sessione`
--

DROP TABLE IF EXISTS `video_sessione`;
CREATE TABLE IF NOT EXISTS `video_sessione` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `videoId` varchar(11) NOT NULL,
  `sessionId` int(4) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `sessionId` (`sessionId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
