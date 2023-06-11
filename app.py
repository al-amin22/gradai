from flask import Flask, request, session, render_template, redirect, url_for, flash, make_response
from flask_mysqldb import MySQL
import mysql.connector
import MySQLdb.cursors
import re
from werkzeug.utils import redirect
from flask import send_file, send_from_directory 
from werkzeug.utils import secure_filename
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from random import choices
import string
from fpdf import FPDF
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from werkzeug.exceptions import abort
import mysql.connector
from flask_mail import Mail, Message
import sys



app = Flask(__name__)


#koneksi
app.secret_key = 'bebasapasaja'
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] =''
app.config['MYSQL_DB'] ='sidqi_db'
mysql = MySQL(app)


msg = ''
formData=[]
mail = Mail(app)


def cosine_sim(text1, text2):
    corpus = [text1, text2]
    cv = CountVectorizer()
    cv_matrix = cv.fit_transform(corpus)
    similarity = cosine_similarity(cv_matrix)
    return similarity[0][1]


def get_data(username):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM data WHERE username = %s", (username,))
    data = mycursor.fetchall()
    return data







#nenu utaman dari system
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/kirim-email', methods=['POST'])
def kirim_email():
    nama = request.form['name']
    email = request.form['email']
    komentar = request.form['message']

    # Mengirim email
    msg = Message('Komentar dari Pengunjung', sender='mfebykhoirus@gmail.com', recipients=['mfebykhoirus@gmail.com'])
    msg.body = f'Nama: {nama}\nEmail: {email}\nKomentar: {komentar}'
    mail.send(msg)

    return 'Email berhasil dikirim'

@app.route('/panduan/pdf')
def panduan():
    return render_template("test.html")

 


#login siswa 
@app.route('/login/siswa', methods=['GET', 'POST'])
def loginsiswa():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `login_siswa` WHERE username=%s AND password=%s", (username, password))
        account = cursor.fetchone()
        cursor.close()
        if account:
            session['username'] = username
            return redirect(url_for('indexsiswa'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login_siswa.html', error=error)


#registrasi akun pada siswa
@app.route('/register/siswa', methods = ["GET", "POST"])
def regissiswa():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login_siswa WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO login_siswa VALUES (NULL, %s, %s, %s)', (username,email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register_siswa.html', msg=msg)
    

#login guru
@app.route('/loginguru', methods=['GET', 'POST'])
def loginguru():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `login_guru` WHERE username=%s AND password=%s", (username, password))
        account = cursor.fetchone()
        cursor.close()
        if account:
            session['username'] = username
            return redirect(url_for('indexguru',username=username))
        else:
            error = 'Invalid Username dan Password. Please try again.'
    return render_template('login_guru.html', error=error)
    



#nenu utaman dari admin
@app.route('/admin')
def adminhome():
    return render_template("admin.html")


@app.route('/get_jumlah_pengguna', methods=['GET'])
def get_jumlah_pengguna():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM login_siswa')
    result = cursor.fetchone()
    cursor.close()
    
    return str(result[0])


@app.route('/get_jumlah_guru', methods=['GET'])
def get_jumlah_guru():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT COUNT(*) FROM login_guru')
    result = cursor.fetchone()
    cursor.close()
    
    return str(result[0])



#nenu utaman dari admin guru
@app.route('/admin/guru')
def adminguru():
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM login_guru'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('adminguru.html', data=data)

# halaman delete data
@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    # Query untuk menghapus data dari tabel "users"
    cursor = mysql.connection.cursor()
    query = 'DELETE FROM `login_guru` WHERE id=%s'
    cursor.execute(query, (id_data,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('adminguru'))



#nenu utaman dari admin siswa
@app.route('/admin/siswa')
def adminsiswa():
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM login_siswa'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template("adminsiswa.html", data=data)

# halaman delete data
@app.route('/delete/siswa/<string:id_data>', methods=['GET'])
def deletesiswa(id_data):
    # Query untuk menghapus data dari tabel "users"
    cursor = mysql.connection.cursor()
    query = 'DELETE FROM `login_siswa` WHERE id=%s'
    cursor.execute(query, (id_data,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('adminsiswa'))



#login admin
@app.route('/login/admin',  methods=['GET', 'POST'])
def admin():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM `admin_db` WHERE username=%s AND password=%s", (username, password))
        account = cursor.fetchone()
        cursor.close()
        if account:
            return redirect(url_for('adminhome'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('loginadmin.html', error=error)


#nenu utaman dari admin profil guru
@app.route('/admin/profil/guru')
def admprofilguru():
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM profil_guru'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template('admguru.html', data=data)

# halaman delete data
@app.route('/delete/profil/<string:id_data>', methods=['GET'])
def deleteprofilguru(id_data):
    # Query untuk menghapus data dari tabel "users"
    cursor = mysql.connection.cursor()
    query = 'DELETE FROM `profil_guru` WHERE id=%s'
    cursor.execute(query, (id_data,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('admprofilguru'))


#nenu utaman dari admin profilsiswa
@app.route('/admin/profil/siswa')
def admprofilsiswa():
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM profil_siswa'
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    return render_template("admsiswa.html", data=data)

# halaman delete data
@app.route('/delete/profil/siswa/<string:id_data>', methods=['GET'])
def deleteprfsiswa(id_data):
    # Query untuk menghapus data dari tabel "users"
    cursor = mysql.connection.cursor()
    query = 'DELETE FROM `profil_siswa` WHERE id=%s'
    cursor.execute(query, (id_data,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('admprofilsiswa'))













#registrasi pada akun guru
@app.route('/register/guru', methods = ["GET", "POST"])
def registerguru():
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        

        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM login_guru WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO login_guru VALUES (NULL, %s, %s, %s)', (username,email,password))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register_guru.html', msg=msg)
        


#tampilan dashboard siswa
@app.route('/index/siswa')
def indexsiswa():
     # Mengambil informasi login dari session
    username = session.get('username')
    # Jika tidak ada informasi login, redirect ke halaman login
    if not username:
        return redirect('/login')
    return render_template("tampilansiswa.html")




#untuk prfil siswa input 
@app.route('/profilsiswa', methods = ["GET", "POST"])
def profilsiswa():
    if request.method == "POST":
        details = request.form
        Nama = details['name']
        gender = details['gender']
        Alamat = details['address']
        idsiswa = details['nis']
        email = details['email']
        number = details['number']
        foto = details['foto']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO profil_siswa(name, gender, alamat, idsiswa, email, number, foto) VALUES (%s,%s,%s,%s,%s,%s, %s)", (Nama, gender, Alamat, idsiswa, email, number, foto))
        mysql.connection.commit()
        cur.close()

        return 'sukses mengisi profil kamu :)'
 
    return render_template("profilsiswa.html")
    





# ini kodingan untuk exam 1

@app.route('/ujian/exam1')
def tessiswa():
    return render_template('newton_1.html')

#halaman ujian siswa  sekalgus similarity nlp
@app.route('/ujian/hasil/exam1', methods=['POST'])
def hasil():
    nama = request.form['user']
    kelas = request.form['kelas']
    chapter = request.form['checkbox']

    input_text = request.form['content1']

    cur = mysql.connection.cursor()
    cur.execute("SELECT jawaban FROM db_soal")
    results = cur.fetchall()

    similarities = []

    for row in results:
        similarity = cosine_sim(input_text, row[0])

        similarities.append(similarity)

    max_similar = max(similarities)

    max_similarity = round(max_similar * 100, 2)

    total = max_similarity
    

    if 1 <= max_similarity <= 29 :
        hasil1 = 'Tidak Memahami'

    elif 30 <= max_similarity <= 49:
        hasil1 = 'Miskonsepsi Spesifik'

    elif 50 <= max_similarity <= 79:
        hasil1 = 'Pemahaman Sebagian'
    else:
        hasil1 = "Pemahaman Yang Baik"


    if total > 1:
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO konsep_siswa (nama, kelas, Chapter, jawaban, nilai1,total, hasil1) VALUES (%s, %s, %s, %s, %s,%s, %s)'
        values = (nama, kelas, chapter, input_text, max_similarity,total, hasil1)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('skor', nilai=format(total) , hasil=hasil1))
    else:
        return redirect(url_for('lowskor'))
    
@app.route('/skor')
def skor():
    nilai = request.args.get('nilai')
    hasil = request.args.get('hasil')
    return render_template('skor.html', nilai=nilai, hasil=hasil)

@app.route('/low')
def lowskor():
    return render_template ('low_skor.html')





### ini adalah coding AI untuk exam 2
@app.route('/ujian/siswa/exam2')
def exam2():
    return render_template('newton_2.html')


@app.route('/ujian/hasil/exam2', methods=['POST'])
def hasil2():
    nama = request.form['user']
    kelas = request.form['kelas']
    chapter = request.form['checkbox']

    input_text = request.form['content1']

    cur = mysql.connection.cursor()
    cur.execute("SELECT jawaban FROM soal_2")
    results = cur.fetchall()

    similarities = []
    

    for row in results:
        similarity = cosine_sim(input_text, row[0])

        similarities.append(similarity)

    max_similar = max(similarities)
    

    max_similarity = round(max_similar * 100, 2)

    total = max_similarity
    
    

    if 1 <= max_similarity <= 29 :
        hasil1 = 'Tidak Memahami'

    elif 30 <= max_similarity <= 49:
        hasil1 = 'Miskonsepsi Spesifik'

    elif 50 <= max_similarity <= 79:
        hasil1 = 'Pemahaman Sebagian'
    else:
        hasil1 = "Pemahaman Yang Baik"


    if total > 1:
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO konsep_siswa (nama, kelas, Chapter, jawaban, nilai1, total, hasil1) VALUES (%s, %s, %s, %s, %s,%s, %s)'
        values = (nama, kelas, chapter, input_text, max_similarity,total, hasil1)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('skorexam2', nilai=format(total), hasil = hasil1))
    else:
        return render_template('low_skor.html')



@app.route('/skor/exam2')
def skorexam2():
    nilai = request.args.get('nilai')
    hasil2 = request.args.get('hasil')
    return render_template('skor2.html', nilai=nilai, hasil2=hasil2)




### ini adalah coding AI untuk exam 3
@app.route('/ujian/siswa/exam3')
def exam3():
    return render_template('newton_3.html')



@app.route('/ujian/hasil/exam3', methods=['POST'])
def hasil3():
    nama = request.form['user']
    kelas = request.form['kelas']
    chapter = request.form['checkbox']

    input_text = request.form['content1']

    cur = mysql.connection.cursor()
    cur.execute("SELECT jawaban FROM soal_3")
    results = cur.fetchall()

    similarities = []
    

    for row in results:
        similarity = cosine_sim(input_text, row[0])
       

        similarities.append(similarity)
      

    max_similar = max(similarities)
  

    max_similarity = round(max_similar * 100, 2)
   
    total = max_similarity
    
    if 1 <= max_similarity <= 29 :
        hasil1 = 'Tidak Memahami'

    elif 30 <= max_similarity <= 49:
        hasil1 = 'Miskonsepsi Spesifik'

    elif 50 <= max_similarity <= 79:
        hasil1 = 'Pemahaman Sebagian'
    else:
        hasil1 = "Pemahaman Yang Baik"
    

    if total > 1:
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO konsep_siswa (nama, kelas, Chapter, jawaban, nilai1, total, hasil1) VALUES ( %s,%s, %s, %s, %s,%s, %s)'
        values = (nama, kelas, chapter, input_text, max_similarity, total, hasil1)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('skor3', nilai=format(total), hasil=max_similarity))
    else:
        return render_template('low_skor.html')



@app.route('/skor/exam3')
def skor3():
    nilai = request.args.get('nilai')
    hasil3 = request.args.get('hasil')
    return render_template('skor3.html', nilai=nilai, hasil3=hasil3)




### ini adalah coding AI untuk exam 4
@app.route('/ujian/siswa/exam4')
def exam4():
    return render_template('newton_4.html')

@app.route('/ujian/hasil/exam4', methods=['POST'])
def hasil4():
    nama = request.form['user']
    kelas = request.form['kelas']
    chapter = request.form['checkbox']

    input_text = request.form['content1']

    cur = mysql.connection.cursor()
    cur.execute("SELECT jawaban FROM soal_4")
    results = cur.fetchall()

    similarities = []
    
    for row in results:
        similarity = cosine_sim(input_text, row[0])
        

        similarities.append(similarity)
        

    max_similar = max(similarities)
    

    max_similarity = round(max_similar * 100, 2)
    
    total = max_similarity
    

    if 1 <= max_similarity <= 29 :
        hasil1 = 'Tidak Memahami'

    elif 30 <= max_similarity <= 49:
        hasil1 = 'Miskonsepsi Spesifik'

    elif 50 <= max_similarity <= 79:
        hasil1 = 'Pemahaman Sebagian'
    else:
        hasil1 = "Pemahaman Yang Baik"
    

    if total > 1:
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO konsep_siswa (nama, kelas, Chapter, jawaban, nilai1, total, hasil1) VALUES (%s, %s, %s, %s,%s, %s, %s)'
        values = (nama, kelas, chapter, input_text, max_similarity, total, hasil1)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('skor4', nilai=format(total), hasil=hasil1))
    else:
        return render_template('low_skor.html')



@app.route('/skor/exam4')
def skor4():
    nilai = request.args.get('nilai')
    hasil4 = request.args.get('hasil')
    return render_template('skor4.html', nilai=nilai, hasil4=hasil4)



### ini adalah coding AI untuk exam 5
@app.route('/ujian/siswa/exam5')
def exam5():
    return render_template('newton_5.html')



@app.route('/ujian/hasil/exam5', methods=['POST'])
def hasil5():
    nama = request.form['user']
    kelas = request.form['kelas']
    chapter = request.form['checkbox']

    input_text = request.form['content1']
  

    cur = mysql.connection.cursor()
    cur.execute("SELECT jawaban FROM soal_5")
    results = cur.fetchall()

    similarities = []
    

    for row in results:
        similarity = cosine_sim(input_text, row[0])
        

        similarities.append(similarity)
       

    max_similar = max(similarities)
    

    max_similarity = round(max_similar * 100, 2)
    

    total = max_similarity
    
    
    if 1 <= max_similarity <= 29 :
        hasil1 = 'Tidak Memahami'

    elif 30 <= max_similarity <= 49:
        hasil1 = 'Miskonsepsi Spesifik'

    elif 50 <= max_similarity <= 79:
        hasil1 = 'Pemahaman Sebagian'
    else:
        hasil1 = "Pemahaman Yang Baik"

    if total > 1:
        cursor = mysql.connection.cursor()
        query = 'INSERT INTO konsep_siswa (nama, kelas, Chapter, jawaban, nilai1, total, hasil1) VALUES ( %s, %s, %s,%s, %s, %s, %s)'
        values = (nama, kelas, chapter, input_text, max_similarity, total, hasil1)
        cursor.execute(query, values)
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('skor5', nilai=format(total), hasil=hasil1))
    else:
        return render_template('low_skor.html')



@app.route('/skor/exam5')
def skor5():
    nilai = request.args.get('nilai')
    hasil5 = request.args.get('hasil')
    return render_template('skor5.html', nilai=nilai, hasil5=hasil5)






#######------------------------------------------------------------------##########################

#halaman ujian class 1
@app.route('/ujian/siswa')
def ujiansiswa():
    return render_template("ujiansiswa.html")





#index guru atau dashboard guru 
@app.route('/index/guru')
def indexguru():
    return render_template("tampilanguru.html")





#masukkan profl guru dan tampilkan 
@app.route('/profilguru', methods=["GET", "POST"])
def profilguru():
    if request.method == "POST":
        details = request.form
        Nama = details['name']
        gender = details['gender']
        Alamat = details['alamat']
        idguru = details['nip']
        email = details['email']
        number = details['number']
        foto = details['foto']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO profil_guru(nama, gender, alamat, idguru, email, number, foto) VALUES (%s,%s,%s,%s,%s,%s, %s)", (Nama, gender, Alamat, idguru, email, number, foto))
        mysql.connection.commit()
        cur.close()
        
        return 'sukses mengisi profil :)'
    
    return render_template("profilguru.html")



# halaman kelas guru                         
@app.route('/kelasguru')
def kelasguru():
    return render_template("kelasguru.html")

# membuat kode exam dalam bentuk pdf
@app.route('/generate', methods=['POST'])
def generate():
    # Ambil data dari form
    nama = request.form['nama']
    kelas = request.form['kelas']
    univ = request.form['univ']
    tanggal = request.form['tanggal']
    # Generate kode acak
    chars = string.ascii_uppercase + string.digits
    kode = ''.join(choices(chars, k=5))

    # Cek apakah kode sudah digunakan
    while check_kode(kode):
        kode = ''.join(choices(chars, k=5))

    # Simpan data ke database
    simpan_data(nama, kelas, univ, tanggal, kode)

    # Buat PDF dengan data guru dan kode
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'KODE UJIAN NEWTON', 0, 1)
    pdf.cell(0, 10, '', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.cell(0, 10, f'Nama guru: {nama}', 0, 1)
    pdf.cell(0, 10, f'Kelas yang diampu: {kelas}', 0, 1)
    pdf.cell(0, 10, f'Instansi : {univ}', 0, 1)
    pdf.cell(0, 10, f'Tanggal ujian: {tanggal}', 0, 1)
    pdf.cell(0, 10, f'Kode ujian: {kode}', 0, 1)

    # Simpan PDF sebagai response dan unduh
    # Simpan PDF sebagai response dan unduh
    response = make_response(pdf.output(dest='S').encode('latin1'))
    response.headers.set('Content-Disposition', 'attachment', filename='kode exam newton.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

def check_kode(kode):
    # Fungsi untuk memeriksa apakah kode sudah digunakan
    # Return True jika sudah digunakan, False jika belum
    # Contoh implementasi sederhana dengan list
    kode_digunakan = ['ABCD', 'EFGH', 'IJKL'] # Contoh data kode yang sudah digunakan
    if kode in kode_digunakan:
        return True
    else:
        return False

def simpan_data(nama, kelas, univ, tanggal, kode):
    # Fungsi untuk menyimpan data ke database
    # Contoh implementasi sederhana dengan list
    data_guru = [{'nama': 'Andi','kelas': 'X ipa 1','Instansi': 'MAN 1','tanggal': '12-12-2022','kode': 'ABCD'}, {'nama': 'Budi', 'kode': 'EFGH'}, {'nama': 'Cindy', 'kode': 'IJKL'}] # Contoh data guru yang sudah ada
    data_guru.append({'nama': nama, 'kelas': kelas ,'instansi': univ,'tanggal': tanggal,'kode': kode})
    print(data_guru) # Contoh tampilan data guru setelah ditambah





#halaman masukkan soal ke database
@app.route('/tambahsoal', methods=["GET", "POST"])
def tambahsoal():
    if request.method == 'POST':
        keyword = request.form['keyword']

        # Query untuk mencari data berdasarkan keyword
        cursor = mysql.connection.cursor()
        query = 'SELECT * FROM konsep_siswa WHERE nama LIKE %s OR kelas LIKE %s'
        values = ('%' + keyword + '%', '%' + keyword + '%')
        cursor.execute(query, values)
        results = cursor.fetchall()
        cursor.close()

        return render_template('kelas_manager.html', results=results)
    
    return render_template('kelas_manager.html') 




@app.route('/unduh/data/siswa', methods=["GET", "POST"])
def unduh():
    class SearchForm(FlaskForm):
        keyword = StringField('Keyword', validators=[DataRequired()])
        submit = SubmitField('Search')
    
    form = SearchForm()
    

    if form.validate_on_submit():

        keyword = form.keyword.data
        cursor = mysql.connection.cursor()
        # Query data dari database
        query = 'SELECT * FROM konsep_siswa WHERE nama LIKE %s OR kelas LIKE %s'
        values = ('%' + keyword + '%', '%' + keyword + '%')
        cursor.execute(query, values)
        results = cursor.fetchall()
        cursor.close()
        
    
        # Jika tidak ada hasil pencarian, tampilkan pesan error
        if not results:
            abort(404)
        
        # Buat file PDF
        pdf = FPDF()
        pdf = FPDF('P', 'mm', 'A4') # A4: 210 x 297 mm
        pdf.add_page()
        
        # Mengatur margin
        
        pdf.set_left_margin(10)
        pdf.set_right_margin(10)
        pdf.set_top_margin(10)
        pdf.set_auto_page_break(True, margin=15)
        pdf.set_font('Arial', 'B', 14)
        pdf.cell(40, 10, 'Kode Exam:' + keyword)
        # Menambahkan judul dokumen
        pdf.cell(80, 10, 'Hasil Siswa', 0, 1, 'C')

        # Menambahkan garis bawah
        pdf.cell(190, 0.5, '', 'B', 1)
        pdf.ln()
        pdf.set_font('Arial', '', 10)
        for result in results:
            pdf.cell(0, 10, f'Nama: {result[1]}', 0, 1)
            pdf.cell(0, 10, f'Kode Ujian : {result[2]}', 0, 1)
            pdf.cell(0, 10, f'Chapter: {result[3]}', 0, 1)
            pdf.cell(0, 10, f'Jawaban: {result[4]}', 0, 1)
            pdf.cell(0, 10, f'Skor & Pemahaman Konsep Soal : {result[5]} ----> {result[7]}', 0, 1)
            pdf.cell(0, 10, f'Total: {result[6]}', 0, 1)
            pdf.cell(0, 10, f'_________________________________________________________________________', 0, 1)
            pdf.cell(0, 10, f"---------------------------------------------------------------------------------------------------------", ln=True)

        response = make_response(pdf.output(dest='S').encode('latin1'))
        response.headers.set('Content-Disposition', 'attachment', filename='Hasil siswa.pdf')
        response.headers.set('Content-Type', 'application/pdf')
        return response

    return render_template('unduh.html', form=form)

    


#### data soal di menu guru#################
@app.route('/data/soal')
def datasoal():
    return render_template('kelas_manager2.html')


@app.route('/kriteria')
def kriteria ():
    return render_template('kriteria.html')

#----------------------------------------

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))    



###---------------

if __name__ == '__main__':
    app.run(debug=True)

