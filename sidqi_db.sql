-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jun 03, 2023 at 07:41 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sidqi_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin_db`
--

CREATE TABLE `admin_db` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `admin_db`
--

INSERT INTO `admin_db` (`id`, `username`, `password`) VALUES
(1, 'admin', 'astroboy');

-- --------------------------------------------------------

--
-- Table structure for table `db_soal`
--

CREATE TABLE `db_soal` (
  `id` int(11) NOT NULL,
  `soal_satuan_id` varchar(255) NOT NULL,
  `pertanyaan` text NOT NULL,
  `jawaban` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `db_soal`
--

INSERT INTO `db_soal` (`id`, `soal_satuan_id`, `pertanyaan`, `jawaban`) VALUES
(35, '', '', '	Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atas\n\n\n\n\n\n\nGaya yang bekerja pada ikan adalah gaya berat ke bawah w=mg dan tegangan tali T ke atas yang diberikan oleh timbangan. Jika lift bergerak dipercepat ke atas, aplikasi hukum II Newton pada ikan menghasilkan gaya total berikut.\n∑▒〖F_y=〗  T-mg=ma_y\n T=ma_y+ mg\nTegangan tali  T,\nT=m〖(a〗_y+ g)\nT=m(a+ g)\nJika lift bergerak dipercepat ke atas, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.  Jadi, penunjukkan skala pada timbangan adalah menunjuk lebih dari 5 N\n'),
(36, '', '', 'Penunjukkan skala pada timbangan saat lift bergerak dipercepat ke atas adalah lebih dari 5 N. Hal ini disebabkan oleh adanya percepatan yang dialami oleh ikan dalam lift. Ketika lift bergerak ke atas dengan percepatan yang lebih besar dari percepatan gravitasi (g), gaya total yang dialami oleh ikan adalah jumlah dari gaya berat (mg) dan gaya tegangan tali (T). Oleh karena itu, tegangan tali (T) akan menjadi lebih besar daripada berat ikan (mg). Sebagai akibatnya, timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sesungguhnya.'),
(37, '', '', 'Ketika lift bergerak dipercepat ke atas, ikan mengalami dua gaya utama: gaya berat yang menarik ikan ke bawah (w = mg) dan tegangan tali (T) yang menarik ikan ke atas. Dalam persamaan gaya Newton kedua, gaya total pada ikan adalah:\n\n∑F_y = T - mg = ma_y\n\nDalam kondisi lift bergerak dipercepat ke atas, a_y adalah percepatan vertikal ikan. Maka, tegangan tali (T) dapat ditulis sebagai:\n\nT = ma_y + mg\n\nDalam persamaan ini, m adalah massa ikan, a adalah percepatan total (percepatan lift dan percepatan gravitasi), dan g adalah percepatan gravitasi.\n\nJadi, tegangan tali (T) pada timbangan adalah:\n\nT = m(a + g)\n\nKarena lift bergerak dipercepat ke atas, nilai a lebih besar dari nol. Sebagai hasilnya, tegangan tali (T) pada timbangan akan menunjukkan nilai yang lebih besar daripada berat ikan yang sebenarnya.\n');

-- --------------------------------------------------------

--
-- Table structure for table `kode_kelas`
--

CREATE TABLE `kode_kelas` (
  `id` int(11) NOT NULL,
  `guru_id` varchar(255) NOT NULL,
  `nama_kelas` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kode_kelas`
--

INSERT INTO `kode_kelas` (`id`, `guru_id`, `nama_kelas`) VALUES
(2, 'guru1', 'NEWTON');

-- --------------------------------------------------------

--
-- Table structure for table `konsep_siswa`
--

CREATE TABLE `konsep_siswa` (
  `id` int(11) NOT NULL,
  `nama` text NOT NULL,
  `kelas` text NOT NULL,
  `Chapter` text NOT NULL,
  `jawaban` text NOT NULL,
  `nilai1` text NOT NULL,
  `total` text NOT NULL,
  `hasil1` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `login_guru`
--

CREATE TABLE `login_guru` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_guru`
--

INSERT INTO `login_guru` (`id`, `username`, `email`, `password`) VALUES
(4, 'guru2', 'guru2@gmail.com', 'guru2');

-- --------------------------------------------------------

--
-- Table structure for table `login_siswa`
--

CREATE TABLE `login_siswa` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `login_siswa`
--

INSERT INTO `login_siswa` (`id`, `username`, `email`, `password`) VALUES
(9, 'feby', 'feby@gmail.com', 'feby'),
(11, 'siswa', 'siswa@gmail.com', 'siswa'),
(12, 'siswa1', 'siswa1@gmail.com', 'siswa'),
(13, 'siswa2', 'siswa2@gmail.com', 'siswa2');

-- --------------------------------------------------------

--
-- Table structure for table `profil_guru`
--

CREATE TABLE `profil_guru` (
  `id` int(11) NOT NULL,
  `nama` text NOT NULL,
  `gender` text NOT NULL,
  `alamat` text NOT NULL,
  `idguru` text NOT NULL,
  `email` text NOT NULL,
  `number` text NOT NULL,
  `foto` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `profil_siswa`
--

CREATE TABLE `profil_siswa` (
  `id` int(11) NOT NULL,
  `name` text NOT NULL,
  `gender` text NOT NULL,
  `alamat` text NOT NULL,
  `idsiswa` text NOT NULL,
  `email` text NOT NULL,
  `number` text NOT NULL,
  `foto` blob NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `profil_siswa`
--

INSERT INTO `profil_siswa` (`id`, `name`, `gender`, `alamat`, `idsiswa`, `email`, `number`, `foto`) VALUES
(4, 'sidqi', 'qdq', 'dqd', 'q', 'sidqi@gmail.com', 'qdqd', ''),
(6, 'M FEBY KHOIRU SIDQI', 'LAKI LAKI', 'PLANET MARS', 'A1C319011', 'ADA@gmail.com', 'u20193u9012', '');

-- --------------------------------------------------------

--
-- Table structure for table `soal_2`
--

CREATE TABLE `soal_2` (
  `id` int(11) NOT NULL,
  `chapter` text NOT NULL,
  `pertanyaan` text NOT NULL,
  `jawaban` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `soal_2`
--

INSERT INTO `soal_2` (`id`, `chapter`, `pertanyaan`, `jawaban`) VALUES
(1, '', '', '	Bola A bergerak dengan kecepatan konstan, percepatan bola A adalah nol, sehingga resultan gaya yang bekerja pada bola A adalah nol (F_A=0)\n	Bola B dan C bergerak dipercepat, perpindahan bola B diantara setiap posisi bertambah setiap waktu lebih kecil dari pada bola C, sehingga kecepatan bola B lebih kecil dari bola C. Perubahan kecepatan bola B setiap waktu lebih kecil dari pada bola C, sehingga percepatan bola B lebih kecil dari bola C. Jadi, resultan gaya bola C lebih besar dari pada resultan gaya B (FC>FB)\n\nPerbandingan resultan gaya yang bekerja pada bola A, B dan C adalah FC>FB>FA\n'),
(2, '', '', 'Bola A bergerak dengan kecepatan yang tetap dan tidak mengalami percepatan. Ini berarti tidak ada gaya yang bekerja pada bola A.\n\nBola B dan C bergerak dengan percepatan, yang berarti ada gaya yang bekerja pada keduanya. Perpindahan bola B antara setiap posisi bertambah lebih sedikit dari perpindahan bola C. Oleh karena itu, kecepatan bola B lebih rendah daripada bola C. Perubahan kecepatan bola B setiap waktu juga lebih kecil daripada bola C, sehingga percepatan bola B lebih kecil daripada bola C. Dengan demikian, resultan gaya yang bekerja pada bola C lebih besar daripada resultan gaya bola B.\n\nDalam perbandingannya, kita dapat mengatakan bahwa perbandingan resultan gaya yang bekerja pada bola A, B, dan C adalah F_C > F_B > F_A.'),
(3, '', '', 'Bola A bergerak dengan kecepatan yang tetap dan tidak mengalami percepatan. Hal ini berarti gaya yang bekerja pada bola A adalah nol (FA = 0).\n\nSementara itu, bola B dan C mengalami percepatan, yang berarti kecepatan mereka meningkat seiring waktu. Perpindahan bola B antara setiap posisi bertambah lebih sedikit dibandingkan dengan bola C. Akibatnya, kecepatan bola B lebih kecil daripada bola C. Perubahan kecepatan bola B setiap waktu juga lebih kecil dibandingkan dengan bola C, sehingga percepatan bola B lebih kecil dibandingkan dengan bola C.\nDengan demikian, resultan gaya yang bekerja pada bola C lebih besar daripada resultan gaya pada bola B (FC > FB). Selain itu, karena bola A tidak mengalami gaya yang bekerja, resultan gaya pada bola A adalah nol (F_A = 0).\nDalam kesimpulannya, perbandingan resultan gaya yang bekerja pada bola A, B, dan C adalah F_C > F_B > F_A.');

-- --------------------------------------------------------

--
-- Table structure for table `soal_3`
--

CREATE TABLE `soal_3` (
  `id` int(11) NOT NULL,
  `chapter` text NOT NULL,
  `pertanyaan` text NOT NULL,
  `jawaban` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `soal_3`
--

INSERT INTO `soal_3` (`id`, `chapter`, `pertanyaan`, `jawaban`) VALUES
(1, '', '', 'Menganggap gabungan dua balok sebagai \nsatu sistem (Fx (sistem) F=(m1+m2 )( a)x (x)=F/(m1+m2 )  \nGaya dorong yang bekerja pada m1 adalah gaya F ke kanan dan  F(2→1 ) ke kiri (gaya yang dikerjakan oleh m2 pada m1). Dari hukum III Newton,  F (2-1 )adalah gaya reaksi terhadap  F (1→2 )sehingga  F(2→1 )= F (1→2). Menggunakan Hukum II Newton pada m_1 menghasilkan\n(Fx)  F- F(2→1 )=(F-F(1→2 )=m)1(a)x\n(F-F(1→2 )=m)1(a)xF_(1→2 )=F-m)1(a)x\n(F(1→2)=F-m1 (F/(m1+m2))\nF(1→2)=(m2/(m1+m2))F\n'),
(2, '', '', 'Gaya horisontal yang bekerja pada m2 adalah gaya F(1→2 ) (gaya yang dikerjakan oleh m1  pada m2), yang arahnya ke kanan. Menggunakan hukum II Newton, diperoleh\n(fx)  F(1→2 )= m2(a)x\nF(1→2 )=m2 (F/(m1+m2 ))\nF(1→2 )=(m2/(m1+m2 ))F\n'),
(3, '', '', 'F> F(2→1)\nHukum  III Newton: F(2→1 )adalah gaya reaksi terhadap  F(1→2 ), sehingga F(1-2 )< F\n');

-- --------------------------------------------------------

--
-- Table structure for table `soal_4`
--

CREATE TABLE `soal_4` (
  `id` int(11) NOT NULL,
  `chapter` text NOT NULL,
  `pertanyaan` text NOT NULL,
  `jawaban` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `soal_4`
--

INSERT INTO `soal_4` (`id`, `chapter`, `pertanyaan`, `jawaban`) VALUES
(1, '', '', 'Menggunakan hukum Newton II, diperoleh F=M a mg=(3m) a a=mg/3m a=1/3  g\n'),
(2, '', '', 'Benda 2m bergerak ke kanan, gaya horisontal yang bekerja pada 2m adalah tegangan tali T ke kanan. Gaya vertikal yang bekerja pada 2m adalah gaya normal N ke atas dan gaya berat 2mg ke bawah. Menggunakan hukum Newton II, diperoleh\n(1)(Fx)  T=2m a\n(2)(Fy)  N-mg=0\n\nDiagram benda bebas:\nBenda m bergerak ke bawah, arah ke bawah sebagai arah positif. Gaya vertikal yang bekerja pada m adalah tegangan tali T ke atas dan gaya berat mg ke bawah. Menggunakan hukum Newton II, diperoleh,\n(3)(Fy) mg-T=m a\nPercepatan gerakan sistem ke bawah. Ketika (1) ditambah dengan (3), T saling meniadakan, sehingga diperoleh\nT+mg-T=2m a+m a\nmg=3 m a;\n a=1/3 g\n');

-- --------------------------------------------------------

--
-- Table structure for table `soal_5`
--

CREATE TABLE `soal_5` (
  `id` int(11) NOT NULL,
  `chapter` text NOT NULL,
  `pertanyaan` text NOT NULL,
  `jawaban` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `soal_5`
--

INSERT INTO `soal_5` (`id`, `chapter`, `pertanyaan`, `jawaban`) VALUES
(1, '', '', 'Diagram benda bebas m1:\nKetika balok m1  dilepas, sehingga balok m_2 bergerak ke bawah dengan percepatan a ⃗.\nMenggunakan hukum Newton II pada diperoleh:\n(1)(Fx)T-m_1 g sin⁡θ=m_1 a\n(2)(Fy)N-m_1 g cos⁡θ=0\nDiagram benda bebas m2:\nMenggunakan hukum Newton II diperoleh,\n(1)(Fx)0\n(2)(Fy)m2 g-T=m2 a\nT=m2 g-m2 a\nT=m2 (g-a)\nJadi, ketika balok m_1  dilepas, sehingga balok m2 bergerak ke bawah dengan percepatan a tegangan tali lebih kecil dari m2 g.\n'),
(2, '', '', 'Ketika balok m1 dilepas, balok m2 akan bergerak ke bawah dengan percepatan a. Dalam hal ini, kita menggunakan hukum Newton untuk menganalisis gerakan kedua balok tersebut.\n\nPada balok m_1, kita dapat menuliskan persamaan Newton II sebagai berikut:\n(1) Jumlah gaya pada sumbu x: T - m_1g sinθ = m_1a\n(2) Jumlah gaya pada sumbu y: N - m_1g cosθ = 0\n\nPada balok m_2, kita dapat menuliskan persamaan Newton II sebagai berikut:\n(1) Jumlah gaya pada sumbu x: 0\n(2) Jumlah gaya pada sumbu y: m_2g - T = m_2a\n\nTegangan tali (T) pada balok m_2 dapat kita hitung menggunakan persamaan T = m_2(g - a). Ini berarti tegangan tali akan lebih kecil dari m_2g.\n\nJadi, ketika balok m_1 dilepas, balok m_2 akan bergerak ke bawah dengan percepatan a. Tegangan tali (T) akan lebih kecil dari m_2g.'),
(3, '', '', 'Ketika balok m1 dilepas, balok m2 akan bergerak ke bawah dengan percepatan a. Menurut hukum Newton, kita dapat menurunkan persamaan berikut:    Jika kita melihat balok m1, kita dapat menggunakan hukum Newton II dan mendapatkan persamaan:Jumlah gaya dalam arah sumbu x adalah Tali - berat m1 * sin(theta) = m1.a. Jumlah gaya dalam arah sumbu y adalah Normal - berat m1 * cos(theta) = 0. Jika kita melihat balok m2, kita dapat menggunakan hukum Newton II dan mendapatkan persamaan: Jumlah gaya dalam arah sumbu x adalah 0.Jumlah gaya dalam arah sumbu y adalah berat m2 - Tali = m2.a.\n        Tali = m2.(g - a), di mana g adalah percepatan gravitasi.\nJadi, saat balok m1 dilepas, balok m2 akan bergerak ke bawah dengan percepatan a. Tegangan tali (Tali) akan lebih kecil daripada berat m2 . g.');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `admin_db`
--
ALTER TABLE `admin_db`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `db_soal`
--
ALTER TABLE `db_soal`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `kode_kelas`
--
ALTER TABLE `kode_kelas`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `konsep_siswa`
--
ALTER TABLE `konsep_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_guru`
--
ALTER TABLE `login_guru`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `login_siswa`
--
ALTER TABLE `login_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profil_guru`
--
ALTER TABLE `profil_guru`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `profil_siswa`
--
ALTER TABLE `profil_siswa`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `soal_2`
--
ALTER TABLE `soal_2`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `soal_3`
--
ALTER TABLE `soal_3`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `soal_4`
--
ALTER TABLE `soal_4`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `soal_5`
--
ALTER TABLE `soal_5`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `admin_db`
--
ALTER TABLE `admin_db`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `db_soal`
--
ALTER TABLE `db_soal`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `kode_kelas`
--
ALTER TABLE `kode_kelas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `konsep_siswa`
--
ALTER TABLE `konsep_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `login_guru`
--
ALTER TABLE `login_guru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `login_siswa`
--
ALTER TABLE `login_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `profil_guru`
--
ALTER TABLE `profil_guru`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `profil_siswa`
--
ALTER TABLE `profil_siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `soal_2`
--
ALTER TABLE `soal_2`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `soal_3`
--
ALTER TABLE `soal_3`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `soal_4`
--
ALTER TABLE `soal_4`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `soal_5`
--
ALTER TABLE `soal_5`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
