/*
Navicat MySQL Data Transfer

Source Server         : localhost-mysql
Source Server Version : 50719
Source Host           : localhost:3306
Source Database       : pythondb

Target Server Type    : MYSQL
Target Server Version : 50719
File Encoding         : 65001

Date: 2018-06-09 13:59:51
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for movie
-- ----------------------------
DROP TABLE IF EXISTS `movie`;
CREATE TABLE `movie` (
  `num` varchar(40) DEFAULT NULL,
  `name` varchar(40) DEFAULT NULL,
  `score` varchar(40) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
