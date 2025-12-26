import random
from faker import Faker

fake = Faker('id_ID')

num_records = 500000
file_name = 'klinik_hewan_data_50.sql'

# ============================
# DATA REFERENSI
# ============================


# ============================
# WRITE SQL FILE
# ============================
with open(file_name, 'w', encoding='utf-8') as f:

    # DDL
    f.write("CREATE DATABASE IF NOT EXISTS klinik_hewan_db;\n")
    f.write("USE klinik_hewan_db;\n\n")

    f.write("""
CREATE TABLE IF NOT EXISTS hewan (
    idHewan INT AUTO_INCREMENT PRIMARY KEY,
    nama VARCHAR(100) NOT NULL,
    jenis VARCHAR(50) NOT NULL,
    umur VARCHAR(20) NOT NULL,
    pemilik VARCHAR(100) NOT NULL
);\n\n""")

    # DML
    f.write("INSERT INTO hewan (nama, jenis, umur, pemilik) VALUES\n")

    for i in range(1, num_records + 1):
        nama = random.choice(nama_hewan)
        jenis = random.choice(jenis_hewan)
        umur = f"{random.randint(1, 15)} Tahun"
        pemilik = f"{fake.first_name()} {fake.last_name()}".replace("'", "''")

        line = f"('{nama}', '{jenis}', '{umur}', '{pemilik}')"

        if i < num_records:
            line += ",\n"
        else:
            line += ";\n"

        f.write(line)

print(f"✅ File '{file_name}' dengan {num_records} data klinik hewan berhasil dibuat.")
