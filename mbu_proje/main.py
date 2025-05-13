# from user.user_module import User
# from quizz.quiz_module import start_quiz # Quiz sınıfını import ediyoruz
# from reports.report_module import generate_report
# from vocabulary.vocabulary_module import add_new_word, list_words, remove_word


# def main():
#     print("Dil Öğrenme Asistanı'na Hoşgeldiniz!")

#     # Kullanıcı kaydı
#     username = input("Kullanıcı adınızı girin: ")
#     password = input("Şifrenizi girin: ")
#     email = input("E-posta adresinizi girin: ")

#     user = User(username, password, email, [])
#     user.register()
#     user.login()

#     # Kullanıcıya seçim yapması için seçenekler sunalım
#     while True:
#         print("\n1. Kelime Ekle")
#         print("2. Kelimeleri Listele")
#         print("3. Kelime Sil")
#         print("4. Kelime Testi Başlat")
#         print("5. Rapor Oluştur")
#         print("6. Çıkış")

#         choice = input("Seçiminizi yapın (1-6): ")

#         if choice == '1':
#             add_new_word(user)  # Kelime ekleme işlemi
#         elif choice == '2':
#             list_words(user)  # Kullanıcıya ait kelimeleri listele
#         elif choice == '3':
#             remove_word(user)
#         elif choice == '4':
#             start_quiz(user)
#         elif choice == '5':
#             generate_report(user) 
#             break
#         elif choice == '6':
#             print("Çıkış yapılıyor...")
#             break
#         else:
#             print("Geçersiz seçenek. Tekrar deneyin.")

# if __name__ == "__main__":
#     main()


from user.user_module import User
from quizz.quiz_module import start_quiz  # Quiz sınıfını import ediyoruz
from reports.report_module import generate_report
from vocabulary.vocabulary_module import add_new_word, list_words, remove_word


def main():
    
    print("Dil Öğrenme Asistanı'na Hoşgeldiniz!")

    # Kullanıcı kaydı
    username = input("Kullanıcı adınızı girin: ")
    password = input("Şifrenizi girin: ")
    email = input("E-posta adresinizi girin: ")

    user = User(username, password, email, [])
    user.register()
    user.login()

    # Kullanıcıya seçim yapması için seçenekler sunalım
    while True:
        print("\n1. Kelime Ekle")
        print("2. Kelimeleri Listele")
        print("3. Kelime Sil")
        print("4. Kelime Testi Başlat")
        print("5. Rapor Oluştur")
        print("6. Çıkış")

        choice = input("Seçiminizi yapın (1-6): ")

        if choice == '1':
            add_new_word(user)  # Kelime ekleme işlemi
        elif choice == '2':
            list_words(user)  # Kullanıcıya ait kelimeleri listele
        elif choice == '3':
            remove_word(user)
        elif choice == '4':
            list_words(user)
            start_quiz(user)  # **Test Başlat**
        elif choice == '5':
            generate_report(user)  # **Rapor oluştur**
            break
        elif choice == '6':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçenek. Tekrar deneyin.")

if __name__ == "__main__":
    main()
