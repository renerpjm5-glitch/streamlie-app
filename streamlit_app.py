import streamlit as st
import sympy as sp
import pandas as pd

st.title("Aplikasi Solusi SPNL - Metode Bisection")

# simbol
x = sp.symbols('x')

# input fungsi
fungsi_input = st.text_input(
    "Masukkan fungsi f(x):",
    value="x**3 - x - 2"
)

# input batas
a = st.number_input("Batas bawah (a)", value=1.0)
b = st.number_input("Batas atas (b)", value=2.0)

# toleransi
tol = st.number_input("Toleransi error", value=0.0001, format="%.6f")

# tombol
if st.button("Hitung"):
    try:
        # ubah fungsi teks ke fungsi matematika
        f = sp.lambdify(x, sp.sympify(fungsi_input), 'math')

        # cek syarat bisection
        if f(a) * f(b) >= 0:
            st.error("Syarat bisection tidak terpenuhi (f(a) dan f(b) harus beda tanda)")
        else:
            data_iterasi = []
            iterasi = 1

            while abs(b - a) > tol:
                c = (a + b) / 2
                fc = f(c)

                data_iterasi.append([iterasi, a, b, c, fc])

                if f(a) * fc < 0:
                    b = c
                else:
                    a = c

                iterasi += 1

            # hasil akhir
            st.success("Perhitungan selesai")
            st.write(f"**Akar hampiran ≈ {c:.5f}**")
            st.write(f"**Jumlah iterasi: {iterasi-1}**")

            # tampilkan tabel iterasi
            df = pd.DataFrame(
                data_iterasi,
                columns=["Iterasi", "a", "b", "c", "f(c)"]
            )

            st.subheader("Tabel Iterasi")
            st.dataframe(df)

    except:
        st.error("Fungsi tidak valid. Contoh penulisan: x**2 - 4")

