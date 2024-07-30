-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 30, 2024 at 06:59 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `user_management`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` bigint(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `hashed_password` varchar(500) NOT NULL,
  `created_at` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `username`, `email`, `hashed_password`, `created_at`) VALUES
(2, 'fasa', 'fasa@gmail.com', '$2b$12$7/eeuAeOg6hoWIyla/Qfa.zBehacDq6Wvdg1e2KrCwtJzgYO0vRR6', '0000-00-00'),
(8, 'ashfak', 'ashfak@gmail.com', '$2b$12$BRRGAvCm0OZRtlr/sxPQv.IVeWddAr0xybg9rMsOeTRGED3CMtTXO', '0000-00-00'),
(10, 'string', 'string', '$2b$12$N8rIcasS33QsenUH3nKJ2OEN71XtJJ48qurFCxXk9Ch/4cswquEzu', '2024-07-30'),
(13, 'kkn', 'asd@gmail.co', '$2b$12$fEuVBsOjQMC61E0ZFAj9VeBa9rNNMZw/WjPhKzB.TsMjkPK03iCBK', '0000-00-00'),
(14, 'alm', 'alm@gmail.com', '$2b$12$FDinOPojFPa6dqtF/5dffO2jZAsZjHbBMMiXWWz/Ri2kevYIoejzi', '0000-00-00'),
(15, 'hjk', 'hjk@gmail.com', '$2b$12$qlPJ5WJjN9H6tac0M74zOePQorM2Ev5HWeiPMwnjRny/nWLUgW8yS', '0000-00-00'),
(16, 'lm', 'lm@gmail.com', '$2b$12$uN/fhXVEWo7VhfLXiERILeKOCTltoABvGXXuBH/haJqtuzL0EW1Pu', '2024-07-30'),
(17, 'fasa3', 'fasa2@gmail.com', '$2b$12$zPHYJKoXnwtVKh5e150HSOfvGeRlUAR65pCHZhAayojPQ8yciUYkC', '2024-07-30'),
(18, 'krish3', 'krish3@gmail.com', '$2b$12$fRaU0dk5m5LUkzeltNSfwOyJY22hO2mibHEnoCJg0b7XdlSHangku', '2024-07-30');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
