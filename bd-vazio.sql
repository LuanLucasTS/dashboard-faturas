-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: bd-vazio
-- ------------------------------------------------------
-- Server version	11.2.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `faturas_abril`
--

DROP TABLE IF EXISTS `faturas_abril`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_abril` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_abril`
--

LOCK TABLES `faturas_abril` WRITE;
/*!40000 ALTER TABLE `faturas_abril` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_abril` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_agosto`
--

DROP TABLE IF EXISTS `faturas_agosto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_agosto` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_agosto`
--

LOCK TABLES `faturas_agosto` WRITE;
/*!40000 ALTER TABLE `faturas_agosto` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_agosto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_dezembro`
--

DROP TABLE IF EXISTS `faturas_dezembro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_dezembro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_dezembro`
--

LOCK TABLES `faturas_dezembro` WRITE;
/*!40000 ALTER TABLE `faturas_dezembro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_dezembro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_fevereiro`
--

DROP TABLE IF EXISTS `faturas_fevereiro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_fevereiro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_fevereiro`
--

LOCK TABLES `faturas_fevereiro` WRITE;
/*!40000 ALTER TABLE `faturas_fevereiro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_fevereiro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_janeiro`
--

DROP TABLE IF EXISTS `faturas_janeiro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_janeiro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_janeiro`
--

LOCK TABLES `faturas_janeiro` WRITE;
/*!40000 ALTER TABLE `faturas_janeiro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_janeiro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_julho`
--

DROP TABLE IF EXISTS `faturas_julho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_julho` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_julho`
--

LOCK TABLES `faturas_julho` WRITE;
/*!40000 ALTER TABLE `faturas_julho` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_julho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_junho`
--

DROP TABLE IF EXISTS `faturas_junho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_junho` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_junho`
--

LOCK TABLES `faturas_junho` WRITE;
/*!40000 ALTER TABLE `faturas_junho` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_junho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_maio`
--

DROP TABLE IF EXISTS `faturas_maio`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_maio` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_maio`
--

LOCK TABLES `faturas_maio` WRITE;
/*!40000 ALTER TABLE `faturas_maio` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_maio` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_marco`
--

DROP TABLE IF EXISTS `faturas_marco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_marco` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_marco`
--

LOCK TABLES `faturas_marco` WRITE;
/*!40000 ALTER TABLE `faturas_marco` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_marco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_novembro`
--

DROP TABLE IF EXISTS `faturas_novembro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_novembro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_novembro`
--

LOCK TABLES `faturas_novembro` WRITE;
/*!40000 ALTER TABLE `faturas_novembro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_novembro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_outubro`
--

DROP TABLE IF EXISTS `faturas_outubro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_outubro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_outubro`
--

LOCK TABLES `faturas_outubro` WRITE;
/*!40000 ALTER TABLE `faturas_outubro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_outubro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faturas_setembro`
--

DROP TABLE IF EXISTS `faturas_setembro`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faturas_setembro` (
  `id_fatura` int(20) NOT NULL AUTO_INCREMENT,
  `recebida` varchar(5) NOT NULL,
  `gestaotop` varchar(5) NOT NULL,
  `rateio` varchar(5) NOT NULL,
  `fornecedor` int(5) NOT NULL,
  `emitido` date DEFAULT NULL,
  `vencimento` date DEFAULT NULL,
  `nf` text DEFAULT NULL,
  `valor` text DEFAULT NULL,
  `dias_emitido` int(20) DEFAULT NULL,
  `dias_vencimento` int(20) DEFAULT NULL,
  PRIMARY KEY (`id_fatura`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faturas_setembro`
--

LOCK TABLES `faturas_setembro` WRITE;
/*!40000 ALTER TABLE `faturas_setembro` DISABLE KEYS */;
/*!40000 ALTER TABLE `faturas_setembro` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `fornecedor`
--

DROP TABLE IF EXISTS `fornecedor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `fornecedor` (
  `id_fornecedor` int(20) NOT NULL AUTO_INCREMENT,
  `razao_social` varchar(100) DEFAULT NULL,
  `nome_fantasia` varchar(100) DEFAULT NULL,
  `descricao` varchar(100) DEFAULT NULL,
  `telefone` varchar(30) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `contato` varchar(100) DEFAULT NULL,
  `cep` text NOT NULL,
  `rua` varchar(100) DEFAULT NULL,
  `numero` text NOT NULL,
  `complemento` varchar(100) DEFAULT NULL,
  `bairro` varchar(100) DEFAULT NULL,
  `cidade` varchar(100) DEFAULT NULL,
  `uf` varchar(100) DEFAULT NULL,
  `informacao_adicional` text DEFAULT NULL,
  `rateio` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`id_fornecedor`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `fornecedor`
--

LOCK TABLES `fornecedor` WRITE;
/*!40000 ALTER TABLE `fornecedor` DISABLE KEYS */;
/*!40000 ALTER TABLE `fornecedor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `log_login`
--

DROP TABLE IF EXISTS `log_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `log_login` (
  `id_log_login` int(20) NOT NULL AUTO_INCREMENT,
  `usuario` varchar(50) DEFAULT NULL,
  `data_login` varchar(50) DEFAULT NULL,
  `tipo` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_log_login`)
) ENGINE=InnoDB AUTO_INCREMENT=161 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `log_login`
--

LOCK TABLES `log_login` WRITE;
/*!40000 ALTER TABLE `log_login` DISABLE KEYS */;
/*!40000 ALTER TABLE `log_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sistema`
--

DROP TABLE IF EXISTS `sistema`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sistema` (
  `id_sistema` int(4) NOT NULL AUTO_INCREMENT,
  `versao` varchar(15) NOT NULL,
  `token_github` varchar(50) NOT NULL,
  `validade_token` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_sistema`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sistema`
--

LOCK TABLES `sistema` WRITE;
/*!40000 ALTER TABLE `sistema` DISABLE KEYS */;
/*!40000 ALTER TABLE `sistema` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `usuarios`
--

DROP TABLE IF EXISTS `usuarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `usuarios` (
  `id_usuario` int(4) NOT NULL AUTO_INCREMENT,
  `nome` varchar(100) NOT NULL,
  `usuario` varchar(50) NOT NULL,
  `senha` varchar(100) NOT NULL,
  `email` varchar(100) DEFAULT NULL,
  `token` varchar(100) DEFAULT NULL,
  `expira` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_bin;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `usuarios`
--

LOCK TABLES `usuarios` WRITE;
/*!40000 ALTER TABLE `usuarios` DISABLE KEYS */;
INSERT INTO `usuarios` VALUES (1,'Admin','super.user','$2b$12$tSqn2CSVbcz5npVK5mEOWOLUSIdoDdOUYy1v7NarMtFx3zPynPdvG','luanlucascorp@gmail.com',NULL,NULL);
/*!40000 ALTER TABLE `usuarios` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'bd-vazio'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-01-25 11:24:14
