import sqlite3

def add_word(word, meaning):
    conn = sqlite3.connect('language_learning.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS words (
                        id INTEGER PRIMARY KEY,
                        word TEXT UNIQUE,
                        meaning TEXT)''')

    try:
        cursor.execute("INSERT INTO words (word, meaning) VALUES (?, ?)", (word, meaning))
        conn.commit()
        print(f"Kelime: {word} başarıyla eklendi.")
    except sqlite3.IntegrityError:
        print(f"{word} zaten mevcut.")
    finally:
        conn.close()

def get_all_words():
    conn = sqlite3.connect('language_learning.db')
    cursor = conn.cursor()
    cursor.execute("SELECT word, meaning FROM words")
    words = cursor.fetchall()
    conn.close()
    return words

def delete_word(word):
    conn = sqlite3.connect('language_learning.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM words WHERE word=?", (word,))
    conn.commit()
    conn.close()
    print(f"{word} başarıyla silindi.")
