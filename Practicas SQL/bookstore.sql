-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-08-2023 a las 12:12:42
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bookstore`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `autores`
--

CREATE TABLE `autores` (
  `autor_id` int(5) NOT NULL,
  `nombre` varchar(99) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `autores`
--

INSERT INTO `autores` (`autor_id`, `nombre`) VALUES
(0, 'Joe Abercrombie'),
(1, 'A.C. Crispin'),
(2, 'Andrzej Sapkowski'),
(3, 'Brandon Sanderson'),
(4, 'Edgar Rice Burroughs'),
(5, 'Elaine Cunningham'),
(6, 'James Luceno'),
(8, 'Kevin J. Anderson');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE `clientes` (
  `cliente_id` int(11) NOT NULL,
  `nombre` varchar(99) DEFAULT NULL,
  `email` varchar(99) DEFAULT NULL,
  `libro_id` int(3) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`cliente_id`, `nombre`, `email`, `libro_id`) VALUES
(1, 'Elhora Veronyre', 'elhora@veronyre.es', 1),
(2, 'Laegon Petsmaris', 'laegon@petsmaris.es', 6),
(3, 'Maryse Daelth', 'maryse@daelth.es', 2),
(4, 'Beriel Arris', 'beriel@Arris.es', 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `libros`
--

CREATE TABLE `libros` (
  `libro_id` int(3) NOT NULL,
  `titulo` varchar(99) DEFAULT NULL,
  `autor_id` int(3) DEFAULT NULL,
  `precio` int(11) DEFAULT NULL,
  `stock` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_spanish_ci;

--
-- Volcado de datos para la tabla `libros`
--

INSERT INTO `libros` (`libro_id`, `titulo`, `autor_id`, `precio`, `stock`) VALUES
(1, 'La trampa del paraíso', 1, 20, 3),
(2, 'El último deseo', 2, 24, 2),
(3, 'El camino de los reyes', 3, 30, 5),
(4, 'Citónica', 3, 20, 3),
(5, 'Jhon Carter de Marte', 4, 16, 2),
(6, 'Bautismo de fuego', 2, 24, 3),
(7, 'La venganza elfa', 5, 17, 1),
(8, 'Pelucidar', 4, 16, 2),
(9, 'Sombras de plata', 5, 17, 0),
(10, 'El señor oscuro', 6, 22, 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`autor_id`),
  ADD UNIQUE KEY `autor_id` (`autor_id`),
  ADD UNIQUE KEY `autor_id_2` (`autor_id`);

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`cliente_id`),
  ADD KEY `libro_id` (`libro_id`);

--
-- Indices de la tabla `libros`
--
ALTER TABLE `libros`
  ADD PRIMARY KEY (`libro_id`),
  ADD KEY `autor_id` (`autor_id`);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD CONSTRAINT `clientes_ibfk_1` FOREIGN KEY (`libro_id`) REFERENCES `libros` (`libro_id`);

--
-- Filtros para la tabla `libros`
--
ALTER TABLE `libros`
  ADD CONSTRAINT `libros_ibfk_1` FOREIGN KEY (`autor_id`) REFERENCES `autores` (`autor_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
