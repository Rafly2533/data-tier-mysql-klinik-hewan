CREATE DATABASE IF NOT EXISTS klinik_hewan;
USE klinik_hewan;

CREATE TABLE IF NOT EXISTS hewan (
    idHewan INT AUTO_INCREMENT PRIMARY KEY,
    nama_hewan VARCHAR(100) NOT NULL,
    jenis VARCHAR(50) NOT NULL,
    umur VARCHAR(20) NOT NULL,
    pemilik VARCHAR(100) NOT NULL
);
