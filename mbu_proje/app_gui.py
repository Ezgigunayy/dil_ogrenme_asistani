import tkinter as tk
from tkinter import messagebox
from user.user_module import User
from vocabulary.vocabulary_module import add_new_word, list_words, remove_word
from quizz.quiz_module import start_quiz
from reports.report_module import generate_report

BG_COLOR = "#faf5e4"
BTN_COLOR = "#f67280"
BTN_HOVER = "#c06c84"
FONT = ("Helvetica", 12)
TITLE_FONT = ("Helvetica", 16, "bold")

global_user = None

def apply_button_style(button):
    button.configure(font=FONT, bg=BTN_COLOR, fg="white", padx=10, pady=5, bd=0, activebackground=BTN_HOVER)
    button.bind("<Enter>", lambda e: button.config(bg=BTN_HOVER))
    button.bind("<Leave>", lambda e: button.config(bg=BTN_COLOR))

def giris_ekrani():
    def giris_yap():
        global global_user
        username = username_entry.get()
        password = password_entry.get()
        email = email_entry.get()
        global_user = User(username, password, email, [])
        global_user.load_data()

        pencere.destroy()
        ana_menu()

    pencere = tk.Tk()
    pencere.title("Giriş Ekranı")
    pencere.configure(bg=BG_COLOR)
    pencere.geometry("300x200")

    tk.Label(pencere, text="Kullanıcı Adı:", bg=BG_COLOR, font=FONT).grid(row=0, column=0, sticky="w", padx=10, pady=5)
    username_entry = tk.Entry(pencere, font=FONT)
    username_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(pencere, text="Şifre:", bg=BG_COLOR, font=FONT).grid(row=1, column=0, sticky="w", padx=10, pady=5)
    password_entry = tk.Entry(pencere, show="*", font=FONT)
    password_entry.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(pencere, text="E-posta:", bg=BG_COLOR, font=FONT).grid(row=2, column=0, sticky="w", padx=10, pady=5)
    email_entry = tk.Entry(pencere, font=FONT)
    email_entry.grid(row=2, column=1, padx=10, pady=5)

    login_button = tk.Button(pencere, text="Giriş Yap", command=giris_yap)
    apply_button_style(login_button)
    login_button.grid(row=3, column=0, columnspan=2, pady=10)

    pencere.mainloop()

def kelime_ekle_penceresi():
    pencere = tk.Toplevel()
    pencere.title("Kelime Ekle")
    pencere.configure(bg="#f2f2f2")

    tk.Label(pencere, text="Türkçe:", bg=BG_COLOR).grid(row=0, column=0, padx=10, pady=10)
    turkish_entry = tk.Entry(pencere, width=30)
    turkish_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(pencere, text="İngilizce:", bg=BG_COLOR).grid(row=1, column=0, padx=10, pady=10)
    english_entry = tk.Entry(pencere, width=30)
    english_entry.grid(row=1, column=1, padx=10, pady=10)

    def kelime_ekle():
        turkish = turkish_entry.get()
        english = english_entry.get()

        if not turkish or not english:
            messagebox.showwarning("Uyarı", "Lütfen her iki alanı da doldurun.")
            return

        global_user.vocabulary.append({"turkish": turkish, "english": english})
        global_user.save_data()
        messagebox.showinfo("Başarılı", f"{turkish} - {english} kelimesi eklendi.")
        pencere.destroy()

    kelime_ekle_button = tk.Button(pencere, text="Kelime Ekle", width=30, bg=BG_COLOR, fg="white", command=kelime_ekle)
    apply_button_style(kelime_ekle_button)
    kelime_ekle_button.grid(row=2, column=0, columnspan=2, pady=20)

def kelimeleri_listele_penceresi():
    pencere = tk.Toplevel()
    pencere.title("Kelimeleri Listele")
    pencere.configure(bg=BG_COLOR)

    listbox = tk.Listbox(pencere, width=50, height=15, font=FONT)
    for word in global_user.vocabulary:
        listbox.insert(tk.END, f"{word['turkish']} - {word['english']}")
    listbox.pack(padx=10, pady=10)

    pencere.mainloop()

def kelime_sil_penceresi():
    def kelime_yukle():
        global global_user
        username = username_entry.get().strip()

        if not username:
            messagebox.showerror("Hata", "Lütfen kullanıcı adınızı girin.")
            return

        global_user = User(username, "", "", [])
        global_user.load_data()

        if not global_user.vocabulary:
            messagebox.showinfo("Bilgi", "Bu kullanıcıya ait kelime bulunamadı.")
            return

        listbox.delete(0, tk.END)
        for word in global_user.vocabulary:
            listbox.insert(tk.END, f"{word['turkish']} - {word['english']}")


    def kelime_sil():
        selected_index = listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Uyarı", "Lütfen silmek istediğiniz kelimeyi seçin.")
            return

        selected_word = listbox.get(selected_index)
        kelime = selected_word.split(" - ")[0]

        global_user.vocabulary = [w for w in global_user.vocabulary if w["turkish"] != kelime]
        global_user.save_data()

        listbox.delete(selected_index)
        messagebox.showinfo("Başarılı", f"{kelime} kelimesi silindi.")

    sil_window = tk.Toplevel()
    sil_window.title("Kelime Sil")
    sil_window.configure(bg=BG_COLOR)

    username_label = tk.Label(sil_window, text="Kullanıcı Adı:", font=FONT, bg=BG_COLOR)
    username_label.pack(pady=(10, 0))

    username_entry = tk.Entry(sil_window, font=FONT, width=30)
    username_entry.pack(pady=5)

    yukle_button = tk.Button(sil_window, text="Kelimeleri Yükle", width=20, command=kelime_yukle)
    apply_button_style(yukle_button)
    yukle_button.pack(pady=5)

    listbox = tk.Listbox(sil_window, font=FONT, width=40, height=10)
    listbox.pack(pady=10)

    sil_button = tk.Button(sil_window, text="Seçilen Kelimeyi Sil", width=25, command=kelime_sil)
    apply_button_style(sil_button)
    sil_button.pack(pady=10)

def test_baslat_penceresi():
    start_quiz_gui(global_user)

def start_quiz_gui(user):
    if not user.vocabulary:
        messagebox.showinfo("Bilgi", "Kelime listeniz boş. Lütfen önce kelime ekleyin.")
        return

    quiz_window = tk.Toplevel()
    quiz_window.title("Test")
    quiz_window.configure(bg="#f2f2f2")
    quiz_window.geometry("400x250")

    current_index = [0]
    correct_count = [0]

    question_label = tk.Label(quiz_window, text="", font=TITLE_FONT, bg=BG_COLOR)
    question_label.pack(pady=20)

    answer_entry = tk.Entry(quiz_window, font=FONT, width=30)
    answer_entry.pack(pady=10)

    feedback_label = tk.Label(quiz_window, text="", font=FONT, bg=BG_COLOR)
    feedback_label.pack(pady=5)

    def next_question():
        if current_index[0] < len(user.vocabulary):
            word = user.vocabulary[current_index[0]]
            question_label.config(text=f"{word['turkish']} kelimesinin İngilizcesi nedir?")
            answer_entry.delete(0, tk.END)
            feedback_label.config(text="")
        else:
            messagebox.showinfo("Test Bitti", f"Doğru sayısı: {correct_count[0]}/{len(user.vocabulary)}")
            quiz_window.destroy()

    def check_answer():
        word = user.vocabulary[current_index[0]]
        user_answer = answer_entry.get().strip().lower()
        correct_answer = word['english'].strip().lower()

        if user_answer == correct_answer:
            feedback_label.config(text="Doğru!", fg="green")
            correct_count[0] += 1
        else:
            feedback_label.config(text=f"Yanlış! Doğru cevap: {word['english']}", fg="red")

        current_index[0] += 1
        quiz_window.after(1500, next_question)

    submit_button = tk.Button(quiz_window, text="Cevabı Gönder", width=30, bg=BG_COLOR, fg="white", command=check_answer)
    apply_button_style(submit_button)
    submit_button.pack(pady=10)

    next_question()

def rapor_olustur():
    global global_user

    if not global_user or not global_user.vocabulary:
        messagebox.showinfo("Bilgi", "Rapor oluşturmak için önce kullanıcıyı seçmeli ve kelime eklemelisiniz.")
        return

    rapor_pencere = tk.Toplevel()
    rapor_pencere.title("Kelime Raporu")
    rapor_pencere.geometry("500x400")

    header = ["Türkçe", "İngilizce"]
    for col_index, baslik in enumerate(header):
        label = tk.Label(rapor_pencere, text=baslik, font=("Arial", 12, "bold"), borderwidth=1, relief="solid", width=15)
        label.grid(row=0, column=col_index, sticky="nsew")

    for row_index, word in enumerate(global_user.vocabulary, start=1):
        tk.Label(rapor_pencere, text=word["turkish"], borderwidth=1, relief="solid").grid(row=row_index, column=0, sticky="nsew")
        tk.Label(rapor_pencere, text=word["english"], borderwidth=1, relief="solid").grid(row=row_index, column=1, sticky="nsew")
        #tk.Label(rapor_pencere, text=word["zorluk"], borderwidth=1, relief="solid").grid(row=row_index, column=2, sticky="nsew")

    for i in range(3):
        rapor_pencere.grid_columnconfigure(i, weight=1)



def ana_menu():
    pencere = tk.Tk()
    pencere.title("Dil Öğrenme Asistanı")
    pencere.configure(bg=BG_COLOR)
    pencere.geometry("400x400")

    tk.Label(pencere, text="Hoşgeldiniz!", font=TITLE_FONT, bg=BG_COLOR).pack(pady=10)

    buttons = [
        ("Kelime Ekle", kelime_ekle_penceresi),
        ("Kelimeleri Listele", kelimeleri_listele_penceresi),
        ("Kelime Sil", kelime_sil_penceresi),
        ("Test Başlat", test_baslat_penceresi),
        ("Rapor Oluştur", rapor_olustur),
        ("Çıkış", pencere.destroy)
    ]

    for text, cmd in buttons:
        btn = tk.Button(pencere, text=text, width=30, command=cmd)
        apply_button_style(btn)
        btn.pack(pady=5)

    pencere.mainloop()

if __name__ == '__main__':
    giris_ekrani()
