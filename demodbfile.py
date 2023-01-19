import sqlite3


class DbOperations:
    def __init__(self):
        self.conn = sqlite3.connect('branddb.db')
        self.curs = self.conn.cursor()

    def select_question(self):
        self.curs.execute('SELECT * FROM question')
        self.questions = self.curs.fetchall()
        return self.questions

    def insert_question(self, question, path, answer):
        try:
            self.curs.execute(
                f'INSERT INTO question (question, path, answer) VALUES("{question}","{path}","{answer}")')
            self.conn.commit()
        except Exception as e:
            print(e)

    def select_score(self):
        try:
            self.curs.execute(f'SELECT * from score_table')
            self.scores = self.curs.fetchall()
            return self.scores
        except Exception as e:
            print(e)

    def create_score(self, player, score):
        try:
            self.curs.execute(
                f'INSERT INTO score_table (name,score) VALUES ("{player}",{score})')
        except Exception as e:
            self.curs.execute(f'SELECT SCORE from score_table WHERE name="{player}"')
            self.player_score = self.curs.fetchone()
            if self.player_score[0] < score:
                self.curs.execute(
                    f'UPDATE score_table SET score=? WHERE name=?', [score, player])
        self.conn.commit()

    def highest_score(self):
        try:
            self.curs.execute('SELECT MAX(score),name FROM score_table')
            print(self.curs.fetchall())
        except Exception as e:
            print(e)

question = DbOperations()
question.create_score("tesla",20)
