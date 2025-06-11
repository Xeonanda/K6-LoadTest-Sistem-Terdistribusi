# Load Testing menggunakan K6

### Tujuan
Melakukan load testing pada endpoint localhost:5000 dengan file berukuran 10KB, 100KB, dan 1MB. File akan diakses oleh banyak user secara bersamaan dengan durasi tetap 1 detik

### Tools
K6

### Endpoint
```http://localhost:5000/api/<nama_file>```

### File
- 10kb.txt
- 100kb.txt
- 1mb.txt

### Skenario Test
Durasi: 1 detik
Jumlah virtual user: variatif

### Perintah eksekusi
```k6 run loadtest.js```

### Kesimpulan
- File kecil (10KB) dapat diakses hingga maksimal 135 user dan jika melebihi 135 user maka jumlah yang berhasil tidak 100%
- File sedang (100KB) dapat diakses hingga maksimal 133 user dan jika melebihi 133 user maka jumlah yang berhasil tidak 100%
- File besar (1MB) dapat diakses hingga maksimal 131 user dan jika melebihi 131 user maka jumlah yang berhasil tidak 100%
<br>
<br>

# Author
Ardhya Xeonanda Pradipta / L0122024