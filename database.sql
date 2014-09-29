/*
Navicat MySQL Data Transfer

Source Server         : MariaDB Local
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : file_crawler

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2014-09-29 19:32:35
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for files
-- ----------------------------
DROP TABLE IF EXISTS `files`;
CREATE TABLE `files` (
  `fil_id` int(11) NOT NULL AUTO_INCREMENT,
  `fil_key_id` int(11) DEFAULT NULL,
  `fil_name` varchar(255) DEFAULT NULL,
  `fil_url` varchar(255) DEFAULT NULL,
  `fil_path` varchar(255) DEFAULT NULL,
  `fil_downloaded` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`fil_id`)
) ENGINE=InnoDB AUTO_INCREMENT=377 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for keywords
-- ----------------------------
DROP TABLE IF EXISTS `keywords`;
CREATE TABLE `keywords` (
  `key_id` int(11) NOT NULL AUTO_INCREMENT,
  `key_quantity` int(11) DEFAULT NULL,
  `key_keyword` varchar(255) DEFAULT NULL,
  `key_completed` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`key_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
