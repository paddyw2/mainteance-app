-- MySQL dump 10.13  Distrib 5.7.21, for osx10.13 (x86_64)
--
-- Host: localhost    Database: 471_project
-- ------------------------------------------------------
-- Server version	5.7.21

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `available`
--

DROP TABLE IF EXISTS `available`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `available` (
  `available_id` int(32) NOT NULL AUTO_INCREMENT,
  `pos_id` int(32) DEFAULT NULL,
  `backroom_id` int(32) DEFAULT NULL,
  `sale_price` varchar(32) DEFAULT NULL,
  `car_condition` varchar(25) DEFAULT NULL,
  `next_repair` date DEFAULT NULL,
  PRIMARY KEY (`available_id`),
  KEY `fk_pos` (`pos_id`),
  KEY `fk_backroom` (`backroom_id`),
  CONSTRAINT `available_ibfk_1` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`pos_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `available_ibfk_2` FOREIGN KEY (`backroom_id`) REFERENCES `backroom` (`backroom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `available`
--

LOCK TABLES `available` WRITE;
/*!40000 ALTER TABLE `available` DISABLE KEYS */;
INSERT INTO `available` VALUES (1,NULL,2,'40,000','Good','2018-05-20');
/*!40000 ALTER TABLE `available` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backroom`
--

DROP TABLE IF EXISTS `backroom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backroom` (
  `backroom_id` int(32) NOT NULL AUTO_INCREMENT,
  `event_id` int(32) NOT NULL,
  `assigned_to` int(100) DEFAULT NULL,
  PRIMARY KEY (`backroom_id`),
  KEY `fk_event` (`event_id`),
  KEY `fk_assigned_to` (`assigned_to`),
  CONSTRAINT `backroom_ibfk_1` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `backroom_ibfk_2` FOREIGN KEY (`assigned_to`) REFERENCES `user` (`employee_no`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backroom`
--

LOCK TABLES `backroom` WRITE;
/*!40000 ALTER TABLE `backroom` DISABLE KEYS */;
INSERT INTO `backroom` VALUES (1,2,123123),(2,3,NULL);
/*!40000 ALTER TABLE `backroom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `car`
--

DROP TABLE IF EXISTS `car`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `car` (
  `vin_no` int(32) NOT NULL,
  `make` varchar(100) DEFAULT NULL,
  `model` varchar(100) DEFAULT NULL,
  `license_plate` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`vin_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `car`
--

LOCK TABLES `car` WRITE;
/*!40000 ALTER TABLE `car` DISABLE KEYS */;
INSERT INTO `car` VALUES (32145,'toyota','corolla','P238NM',NULL,NULL),(123456,'ford','f150','T2R123',NULL,NULL),(459827,'chevrolet','camaro','RF2319',NULL,NULL);
/*!40000 ALTER TABLE `car` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `customer` (
  `license_no` varchar(100) NOT NULL,
  `phone_no` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `address` varchar(250) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`license_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('12FG992','5871231234','John','Doe',NULL,NULL);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `event`
--

DROP TABLE IF EXISTS `event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `event` (
  `event_id` int(32) NOT NULL AUTO_INCREMENT,
  `car_vin` int(32) NOT NULL,
  `created_by` int(100) DEFAULT NULL,
  `description` varchar(250) NOT NULL,
  `title` varchar(100) NOT NULL,
  `status` varchar(100) DEFAULT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`event_id`),
  KEY `fk_vin` (`car_vin`),
  KEY `fk_created_by` (`created_by`),
  CONSTRAINT `event_ibfk_1` FOREIGN KEY (`car_vin`) REFERENCES `car` (`vin_no`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `event_ibfk_2` FOREIGN KEY (`created_by`) REFERENCES `user` (`employee_no`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `event`
--

LOCK TABLES `event` WRITE;
/*!40000 ALTER TABLE `event` DISABLE KEYS */;
INSERT INTO `event` VALUES (1,32145,2345223,'This is a rental event','Rental',NULL,'2018-04-25',NULL),(2,123456,2345223,'Windshield repair required for a Ford truck','Truck repair',NULL,'2018-04-20',NULL),(3,459827,2345223,'This car is available to rent','Chevrolet is available',NULL,'2018-04-01',NULL);
/*!40000 ALTER TABLE `event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inspection`
--

DROP TABLE IF EXISTS `inspection`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inspection` (
  `inspection_id` int(32) NOT NULL AUTO_INCREMENT,
  `backroom_id` int(32) NOT NULL,
  `est_finish_date` date DEFAULT NULL,
  `next_inspection` date DEFAULT NULL,
  `work_done` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`inspection_id`),
  KEY `fk_backroom` (`backroom_id`),
  CONSTRAINT `inspection_ibfk_1` FOREIGN KEY (`backroom_id`) REFERENCES `backroom` (`backroom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inspection`
--

LOCK TABLES `inspection` WRITE;
/*!40000 ALTER TABLE `inspection` DISABLE KEYS */;
/*!40000 ALTER TABLE `inspection` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pos`
--

DROP TABLE IF EXISTS `pos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `pos` (
  `pos_id` int(32) NOT NULL AUTO_INCREMENT,
  `event_id` int(32) NOT NULL,
  `license_no` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`pos_id`),
  KEY `fk_license` (`license_no`),
  KEY `fk_event` (`event_id`),
  CONSTRAINT `pos_ibfk_1` FOREIGN KEY (`license_no`) REFERENCES `customer` (`license_no`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `pos_ibfk_2` FOREIGN KEY (`event_id`) REFERENCES `event` (`event_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pos`
--

LOCK TABLES `pos` WRITE;
/*!40000 ALTER TABLE `pos` DISABLE KEYS */;
INSERT INTO `pos` VALUES (1,1,'12FG992');
/*!40000 ALTER TABLE `pos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rental`
--

DROP TABLE IF EXISTS `rental`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rental` (
  `rental_id` int(32) NOT NULL AUTO_INCREMENT,
  `pos_id` int(32) NOT NULL,
  `problems` varchar(25) DEFAULT NULL,
  `est_return` date DEFAULT NULL,
  PRIMARY KEY (`rental_id`),
  KEY `fk_pos` (`pos_id`),
  CONSTRAINT `rental_ibfk_1` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`pos_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rental`
--

LOCK TABLES `rental` WRITE;
/*!40000 ALTER TABLE `rental` DISABLE KEYS */;
INSERT INTO `rental` VALUES (1,1,NULL,'2018-04-28');
/*!40000 ALTER TABLE `rental` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repair`
--

DROP TABLE IF EXISTS `repair`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `repair` (
  `repair_id` int(32) NOT NULL AUTO_INCREMENT,
  `backroom_id` int(32) NOT NULL,
  `est_finish_date` date DEFAULT NULL,
  `description` varchar(250) DEFAULT NULL,
  `parts_list` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`repair_id`),
  KEY `fk_backroom` (`backroom_id`),
  CONSTRAINT `repair_ibfk_1` FOREIGN KEY (`backroom_id`) REFERENCES `backroom` (`backroom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repair`
--

LOCK TABLES `repair` WRITE;
/*!40000 ALTER TABLE `repair` DISABLE KEYS */;
INSERT INTO `repair` VALUES (1,1,'2018-04-30','The windshield has been ordered, still needs to be installed','Windshield');
/*!40000 ALTER TABLE `repair` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sale`
--

DROP TABLE IF EXISTS `sale`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sale` (
  `sale_id` int(32) NOT NULL AUTO_INCREMENT,
  `pos_id` int(32) NOT NULL,
  `price` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`sale_id`),
  KEY `fk_pos` (`pos_id`),
  CONSTRAINT `sale_ibfk_1` FOREIGN KEY (`pos_id`) REFERENCES `pos` (`pos_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sale`
--

LOCK TABLES `sale` WRITE;
/*!40000 ALTER TABLE `sale` DISABLE KEYS */;
/*!40000 ALTER TABLE `sale` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `employee_no` int(100) NOT NULL,
  `phone_no` varchar(100) NOT NULL,
  `fname` varchar(100) NOT NULL,
  `lname` varchar(100) NOT NULL,
  `is_admin` int(10) NOT NULL,
  `address` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`employee_no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (123123,'18002472001','Jane','Doe',0,NULL),(2345223,'5871231234','Jimmy','Doe',1,NULL);
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `writeoff`
--

DROP TABLE IF EXISTS `writeoff`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `writeoff` (
  `writeoff_id` int(32) NOT NULL AUTO_INCREMENT,
  `backroom_id` int(32) NOT NULL,
  `reason` varchar(250) DEFAULT NULL,
  PRIMARY KEY (`writeoff_id`),
  KEY `fk_backroom` (`backroom_id`),
  CONSTRAINT `writeoff_ibfk_1` FOREIGN KEY (`backroom_id`) REFERENCES `backroom` (`backroom_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `writeoff`
--

LOCK TABLES `writeoff` WRITE;
/*!40000 ALTER TABLE `writeoff` DISABLE KEYS */;
/*!40000 ALTER TABLE `writeoff` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-04-17 10:21:46
