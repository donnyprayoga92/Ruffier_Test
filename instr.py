from PyQt5.QtCore import QTime

win_x, win_y = 100, 100
win_width, win_height = 1000, 600

txt_hello = 'Selamat datang di program deteksi status kesehatan!'
txt_next = 'Mulai'
txt_instruction = ('Aplikasi ini memungkinkan Anda menggunakan tes Rufier untuk membuat diagnosis awal kesehatan Anda.\n'
                   'Tes Rufier adalah serangkaian latihan fisik yang dirancang untuk menilai kinerja jantung Anda selama aktivitas fisik.\n'
                   'Subjek berbaring dalam posisi terlentang selama 5 menit dan denyut nadi diukur selama 15 detik;\n'
                   'kemudian, dalam waktu 45 detik, subjek melakukan 30 kali squat.\n'
                   'Ketika latihan berakhir, subjek berbaring dan denyut nadi mereka diukur lagi selama 15 detik pertama\n'
                   'dan kemudian selama 15 detik terakhir dari menit pertama periode pemulihan.\n'
                   'Penting! Jika Anda merasa tidak enak badan selama tes (pusing,\n'
                   'tinnitus, sesak napas, dll.), hentikan tes dan konsultasikan dengan dokter.' )
txt_title = 'Informasi Kesehatan'
txt_name = 'Masukkan Nama Lengkap:'
txt_hintname = "Nama Lengkap"
txt_hintage = "0"
txt_test1 = ('Berbaring telentang dan ukur denyut nadi Anda selama 15 detik. Klik tombol "Mulai tes pertama" untuk memulai pengatur waktu.'
             '\nTuliskan hasilnya di bidang yang sesuai.')
txt_test2 = 'Lakukan 30 squat dalam 45 detik. Untuk melakukan ini, klik tombol "Mulai melakukan squat" \nuntuk memulai penghitung squat.'
txt_test3 = ('Berbaring telentang dan ambil denyut nadi Anda selama 15 detik pertama setiap menit, kemudian selama 15 detik terakhir setiap menit.'
             '\nTekan tombol "Mulai tes akhir" untuk memulai pengukur waktu.'
             '\nDetik yang harus diukur ditandai dengan warna hijau dan detik yang tidak boleh diukur ditandai dengan warna hitam.'
             'Catat hasilnya di bidang yang sesuai.')
txt_sendresults = 'Kirimkan hasilnya'
txt_hinttest1 = '0'
txt_hinttest2 = '0'
txt_hinttest3 = '0'
txt_starttest1 = 'Memulai tes pertama'
txt_starttest2 = 'Mulai melakukan squat'
txt_starttest3 = 'Memulai tes terakhir'
time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
txt_age = 'Usia:'
txt_finalwin = 'Hasil'
txt_index = 'Roufier Index: '
txt_workheart = 'Kinerja jantung: '
txt_res1 = "rendah. Segera temui dokter Anda!"
txt_res2 = "memuaskan. Temui dokter Anda!"
txt_res3 = "rata-rata. Mungkin ada baiknya Anda memeriksakan diri ke dokter untuk memeriksakan diri."
txt_res4 = "di atas rata-rata"
txt_res5 = "Tinggi"
