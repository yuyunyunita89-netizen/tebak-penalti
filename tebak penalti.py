import streamlit as st
import random

# Inisialisasi state jika belum ada
if "skor_pemain" not in st.session_state:
    st.session_state.skor_pemain = 0
if "skor_komputer" not in st.session_state:
    st.session_state.skor_komputer = 0
if "tendangan_ke" not in st.session_state:
    st.session_state.tendangan_ke = 1
if "hasil" not in st.session_state:
    st.session_state.hasil = []

def reset_game():
    st.session_state.skor_pemain = 0
    st.session_state.skor_komputer = 0
    st.session_state.tendangan_ke = 1
    st.session_state.hasil = []

# UI Judul
st.title("⚽ Game Penalti Sederhana")
st.write("Pilih arah tendangan: **kiri**, **tengah**, atau **kanan**")
st.write(f"Kesempatan ke: **{st.session_state.tendangan_ke} / 5**")

arah = ["kiri", "tengah", "kanan"]
pilihan = st.radio("Pilih arah tendanganmu:", arah, horizontal=True)

if st.button("Tendang!"):
    if st.session_state.tendangan_ke <= 5:
        kiper = random.choice(arah)

        st.session_state.hasil.append(f"➡️ Kamu menendang ke: **{pilihan}**")
        st.session_state.hasil.append(f"🧤 Kiper lompat ke: **{kiper}**")

        if pilihan == kiper:
            st.session_state.hasil.append("⚽❌ Tendanganmu ditepis kiper!\n")
            st.session_state.skor_komputer += 1
        else:
            st.session_state.hasil.append("⚽✅ GOLLLL!!\n")
            st.session_state.skor_pemain += 1

        st.session_state.tendangan_ke += 1

# Menampilkan hasil tendangan sejauh ini
for h in st.session_state.hasil:
    st.markdown(h)

# Tampilkan hasil akhir jika sudah 5 tendangan
if st.session_state.tendangan_ke > 5:
    st.subheader("=== HASIL AKHIR ===")
    st.write("Skor Kamu:", st.session_state.skor_pemain)
    st.write("Skor Kiper:", st.session_state.skor_komputer)

    if st.session_state.skor_pemain > st.session_state.skor_komputer:
        st.success("🎉 Kamu Menang!")
    elif st.session_state.skor_pemain < st.session_state.skor_komputer:
        st.error("😢 Kamu Kalah!")
    else:
        st.info("🤝 Seri!")

    if st.button("Main Lagi"):
        reset_game()
