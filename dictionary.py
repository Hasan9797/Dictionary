
import mysql.connector
import os


class Dictionary:
    def __init__(self, english_word=None, uzb_word=None):
        self.word_Eng = english_word
        self.word_Uzb = uzb_word
        self.character = ['1', '2', '3', '4']
        self.choice()

    def choice(self):
        self.clear()
        self.show()
        choices = input("Enter a selection: ").strip()
        while not choices.isdigit() or choices not in self.character:
            self.clear()
            print("you entered the wrong character!")
            self.show()
            choices = input("please enter one of the numbers [1/2/3/4/]: ").strip()

        if choices == self.character[0]:
            self.see_the_words_in_dictionary()
        elif choices == self.character[1]:
            self.add_a_new_word()
        elif choices == self.character[2]:
            self.searching()
        else:
            self.sign_out()

    def add_a_new_word(self):
        self.clear()
        new_word = input("Enter the new English word: ").strip().capitalize()
        uzbek_word = input("Enter the new Uzbek word: ").strip().capitalize()

        while not new_word.isalpha() or not uzbek_word.isalpha():
            print("You entered the wrong value!")
            new_word = input("Please Enter the word: ").strip().capitalize()
            uzbek_word = input("Enter the Uzbek word: ").strip().capitalize()

        self.word_Eng = new_word
        self.word_Uzb = uzbek_word

        my_sql = mysql.connector.connect(
            host="localhost",
            user="demo",
            password="12345678",
            database="DANG"
        )
        my_sql_db1 = my_sql.cursor()
        query1 = f"select * from dictionary where English_word='{self.word_Eng}' and " \
                 f"Uzbek_word='{self.word_Uzb}'"
        my_sql_db1.execute(query1)
        result = my_sql_db1.fetchall()

        if not result:
            my_sql = mysql.connector.connect(
                host="localhost",
                user="demo",
                password="12345678",
                database="DANG"
            )

            my_sql_db = my_sql.cursor()
            my_add = f"insert into dictionary(English_word, Uzbek_word) " \
                     f"values ('{self.word_Eng}', '{self.word_Uzb}')"
            my_sql_db.execute(my_add)
            my_sql.commit()
            print("A word was added to the dictionary\n")
            self.go_back()

        else:
            print("there is such a word, pleas try again")
            self.go_back()

    def go_back(self):
        back = input("\nPress B to go back >> B << : ").strip().lower()
        while not back == "b":
            self.clear()
            print("you made a mistake, pleas try again")
            back = input("Press B to go back >> B << : ").strip().lower()
        if back:
            self.back()

    def see_the_words_in_dictionary(self):
        self.clear()
        my_sql = mysql.connector.connect(
            host="localhost",
            user="demo",
            password="12345678",
            database="DANG"
        )
        my_sql_db1 = my_sql.cursor()
        query1 = "select * from dictionary"
        my_sql_db1.execute(query1)
        result = my_sql_db1.fetchall()

        if result:
            for see in result:
                print(see)
        else:
            print("The dictionary is empty")

        self.go_back()

    def searching(self):
        self.clear()
        self.choice_word()
        search_word = input("Enter a selection: ").strip()

        while search_word not in self.character[:2]:
            self.clear()
            print("You made a mistake, pleas try again")
            self.choice_word()
            search_word = input("Enter a selection: ").strip()

        if search_word == self.character[0]:
            self.clear()
            self.word_Eng = input("Enter an English word: ").capitalize()
            my_sql = mysql.connector.connect(
                host="localhost",
                user="demo",
                password="12345678",
                database="DANG"
            )
            my_sql_db1 = my_sql.cursor()
            query1 = f"select * from dictionary where English_word='{self.word_Eng}'"
            my_sql_db1.execute(query1)
            result = my_sql_db1.fetchall()

            if result:
                for see in result:
                    print(see)
            else:
                print("there is no such word")

            self.go_back()

        else:
            self.clear()
            self.word_Uzb = input("Enter an Uzbek word: ").capitalize()
            my_sql = mysql.connector.connect(
                host="localhost",
                user="demo",
                password="12345678",
                database="DANG"
            )
            my_sql_db1 = my_sql.cursor()
            query1 = f"select * from dictionary where Uzbek_word='{self.word_Uzb}'"
            my_sql_db1.execute(query1)
            result = my_sql_db1.fetchall()

            if result:
                for see in result:
                    print(see)
            else:
                print("there is no such word")

            self.go_back()

    @staticmethod
    def sign_out():
        print("\nThank you for using our dictionary! ")

    def back(self):
        self.choice()

    @staticmethod
    def choice_word():
        print("""
                    Which word are you looking for

        English word    >>[1]<<

        Uzbek word      >>[2]<<
        """)

    @staticmethod
    def clear():
        os.system("clear")

    @staticmethod
    def show():
        print("""
                                 Dictionary:

               1. see the words in the dictionary        >> 1 <<

               2. Add a new word.                        >> 2 <<

               3. Search                                 >> 3 <<

               4. Exit                                   >> 4 <<
               """)


report = Dictionary()