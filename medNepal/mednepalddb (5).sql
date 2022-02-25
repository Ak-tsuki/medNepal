-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Feb 25, 2022 at 08:46 AM
-- Server version: 10.4.20-MariaDB
-- PHP Version: 8.0.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `mednepalddb`
--

-- --------------------------------------------------------

--
-- Table structure for table `accounts_department`
--

CREATE TABLE `accounts_department` (
  `id` bigint(20) NOT NULL,
  `DeptName` varchar(100) NOT NULL,
  `deptPic` varchar(100) NOT NULL,
  `description` longtext DEFAULT NULL,
  `appointmentFee` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_department`
--

INSERT INTO `accounts_department` (`id`, `DeptName`, `deptPic`, `description`, `appointmentFee`) VALUES
(2, 'WednCritical Care Medicine Specialistsesday', 'static/uploads/download.jpg', 'dfdfgdsgfs', 123),
(3, 'Anesthesiologists', 'static/uploads/download_nrq2zCZ.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 300),
(4, 'Cardiologists', 'static/uploads/download_p9eLLeV.jpg', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 1000);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_doctor`
--

CREATE TABLE `accounts_doctor` (
  `user_id` bigint(20) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(200) NOT NULL,
  `departmentName` varchar(100) NOT NULL,
  `hospitalName` varchar(200) NOT NULL,
  `profile_pic` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_doctor`
--

INSERT INTO `accounts_doctor` (`user_id`, `firstname`, `lastname`, `phone`, `address`, `departmentName`, `hospitalName`, `profile_pic`) VALUES
(21, 'David', 'Shah', '9845798454', 'Banepa-07', 'Anesthesiologists', 'Scheer Memorial Hospital', 'static/doctorProfile/usman-yousaf-pTrhfmj2jDA-unsplash.jpg'),
(22, 'Henry', 'Alen', '9855484563', 'Ratnapark,Kathmandu', 'Cardiologists', 'B & B Hospital', 'static/doctorProfile/austin-distel-7bMdiIqz_J4-unsplash.jpg'),
(23, 'Ram', 'Karki', '9748564578', 'Kalanki,Kathmandu', 'Dermatologists', 'Bir Hospital', 'static/doctorProfile/bruno-rodrigues-279xIHymPYY-unsplash.jpg'),
(24, 'Prety', 'Silk', '98454786547', 'Kausaltar,Kathmandu', 'Endocrinologists', 'Medi City Hospital', 'static/doctorProfile/humberto-chavez-FVh_yqLR9eA-unsplash.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_patient`
--

CREATE TABLE `accounts_patient` (
  `user_id` bigint(20) NOT NULL,
  `firstname` varchar(50) NOT NULL,
  `lastname` varchar(50) NOT NULL,
  `phone` varchar(15) NOT NULL,
  `address` varchar(200) NOT NULL,
  `age` int(11) DEFAULT NULL,
  `gender` varchar(50) NOT NULL,
  `profile_pic` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_patient`
--

INSERT INTO `accounts_patient` (`user_id`, `firstname`, `lastname`, `phone`, `address`, `age`, `gender`, `profile_pic`) VALUES
(2, 'tsering', 'sherpa', '0483248923', 'Jyotinagar', 19, 'Male', 'static/default_user.png'),
(7, 'Aaron', 'Thaku', '978923692', 'Ghathaghar', 21, 'Male', 'static/patientProfile/C0344814-Doctor_at_work.jpg'),
(12, 'tsering', 'sherpa', '0483248923', 'Jyotinagar', 22, 'Male', 'static/patientProfile/IMG_2946.JPG'),
(13, 'tsering', 'sherpa', '0483248923', 'Jyotinagar', 21, 'Male', 'static/patientProfile/C0344814-Doctor_at_work_uCYQCBC.jpg'),
(14, 'Rijwol', 'Shakya', '9861291534', 'Banepa-10', 20, 'Male', 'static/patientProfile/1K6A0071.jpg'),
(15, 'Rijwol', 'Shakya', '9861291534', 'Banepa-10', 20, 'Male', 'static/patientProfile/flexon.png'),
(16, 'Rijwol', 'Shakya', '9861291534', 'Banepa-07', 20, 'Male', 'static/patientProfile/2E6A8379.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user`
--

CREATE TABLE `accounts_user` (
  `id` bigint(20) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `is_patient` tinyint(1) NOT NULL,
  `is_doctor` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `accounts_user`
--

INSERT INTO `accounts_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`, `is_patient`, `is_doctor`) VALUES
(1, 'pbkdf2_sha256$260000$P5ipsB1itSjQnpHZ8wLSZ7$xdTuGuK23Gdg4qYS7JOwjARlKh+y8IsNuk5m0QSb9Cc=', '2022-02-25 06:47:05.743894', 1, 'tsering', '', '', '', 1, 1, '2021-12-31 05:18:15.513167', 0, 0),
(2, 'pbkdf2_sha256$260000$l7XFfEioJgXG5UJ8LoF9EB$PfzvhHBxeY9NNa+WRYhrDJmbO5S5Xx1DJWLXZBL1vMY=', NULL, 0, 'tsering12', '', '', 'ts19sherpa@gmail.com', 0, 1, '2021-12-31 11:59:12.817349', 1, 0),
(4, 'pbkdf2_sha256$260000$nTks6LGjUausg0zyiXZJT1$EewLL2SgnfwB7rTYy5gw1nqiBYhoG9xUPJjGuqP3WeI=', '2022-01-03 06:43:20.800629', 0, 'Ram12', '', '', 'ram12@gmail.com', 0, 1, '2021-12-31 12:11:58.315623', 0, 1),
(5, 'pbkdf2_sha256$260000$JsfIyo2YFvSZXmzQ3TUpcF$Xhfc2TcayADM+pjUMrZjQXTuW8ZJKExTFLqsbXYsm4A=', NULL, 0, 'Rijwol12', '', '', 'ts12@gmail.com', 0, 1, '2021-12-31 12:20:44.977814', 0, 1),
(6, 'pbkdf2_sha256$260000$LHH2tHmZEEgRX1fRcyd4At$FOLokC+SKKO3xDYQV8cqhkn2X6ue2TpPpqyalCdE8WQ=', NULL, 0, 'Prassana12', '', '', 'prassana12@gmail.com', 0, 1, '2021-12-31 14:07:35.738563', 0, 1),
(7, 'pbkdf2_sha256$260000$liC2BS6tUVv4YVCuIuw0S2$dupwiTn4Skdbw2ePkLY42KZ9Tjt1mim12ltsoOeEKUM=', NULL, 0, 'Aaron21', '', '', 'aaron1233@gamk.com', 0, 1, '2022-01-01 07:34:35.875145', 1, 0),
(8, 'pbkdf2_sha256$260000$EmsDeDAA3hn6Q4jVPzqElm$rjKpai8CfQyz9jDVw5Z4Yg5ebnbE0quZXKUHRRfgeN4=', NULL, 0, 'Arron23', '', '', 'aaron1233@gamk.com', 0, 1, '2022-01-01 07:37:44.069642', 0, 1),
(9, 'pbkdf2_sha256$260000$eMJtHdYhQHsnYSPAskRGDI$0pFh5Ozt8Bldx5D6rdESj1iPOLkmClQFiN03jlipWtw=', NULL, 0, 'Aayush21', '', '', 'Auyush12@gmail.com', 0, 1, '2022-01-01 07:38:57.907418', 0, 1),
(10, 'pbkdf2_sha256$260000$3N2Z3BhRma7lYRWkE36O79$V+tWzjZROigw8/FZ+6zKnm1ZHLqv6wVSC29hQRk8Lbc=', NULL, 0, 'HenryClide21', '', '', 'ccsdfdfs@gmail.com', 0, 1, '2022-01-01 07:40:15.562875', 0, 1),
(11, 'pbkdf2_sha256$260000$JDZpr846eToDcyMZBBEa5X$F/AvYYRIbWb4YD0Tx06TODX3qsF7BrLvZJ1cWyJPNLY=', '2022-01-04 06:19:58.259330', 0, 'Tsering13', '', '', 'ts19sherpa@gmail.com', 0, 1, '2022-01-03 07:02:46.260926', 0, 1),
(12, 'pbkdf2_sha256$260000$VtdJE3qpWTeCQwbDabxwSP$6NLfHy1pUSdwacFubz6SssFjAuv2lHt1E9i3Ua326hA=', '2022-01-06 08:26:46.837793', 0, 'tsering21', '', '', 'ts19sherpa@gmail.com', 0, 1, '2022-01-06 08:25:38.956195', 1, 0),
(13, 'pbkdf2_sha256$260000$1YUmtnZt9X7wQqwqPA19AP$qQYzxveqcYHP13NT2IDwEfldtzDmfMDY+MkM6rAAODs=', '2022-01-10 06:29:18.026727', 0, 'tsering11', '', '', 'ts19sherpa@gmail.com', 0, 1, '2022-01-10 06:29:06.209964', 1, 0),
(14, 'pbkdf2_sha256$260000$g8dhcRq0GlXjVAV8xyKz3F$K8JJ8j3KY64t4qm/RAVRlJyiL5eteQptQmM+mGKJ6N4=', '2022-02-02 14:05:48.816234', 0, 'rijwolshakya19', '', '', 'shakyarijwol09@gmail.com', 0, 1, '2022-01-10 07:07:26.273423', 1, 0),
(15, 'pbkdf2_sha256$260000$qTeG1WRhApTClzTnbVZ6o1$xmjyQw60GZwnuP4R+Llu/t5psknA1m4rKoHyxacO4Oc=', '2022-02-25 06:36:10.688617', 0, 'shakyarijwol', '', '', 'shakyarijwol09@gmail.com', 0, 1, '2022-01-11 06:46:33.377639', 1, 0),
(16, 'pbkdf2_sha256$260000$tOT2RmEyxxdPGjBGHdN1TE$7IaK8EMzcORU/bY1tYDALEiRhd0/wAvxsFroOihmyAg=', '2022-02-25 06:49:42.886811', 0, 'shakya09', '', '', 'shakyarijwol09@gmail.com', 0, 1, '2022-01-31 11:07:21.960456', 1, 0),
(17, 'pbkdf2_sha256$260000$HVXwdMYkdQnc5Dzsxvwade$t1b7RLGKhtpA8aXTODCmKKfXv/Q64Uf19kjMI60/odM=', NULL, 0, 'naruto09', '', '', 'naruto09@gmail.com', 0, 1, '2022-02-13 07:00:13.005374', 0, 1),
(18, 'pbkdf2_sha256$260000$HoHz5uBFSs7PWIlQhOOsTL$OP0SDBs1ACEKk6FUn87beOZrPYCq2NkAK9fTB823HcU=', NULL, 0, 'naruto19', '', '', 'naruto19@gmail.com', 0, 1, '2022-02-13 07:03:16.030301', 0, 1),
(19, 'pbkdf2_sha256$260000$NjzwRfCUGPXR95GzI16vkV$oxM1r4oA1NcZU9qtuthOQI86JGI1Y7HFZuwRireUo3g=', NULL, 0, 'naruto10', '', '', 'naruto10@gmail.com', 0, 1, '2022-02-13 07:05:23.110867', 0, 1),
(20, 'pbkdf2_sha256$260000$oL1evJvOisLAq9LosbSKh8$1PQhICNTNJyZ6WOA+OcYnEvAL201dQ2I9NVt10YZBEc=', NULL, 0, 'naruto11', '', '', 'naruto11@gmail.com', 0, 1, '2022-02-13 07:07:11.161104', 0, 1),
(21, 'pbkdf2_sha256$260000$PXstfJXtQdrbIIjz6wq1iG$hwkyFrrVNpHI+wWlxTXJoOOnfAkB+OkPbtI9NnqJLh8=', '2022-02-25 06:45:31.705113', 0, 'davidshah', '', '', 'davidsingh@gmail.com', 0, 1, '2022-02-13 07:11:32.791076', 0, 1),
(22, 'pbkdf2_sha256$260000$hwtSnocEMpW4EYXuJ2GSix$b/OgsOmLNJsyVe1rFNyASKS3PXPcjyZuoEuIM4wCK6k=', NULL, 0, 'henryalen', '', '', 'henryalen@gmail.com', 0, 1, '2022-02-13 07:13:16.942128', 0, 1),
(23, 'pbkdf2_sha256$260000$gwZsWaW2f3scqD4kVYpNBW$wV4norppU7PnoAVCMuDzzre+g/hcM3RGPb1PR9xprCM=', NULL, 0, 'ramkarki', '', '', 'ramkarki@gmail.com', 0, 1, '2022-02-13 07:15:19.030387', 0, 1),
(24, 'pbkdf2_sha256$260000$kEPoIg8VZAoxD9c0QUDRmz$O8OnY5cyN3HnzKnZLS15/GBGZedWv2/yXLjA/7BOCAo=', NULL, 0, 'pretysilk', '', '', 'pretysilk@gmail.com', 0, 1, '2022-02-13 07:16:20.621888', 0, 1);

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_groups`
--

CREATE TABLE `accounts_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `accounts_user_user_permissions`
--

CREATE TABLE `accounts_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `admins_article`
--

CREATE TABLE `admins_article` (
  `id` bigint(20) NOT NULL,
  `article_image` varchar(100) DEFAULT NULL,
  `article_title` varchar(200) NOT NULL,
  `article_brief` longtext NOT NULL,
  `article_sub_brief` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `admins_medicine`
--

CREATE TABLE `admins_medicine` (
  `id` bigint(20) NOT NULL,
  `medicine_name` varchar(200) NOT NULL,
  `medicine_price` double NOT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `category_id` bigint(20) DEFAULT NULL,
  `medicine_image` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins_medicine`
--

INSERT INTO `admins_medicine` (`id`, `medicine_name`, `medicine_price`, `created_date`, `category_id`, `medicine_image`) VALUES
(2, 'Flexon', 200, '2022-01-10 07:14:34.409910', 1, 'static/medicine_uploads/flexon_V4X4MIp.png'),
(3, 'DeCold', 180, '2022-01-10 07:14:51.792604', 1, 'static/medicine_uploads/decold_NjMrIU0.jfif'),
(4, 'Bandage', 250, '2022-01-10 07:15:08.290823', 2, 'static/medicine_uploads/bandage_V9I90ms.jpg'),
(5, 'First Aid', 500, '2022-01-10 07:15:22.596787', 2, 'static/medicine_uploads/firstaid_lyI2oc8.jpg'),
(6, 'HandyPlast', 20, '2022-01-10 07:15:34.021894', 2, 'static/medicine_uploads/handyplast_WdE0cfv.jpg'),
(7, 'Paracetamol', 100, '2022-02-25 06:48:26.218189', 1, 'static/medicine_uploads/paracetamol_vJKRMWa.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `admins_medicinecategory`
--

CREATE TABLE `admins_medicinecategory` (
  `id` bigint(20) NOT NULL,
  `med_category_name` varchar(200) DEFAULT NULL,
  `category_brief` longtext NOT NULL,
  `created_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admins_medicinecategory`
--

INSERT INTO `admins_medicinecategory` (`id`, `med_category_name`, `category_brief`, `created_date`) VALUES
(1, 'Common Medicine', 'Common Medicine', '2022-01-10 07:13:27.930115'),
(2, 'Health Suppliments', 'Medicine For Health', '2022-01-10 07:13:40.816492');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add content type', 4, 'add_contenttype'),
(14, 'Can change content type', 4, 'change_contenttype'),
(15, 'Can delete content type', 4, 'delete_contenttype'),
(16, 'Can view content type', 4, 'view_contenttype'),
(17, 'Can add session', 5, 'add_session'),
(18, 'Can change session', 5, 'change_session'),
(19, 'Can delete session', 5, 'delete_session'),
(20, 'Can view session', 5, 'view_session'),
(21, 'Can add user', 6, 'add_user'),
(22, 'Can change user', 6, 'change_user'),
(23, 'Can delete user', 6, 'delete_user'),
(24, 'Can view user', 6, 'view_user'),
(25, 'Can add department', 7, 'add_department'),
(26, 'Can change department', 7, 'change_department'),
(27, 'Can delete department', 7, 'delete_department'),
(28, 'Can view department', 7, 'view_department'),
(29, 'Can add doctor', 8, 'add_doctor'),
(30, 'Can change doctor', 8, 'change_doctor'),
(31, 'Can delete doctor', 8, 'delete_doctor'),
(32, 'Can view doctor', 8, 'view_doctor'),
(33, 'Can add patient', 9, 'add_patient'),
(34, 'Can change patient', 9, 'change_patient'),
(35, 'Can delete patient', 9, 'delete_patient'),
(36, 'Can view patient', 9, 'view_patient'),
(37, 'Can add doctor profile', 10, 'add_doctorprofile'),
(38, 'Can change doctor profile', 10, 'change_doctorprofile'),
(39, 'Can delete doctor profile', 10, 'delete_doctorprofile'),
(40, 'Can view doctor profile', 10, 'view_doctorprofile'),
(41, 'Can add patient profile', 11, 'add_patientprofile'),
(42, 'Can change patient profile', 11, 'change_patientprofile'),
(43, 'Can delete patient profile', 11, 'delete_patientprofile'),
(44, 'Can view patient profile', 11, 'view_patientprofile'),
(45, 'Can add medicine category', 12, 'add_medicinecategory'),
(46, 'Can change medicine category', 12, 'change_medicinecategory'),
(47, 'Can delete medicine category', 12, 'delete_medicinecategory'),
(48, 'Can view medicine category', 12, 'view_medicinecategory'),
(49, 'Can add medicine', 13, 'add_medicine'),
(50, 'Can change medicine', 13, 'change_medicine'),
(51, 'Can delete medicine', 13, 'delete_medicine'),
(52, 'Can view medicine', 13, 'view_medicine'),
(53, 'Can add cart', 14, 'add_cart'),
(54, 'Can change cart', 14, 'change_cart'),
(55, 'Can delete cart', 14, 'delete_cart'),
(56, 'Can view cart', 14, 'view_cart'),
(57, 'Can add appointment', 15, 'add_appointment'),
(58, 'Can change appointment', 15, 'change_appointment'),
(59, 'Can delete appointment', 15, 'delete_appointment'),
(60, 'Can view appointment', 15, 'view_appointment'),
(61, 'Can add thread model', 16, 'add_threadmodel'),
(62, 'Can change thread model', 16, 'change_threadmodel'),
(63, 'Can delete thread model', 16, 'delete_threadmodel'),
(64, 'Can view thread model', 16, 'view_threadmodel'),
(65, 'Can add message model', 17, 'add_messagemodel'),
(66, 'Can change message model', 17, 'change_messagemodel'),
(67, 'Can delete message model', 17, 'delete_messagemodel'),
(68, 'Can view message model', 17, 'view_messagemodel'),
(69, 'Can add order', 18, 'add_order'),
(70, 'Can change order', 18, 'change_order'),
(71, 'Can delete order', 18, 'delete_order'),
(72, 'Can view order', 18, 'view_order'),
(73, 'Can add lab test', 19, 'add_labtest'),
(74, 'Can change lab test', 19, 'change_labtest'),
(75, 'Can delete lab test', 19, 'delete_labtest'),
(76, 'Can view lab test', 19, 'view_labtest'),
(77, 'Can add article', 20, 'add_article'),
(78, 'Can change article', 20, 'change_article'),
(79, 'Can delete article', 20, 'delete_article'),
(80, 'Can view article', 20, 'view_article');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(7, 'accounts', 'department'),
(8, 'accounts', 'doctor'),
(10, 'accounts', 'doctorprofile'),
(9, 'accounts', 'patient'),
(11, 'accounts', 'patientprofile'),
(6, 'accounts', 'user'),
(1, 'admin', 'logentry'),
(20, 'admins', 'article'),
(13, 'admins', 'medicine'),
(12, 'admins', 'medicinecategory'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'contenttypes', 'contenttype'),
(15, 'patients', 'appointment'),
(14, 'patients', 'cart'),
(19, 'patients', 'labtest'),
(17, 'patients', 'messagemodel'),
(18, 'patients', 'order'),
(16, 'patients', 'threadmodel'),
(5, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2021-12-31 05:17:50.315269'),
(2, 'contenttypes', '0002_remove_content_type_name', '2021-12-31 05:17:50.352922'),
(3, 'auth', '0001_initial', '2021-12-31 05:17:50.563421'),
(4, 'auth', '0002_alter_permission_name_max_length', '2021-12-31 05:17:50.603283'),
(5, 'auth', '0003_alter_user_email_max_length', '2021-12-31 05:17:50.611261'),
(6, 'auth', '0004_alter_user_username_opts', '2021-12-31 05:17:50.617973'),
(7, 'auth', '0005_alter_user_last_login_null', '2021-12-31 05:17:50.626999'),
(8, 'auth', '0006_require_contenttypes_0002', '2021-12-31 05:17:50.629368'),
(9, 'auth', '0007_alter_validators_add_error_messages', '2021-12-31 05:17:50.636352'),
(10, 'auth', '0008_alter_user_username_max_length', '2021-12-31 05:17:50.644145'),
(11, 'auth', '0009_alter_user_last_name_max_length', '2021-12-31 05:17:50.651454'),
(12, 'auth', '0010_alter_group_name_max_length', '2021-12-31 05:17:50.663255'),
(13, 'auth', '0011_update_proxy_permissions', '2021-12-31 05:17:50.671234'),
(14, 'auth', '0012_alter_user_first_name_max_length', '2021-12-31 05:17:50.678264'),
(15, 'accounts', '0001_initial', '2021-12-31 05:17:51.043628'),
(16, 'admin', '0001_initial', '2021-12-31 05:17:51.149759'),
(17, 'admin', '0002_logentry_remove_auto_add', '2021-12-31 05:17:51.165528'),
(18, 'admin', '0003_logentry_add_action_flag_choices', '2021-12-31 05:17:51.176799'),
(19, 'sessions', '0001_initial', '2021-12-31 05:17:51.212582'),
(20, 'accounts', '0002_doctorprofile_patientprofile', '2021-12-31 11:42:00.990202'),
(21, 'accounts', '0003_auto_20211231_1746', '2021-12-31 12:01:04.333254'),
(22, 'accounts', '0004_auto_20211231_1756', '2021-12-31 12:11:07.902487'),
(23, 'accounts', '0005_auto_20220102_0940', '2022-01-02 03:55:17.196655'),
(24, 'admins', '0001_initial', '2022-01-02 03:55:17.304642'),
(25, 'admins', '0002_medicine_medicine_image', '2022-01-06 08:01:34.720539'),
(26, 'admins', '0003_alter_medicine_category', '2022-01-06 08:01:34.728642'),
(27, 'accounts', '0006_alter_patient_profile_pic', '2022-01-10 07:22:34.515187'),
(28, 'patients', '0001_initial', '2022-01-10 07:29:08.715494'),
(29, 'patients', '0002_appointment', '2022-01-19 07:45:31.469072'),
(30, 'patients', '0003_alter_appointment_status', '2022-01-25 09:56:15.305313'),
(31, 'patients', '0004_threadmodel_messagemodel', '2022-01-25 09:56:15.600385'),
(32, 'patients', '0005_order', '2022-01-25 09:56:15.732481'),
(33, 'patients', '0006_auto_20220125_1546', '2022-01-25 10:01:59.459759'),
(34, 'accounts', '0007_alter_doctor_phone_alter_patient_phone', '2022-02-02 06:28:48.726983'),
(35, 'patients', '0005_labtest', '2022-02-02 06:28:48.811643'),
(36, 'patients', '0006_remove_labtest_report', '2022-02-02 06:28:48.831589'),
(37, 'patients', '0007_labreport', '2022-02-02 06:28:48.910787'),
(38, 'patients', '0008_labtest_report_delete_labreport', '2022-02-02 06:28:48.940941'),
(39, 'patients', '0009_merge_20220201_2054', '2022-02-02 06:28:48.945887'),
(40, 'admins', '0004_article', '2022-02-24 09:15:23.801580');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('27gbb922dt8rigfm1kzcklwpeh30vzu6', '.eJxVjEsOAiEQBe_C2hBAOg0u3XsG0g2NjBommc9q4t11klno9lXV21SidWlpnWVKQ1EXZdXpd2PKT-k7KA_q91HnsS_TwHpX9EFnfRuLvK6H-3fQaG7fuoKJXnwo1kfHgMxUSdiAIJrgc7SBK7rskSJaOQMGyZnBMYORAur9Aeh-ODw:1n3rqX:crDLbZ9pizQ4ghT3hgaEEqcVnarrucbIRKU8TRLrp3U', '2022-01-16 03:47:49.475747'),
('ic9iinisn6nwch1cpe01clardmfsjniz', '.eJxVjMsOwiAQRf-FtSHQTgfGpXu_gTA8pGogKe3K-O_apAvd3nPOfQnnt7W4rafFzVGchUZx-h3Zh0eqO4l3X29NhlbXZWa5K_KgXV5bTM_L4f4dFN_Ltx5AmQAJc4bRJoXGAnoFZgwU0XiKPGRDU85sSWcwhJrtSACckKYA4v0B8ug3ew:1nNUQA:Bb-_FspLzGw8HVuT9s7YGETInVHzuIiJh7jdujSnIN0', '2022-03-11 06:49:42.890828'),
('pmdf4q10nyb7wkuohb9pj1vmyv661vu1', '.eJxVjEsOAiEQBe_C2hBAOg0u3XsG0g2NjBommc9q4t11klno9lXV21SidWlpnWVKQ1EXZdXpd2PKT-k7KA_q91HnsS_TwHpX9EFnfRuLvK6H-3fQaG7fuoKJXnwo1kfHgMxUSdiAIJrgc7SBK7rskSJaOQMGyZnBMYORAur9Aeh-ODw:1n3GlU:zBIYW8LdZ75pb6CO9-e-yNCjrt67t86cWjtH0TIXLBg', '2022-01-14 12:12:08.324760'),
('srbakjvjn9okougy6fr1h6ibbuwi7y2c', 'e30:1n7BPr:rTuP2o1gzE3oSrR3QtP8rhEooHZnNxwHhTLZ3QbDsGo', '2022-01-25 07:17:59.387169'),
('z0qtsvhxys0fy1pyqrf5xqdlr96yuvki', '.eJxVjEEOwiAQRe_C2hCGDgVcuvcMZJgBWzVtUtqV8e7apAvd_vfef6lE2zqkrZUljaLOCtXpd8vEjzLtQO403WbN87QuY9a7og_a9HWW8rwc7t_BQG341mRjnzmCi2KRgnES2FFw1EklRCjGsEAEE31B6YjBslRbPXjEHrJ6fwDiOTfE:1n40qW:ervd7eM_B7jvz7lanQgXSEDSGolbWHjychA3PauCGCI', '2022-01-16 13:24:24.976503');

-- --------------------------------------------------------

--
-- Table structure for table `patients_appointment`
--

CREATE TABLE `patients_appointment` (
  `id` bigint(20) NOT NULL,
  `appointment_Date_Time` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `booked_date` datetime(6) NOT NULL,
  `doctor_id` bigint(20) NOT NULL,
  `patient_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_appointment`
--

INSERT INTO `patients_appointment` (`id`, `appointment_Date_Time`, `status`, `booked_date`, `doctor_id`, `patient_id`) VALUES
(4, '2022-02-26 12:10:00.000000', 1, '2022-02-25 06:25:54.784773', 21, 16);

-- --------------------------------------------------------

--
-- Table structure for table `patients_cart`
--

CREATE TABLE `patients_cart` (
  `id` bigint(20) NOT NULL,
  `created_date` datetime(6) NOT NULL,
  `medicine_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_cart`
--

INSERT INTO `patients_cart` (`id`, `created_date`, `medicine_id`, `user_id`) VALUES
(7, '2022-01-25 10:15:13.777488', 2, 14),
(15, '2022-02-25 06:43:45.190726', 5, 16);

-- --------------------------------------------------------

--
-- Table structure for table `patients_labtest`
--

CREATE TABLE `patients_labtest` (
  `id` bigint(20) NOT NULL,
  `labtest_Date_Time` datetime(6) NOT NULL,
  `status` tinyint(1) NOT NULL,
  `booked_date` datetime(6) NOT NULL,
  `patient_id` bigint(20) NOT NULL,
  `report` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_labtest`
--

INSERT INTO `patients_labtest` (`id`, `labtest_Date_Time`, `status`, `booked_date`, `patient_id`, `report`) VALUES
(1, '2022-02-27 12:15:00.000000', 1, '2022-02-25 06:30:47.524768', 16, ''),
(2, '2022-02-27 12:29:00.000000', 0, '2022-02-25 06:44:53.156287', 16, '');

-- --------------------------------------------------------

--
-- Table structure for table `patients_messagemodel`
--

CREATE TABLE `patients_messagemodel` (
  `id` bigint(20) NOT NULL,
  `body` varchar(1000) NOT NULL,
  `date` datetime(6) NOT NULL,
  `is_read` tinyint(1) NOT NULL,
  `receiver_user_id` bigint(20) NOT NULL,
  `sender_user_id` bigint(20) NOT NULL,
  `thread_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_messagemodel`
--

INSERT INTO `patients_messagemodel` (`id`, `body`, `date`, `is_read`, `receiver_user_id`, `sender_user_id`, `thread_id`) VALUES
(1, 'asda', '2022-02-13 07:08:58.534461', 0, 17, 16, 2),
(2, 'hello', '2022-02-13 07:16:50.278300', 0, 21, 16, 3),
(3, 'Hello Doctor! I have a problem', '2022-02-25 06:25:29.010353', 0, 21, 16, 3),
(4, 'Hello Doctor', '2022-02-25 06:41:41.726015', 0, 21, 16, 3),
(5, 'Hello How are you', '2022-02-25 06:46:24.086110', 0, 16, 21, 3);

-- --------------------------------------------------------

--
-- Table structure for table `patients_order`
--

CREATE TABLE `patients_order` (
  `id` bigint(20) NOT NULL,
  `quantity` int(11) NOT NULL,
  `total_price` int(11) DEFAULT NULL,
  `payment_method` varchar(200) DEFAULT NULL,
  `payment_status` tinyint(1) DEFAULT NULL,
  `contact_no` varchar(10) DEFAULT NULL,
  `contact_address` varchar(200) DEFAULT NULL,
  `created_date` datetime(6) DEFAULT NULL,
  `status` varchar(200) DEFAULT NULL,
  `medicine_id` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_order`
--

INSERT INTO `patients_order` (`id`, `quantity`, `total_price`, `payment_method`, `payment_status`, `contact_no`, `contact_address`, `created_date`, `status`, `medicine_id`, `user_id`) VALUES
(7, 3, 600, 'Esewa', 0, '9861291534', 'Madhyepur, Thimi', '2022-01-25 10:19:15.253556', 'Pending', 2, 14),
(8, 5, 900, 'Esewa', 1, '9861291534', 'Khopasi', '2022-01-31 06:53:51.349998', 'Pending', 3, 14),
(10, 9, 1800, 'Esewa', 1, '9861291534', 'Banepa, Kavre', '2022-02-01 05:42:13.508127', 'Delivered', 2, 16),
(11, 5, 1000, 'Esewa', 0, '9861291534', 'Banepa, Kavre', '2022-02-25 06:27:16.802885', 'Pending', 2, 16),
(12, 5, 1000, 'Esewa', 1, '9861291534', 'Banepa, Kavre', '2022-02-25 06:29:43.138738', 'Pending', 2, 16),
(13, 4, 720, 'Esewa', 1, '9861291534', 'Madhyepur, Thimi', '2022-02-25 06:44:01.456095', 'Delivered', 3, 16);

-- --------------------------------------------------------

--
-- Table structure for table `patients_threadmodel`
--

CREATE TABLE `patients_threadmodel` (
  `id` bigint(20) NOT NULL,
  `receiver_id` bigint(20) NOT NULL,
  `user_id` bigint(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `patients_threadmodel`
--

INSERT INTO `patients_threadmodel` (`id`, `receiver_id`, `user_id`) VALUES
(1, 6, 16),
(2, 17, 16),
(3, 21, 16);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accounts_department`
--
ALTER TABLE `accounts_department`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `accounts_doctor`
--
ALTER TABLE `accounts_doctor`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `accounts_patient`
--
ALTER TABLE `accounts_patient`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `accounts_user`
--
ALTER TABLE `accounts_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_groups_user_id_group_id_59c0b32f_uniq` (`user_id`,`group_id`),
  ADD KEY `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `accounts_user_user_permi_user_id_permission_id_2ab516c2_uniq` (`user_id`,`permission_id`),
  ADD KEY `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `admins_article`
--
ALTER TABLE `admins_article`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `admins_medicine`
--
ALTER TABLE `admins_medicine`
  ADD PRIMARY KEY (`id`),
  ADD KEY `admins_medicine_category_id_ff26af9f_fk_admins_me` (`category_id`);

--
-- Indexes for table `admins_medicinecategory`
--
ALTER TABLE `admins_medicinecategory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `patients_appointment`
--
ALTER TABLE `patients_appointment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_appointment_doctor_id_ff42f56c_fk_accounts_` (`doctor_id`),
  ADD KEY `patients_appointment_patient_id_09055781_fk_accounts_` (`patient_id`);

--
-- Indexes for table `patients_cart`
--
ALTER TABLE `patients_cart`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_cart_medicine_id_6945bdb6_fk_admins_medicine_id` (`medicine_id`),
  ADD KEY `patients_cart_user_id_5de942cb_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `patients_labtest`
--
ALTER TABLE `patients_labtest`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_labtest_patient_id_5a8ec15b_fk_accounts_patient_user_id` (`patient_id`);

--
-- Indexes for table `patients_messagemodel`
--
ALTER TABLE `patients_messagemodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_messagemode_receiver_user_id_d69909a0_fk_accounts_` (`receiver_user_id`),
  ADD KEY `patients_messagemode_sender_user_id_446ed215_fk_accounts_` (`sender_user_id`),
  ADD KEY `patients_messagemode_thread_id_e0603a4a_fk_patients_` (`thread_id`);

--
-- Indexes for table `patients_order`
--
ALTER TABLE `patients_order`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_order_medicine_id_616b362a_fk_admins_medicine_id` (`medicine_id`),
  ADD KEY `patients_order_user_id_cff3d218_fk_accounts_user_id` (`user_id`);

--
-- Indexes for table `patients_threadmodel`
--
ALTER TABLE `patients_threadmodel`
  ADD PRIMARY KEY (`id`),
  ADD KEY `patients_threadmodel_receiver_id_2f0a1ae2_fk_accounts_user_id` (`receiver_id`),
  ADD KEY `patients_threadmodel_user_id_121e615f_fk_accounts_user_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accounts_department`
--
ALTER TABLE `accounts_department`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `accounts_user`
--
ALTER TABLE `accounts_user`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `admins_article`
--
ALTER TABLE `admins_article`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `admins_medicine`
--
ALTER TABLE `admins_medicine`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `admins_medicinecategory`
--
ALTER TABLE `admins_medicinecategory`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=81;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `patients_appointment`
--
ALTER TABLE `patients_appointment`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patients_cart`
--
ALTER TABLE `patients_cart`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `patients_labtest`
--
ALTER TABLE `patients_labtest`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `patients_messagemodel`
--
ALTER TABLE `patients_messagemodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `patients_order`
--
ALTER TABLE `patients_order`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `patients_threadmodel`
--
ALTER TABLE `patients_threadmodel`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `accounts_doctor`
--
ALTER TABLE `accounts_doctor`
  ADD CONSTRAINT `accounts_doctor_user_id_d06b185a_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_patient`
--
ALTER TABLE `accounts_patient`
  ADD CONSTRAINT `accounts_patient_user_id_c6b04ce0_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_groups`
--
ALTER TABLE `accounts_user_groups`
  ADD CONSTRAINT `accounts_user_groups_group_id_bd11a704_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `accounts_user_groups_user_id_52b62117_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `accounts_user_user_permissions`
--
ALTER TABLE `accounts_user_user_permissions`
  ADD CONSTRAINT `accounts_user_user_p_permission_id_113bb443_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `accounts_user_user_p_user_id_e4f0a161_fk_accounts_` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `admins_medicine`
--
ALTER TABLE `admins_medicine`
  ADD CONSTRAINT `admins_medicine_category_id_ff26af9f_fk_admins_me` FOREIGN KEY (`category_id`) REFERENCES `admins_medicinecategory` (`id`);

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `patients_appointment`
--
ALTER TABLE `patients_appointment`
  ADD CONSTRAINT `patients_appointment_doctor_id_ff42f56c_fk_accounts_` FOREIGN KEY (`doctor_id`) REFERENCES `accounts_doctor` (`user_id`),
  ADD CONSTRAINT `patients_appointment_patient_id_09055781_fk_accounts_` FOREIGN KEY (`patient_id`) REFERENCES `accounts_patient` (`user_id`);

--
-- Constraints for table `patients_cart`
--
ALTER TABLE `patients_cart`
  ADD CONSTRAINT `patients_cart_medicine_id_6945bdb6_fk_admins_medicine_id` FOREIGN KEY (`medicine_id`) REFERENCES `admins_medicine` (`id`),
  ADD CONSTRAINT `patients_cart_user_id_5de942cb_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `patients_labtest`
--
ALTER TABLE `patients_labtest`
  ADD CONSTRAINT `patients_labtest_patient_id_5a8ec15b_fk_accounts_patient_user_id` FOREIGN KEY (`patient_id`) REFERENCES `accounts_patient` (`user_id`);

--
-- Constraints for table `patients_messagemodel`
--
ALTER TABLE `patients_messagemodel`
  ADD CONSTRAINT `patients_messagemode_receiver_user_id_d69909a0_fk_accounts_` FOREIGN KEY (`receiver_user_id`) REFERENCES `accounts_user` (`id`),
  ADD CONSTRAINT `patients_messagemode_sender_user_id_446ed215_fk_accounts_` FOREIGN KEY (`sender_user_id`) REFERENCES `accounts_user` (`id`),
  ADD CONSTRAINT `patients_messagemode_thread_id_e0603a4a_fk_patients_` FOREIGN KEY (`thread_id`) REFERENCES `patients_threadmodel` (`id`);

--
-- Constraints for table `patients_order`
--
ALTER TABLE `patients_order`
  ADD CONSTRAINT `patients_order_medicine_id_616b362a_fk_admins_medicine_id` FOREIGN KEY (`medicine_id`) REFERENCES `admins_medicine` (`id`),
  ADD CONSTRAINT `patients_order_user_id_cff3d218_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);

--
-- Constraints for table `patients_threadmodel`
--
ALTER TABLE `patients_threadmodel`
  ADD CONSTRAINT `patients_threadmodel_receiver_id_2f0a1ae2_fk_accounts_user_id` FOREIGN KEY (`receiver_id`) REFERENCES `accounts_user` (`id`),
  ADD CONSTRAINT `patients_threadmodel_user_id_121e615f_fk_accounts_user_id` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
