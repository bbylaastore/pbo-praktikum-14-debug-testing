# DEBUG REPORT – Bug PPN 10%

## Deskripsi Bug
Pada proses perhitungan diskon ditemukan bug pada fungsi `hitung_diskon`,
di mana PPN 10% dihitung dua kali secara tidak sengaja sehingga
hasil harga akhir menjadi lebih besar dari yang seharusnya.

## Langkah Debugging (menggunakan pdb)
1. Program dijalankan dengan breakpoint menggunakan modul `pdb`.
2. Dilakukan pengecekan nilai variabel harga sebelum dan sesudah diskon.
3. Menggunakan perintah `p harga` untuk memantau perubahan nilai.
4. Terlihat bahwa PPN 10% ditambahkan lebih dari satu kali.
5. Setelah perbaikan logika perhitungan, nilai harga menjadi sesuai.

## Bukti Debug
- Hasil perintah `p harga` menunjukkan penambahan PPN ganda.
- Setelah bug diperbaiki, hasil perhitungan diskon dan pajak sudah benar.

## Kesimpulan
Bug terjadi akibat kesalahan logika penambahan PPN.
Dengan bantuan debugging menggunakan `pdb`, bug dapat ditemukan
dan diperbaiki sehingga perhitungan diskon berjalan dengan benar.
