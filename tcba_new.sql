-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Apr 29, 2022 at 05:52 AM
-- Server version: 5.7.33
-- PHP Version: 7.4.19

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tcba`
--

-- --------------------------------------------------------

--
-- Table structure for table `changelog`
--

CREATE TABLE `changelog` (
  `device_id` int(11) DEFAULT NULL,
  `human_name` varchar(1023) COLLATE utf8_unicode_ci NOT NULL,
  `dcs_change` varchar(1023) COLLATE utf8_unicode_ci DEFAULT NULL,
  `time_stamp` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `changelog`
--

INSERT INTO `changelog` (`device_id`, `human_name`, `dcs_change`, `time_stamp`) VALUES
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:18:08'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:18:22'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:18:46'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:19:16'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 02:19:24'),
(103, 'Bao', 'OFF TO ON', '2022-04-29 02:19:25'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 02:24:04'),
(103, 'Bao', 'ON TO OFF', '2022-04-29 02:24:05'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:24:07'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 02:24:08'),
(103, 'Bao', 'OFF TO ON', '2022-04-29 02:24:09'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:24:10'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:24:14'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:24:15'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:24:16'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:24:18'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:24:19'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:24:25'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:24:35'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 02:24:46'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 02:24:55'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 02:25:02'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:25:32'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 02:25:34'),
(103, 'Bao', 'ON TO OFF', '2022-04-29 02:25:35'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 02:29:13'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 02:31:14'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 10:55:19'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 12:14:18'),
(103, 'Bao', 'OFF TO ON', '2022-04-29 12:14:31'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 12:19:59'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 12:20:41'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 12:20:48'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 12:21:15'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 12:21:20'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 12:21:23'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 12:21:25'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 12:21:30'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 12:21:41'),
(102, 'Bao', 'ON TO OFF', '2022-04-29 12:22:24'),
(101, 'Bao', 'ON TO OFF', '2022-04-29 12:22:25'),
(103, 'Bao', 'ON TO OFF', '2022-04-29 12:22:26'),
(101, 'Bao', 'OFF TO ON', '2022-04-29 12:44:13'),
(102, 'Bao', 'OFF TO ON', '2022-04-29 12:44:16');

-- --------------------------------------------------------

--
-- Table structure for table `device`
--

CREATE TABLE `device` (
  `device_id` int(11) NOT NULL,
  `state` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `device`
--

INSERT INTO `device` (`device_id`, `state`) VALUES
(101, 1),
(102, 1),
(103, 0);

-- --------------------------------------------------------

--
-- Table structure for table `record`
--

CREATE TABLE `record` (
  `record_id` int(11) NOT NULL,
  `temp` int(11) DEFAULT NULL,
  `humi` int(11) DEFAULT NULL,
  `light` int(11) DEFAULT NULL,
  `soil` int(11) DEFAULT NULL,
  `time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `record`
--

INSERT INTO `record` (`record_id`, `temp`, `humi`, `light`, `soil`, `time`) VALUES
(1, 30, 51, 159, 546, '2022-04-17 01:43:15'),
(2, 31, 52, 160, 612, '2022-04-17 01:43:20'),
(3, 21, 80, 80, 584, '2022-04-17 01:43:25'),
(4, 30, 24, 729, 163, '2022-04-17 01:43:30'),
(5, 40, 47, 814, 1021, '2022-04-17 01:43:40'),
(6, 43, 72, 435, 121, '2022-04-17 01:43:51'),
(7, 25, 61, 553, 520, '2022-04-17 01:43:55');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `email` varchar(64) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` blob
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `password`) VALUES
(1, 'bao123', 'bao.lethpttpcb@hcmut.edu.vn', 0x383364316539346435326632343331613965396133303465393030653532313739366333363336316536663430343965666138366239383663623036393166666630306265346539376234386631626361306237346636383366316637353334623363643563396562336664373437373463316164326231663037346439306532313738376535643335663436666638626166313161373039616666353932346537363132663033353261386465323364623238666235613139336162643433);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `changelog`
--
ALTER TABLE `changelog`
  ADD PRIMARY KEY (`time_stamp`);

--
-- Indexes for table `device`
--
ALTER TABLE `device`
  ADD PRIMARY KEY (`device_id`);

--
-- Indexes for table `record`
--
ALTER TABLE `record`
  ADD PRIMARY KEY (`record_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `device`
--
ALTER TABLE `device`
  MODIFY `device_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=104;

--
-- AUTO_INCREMENT for table `record`
--
ALTER TABLE `record`
  MODIFY `record_id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
