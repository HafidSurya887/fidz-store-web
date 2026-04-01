from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('fidz_store.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users 
                 (username TEXT PRIMARY KEY, balance REAL)''')
    conn.commit()
    conn.close()

@app.route('/deposit', methods=['POST', 'GET'])
def deposit():
    # Bisa terima JSON atau Form-data biasa biar gak ribet
    username = request.form.get('username') or request.json.get('username')
    amount = float(request.form.get('amount') or request.json.get('amount'))
    
    pajak = amount * 0.01
    bersih = amount - pajak
    
    conn = sqlite3.connect('fidz_store.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users VALUES (?, 0)", (username,))
    c.execute("UPDATE users SET balance = balance + ? WHERE username = ?", (bersih, username))
    conn.commit()
    conn.close()
    
    return jsonify({"status": "success", "msg": f"Deposit {username} Masuk! Potongan pajak: Rp{pajak}. Saldo bersih: Rp{bersih}"})

@app.route('/wallet/<username>', methods=['GET'])
def cek_wallet(username):
    conn = sqlite3.connect('fidz_store.db')
    c = conn.cursor()
    c.execute("SELECT balance FROM users WHERE username = ?", (username,))
    res = c.fetchone()
    conn.close()
    if res:
        return jsonify({"username": username, "total_saldo": res[0]})
    return jsonify({"error": "User tidak ditemukan"}), 404

if __name__ == '__main__':
    init_db()
    print("Sistem Fidz Store Pay Jalan di Port 8080...")
    app.run(host='0.0.0.0', port=8080)
import streamlit as st

# Tampilan Web
st.title("Fidz Store - JUBEL HASIL RESS")
st.write("Selamat datang di panel manajemen akun.")

def main():
    # Contoh input sederhana
    nama_akun = st.text_input("Masukkan Nama Akun:")
    harga = st.number_input("Harga (Rp):", min_value=0)
    
    if st.button("Simpan Data"):
        st.success(f"Akun {nama_akun} dengan harga {harga} berhasil dicatat!")

if __name__ == "__main__":
    main()

