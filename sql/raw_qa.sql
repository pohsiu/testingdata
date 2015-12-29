/*
Navicat MySQL Data Transfer

Source Server         : local
Source Server Version : 50626
Source Host           : localhost:3306
Source Database       : toy_union

Target Server Type    : MYSQL
Target Server Version : 50626
File Encoding         : 65001

Date: 2015-12-18 14:31:20
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `raw_qa`
-- ----------------------------
DROP TABLE IF EXISTS `raw_qa`;
CREATE TABLE `raw_qa` (
  `ID` int(10) NOT NULL,
  `Asin` varchar(50) DEFAULT NULL,
  `AmazonID` int(10) DEFAULT NULL,
  `Question` text,
  `Ans` text,
  `Date` text,
  `votes` text,
  `Writer` text,
  `Asker` text,
  `AskDate` text,
  UNIQUE KEY `Asin_Date_Writer_Question_Ans_Asker` (`Asin`,`Date`(10),`Writer`(100),`Question`(100),`Ans`(100),`Asker`(100))
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of raw_qa
-- ----------------------------
