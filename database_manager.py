import sqlite3
from sqlite3 import Error

class Database_Manager:
    def __init__(self):
        self.create_connection("trivia_database")
        self.category_conversion = ["General Knowledge","Animals","History","Politics","Art"]


    def create_connection(self,db_file):
        conn = sqlite3.connect("trivia_database")
        c = conn.cursor()
        c.execute('''
                  CREATE TABLE IF NOT EXISTS `General Knowledge`
                  (score INTEGER)
                  ''')
        
        c.execute('''
                  CREATE TABLE IF NOT EXISTS Animals
                  (score INTEGER)
                  ''')
        
        
        c.execute('''
                  CREATE TABLE IF NOT EXISTS History
                  (score INTEGER)
                  ''')
        
        c.execute('''
                  CREATE TABLE IF NOT EXISTS Politics
                  (score INTEGER)
                  ''')
        
        c.execute('''
                  CREATE TABLE IF NOT EXISTS Art
                  (score INTEGER)
                  ''')
        conn.commit()
        conn.close()

    def add_values(self,category,score):
        conn = sqlite3.connect("trivia_database")
        c=conn.cursor()

        if category=="Animals":
            print(type(score))
            c.execute("INSERT INTO Animals VALUES (?)", (score,))
            conn.commit()
            conn.close()

        if category=="General Knowledge":
            print(type(score))
            c.execute("INSERT INTO `General Knowledge` VALUES (?)", (score,))
            c.execute("SELECT * FROM `General Knowledge`")
            conn.commit()
            conn.close()

        if category=="History":
            print(type(score))
            c.execute("INSERT INTO History VALUES (?)", (score,))
            conn.commit()
            conn.close()
        
        if category=="Politics":
            print(type(score))
            c.execute("INSERT INTO Politics VALUES (?)", (score,))
            conn.commit()
            conn.close()

        if category=="Art":
            print(type(score))
            c.execute("INSERT INTO Art VALUES (?)", (score,))
            conn.commit()
            conn.close()

    def retrieve_values(self):
        conn = sqlite3.connect("trivia_database")
        c = conn.cursor()
        c.execute(
            '''SELECT * From `General Knowledge`'''
        )

        general_knowledge_data = c.fetchall()


        c.execute(
            '''SELECT * From Animals'''
        )

        animals_data = c.fetchall()
        
        c.execute(
            '''SELECT * From Art'''
        )

        arts_data = c.fetchall()

        c.execute(
            '''SELECT * From History'''
        )

        history_data = c.fetchall()


        c.execute(
            '''SELECT * From Politics'''
        )

        politics_data = c.fetchall()
        conn.commit()
        conn.close()

        data_list = [general_knowledge_data,animals_data,history_data,arts_data,politics_data]

        print((data_list))

        return data_list
    
    def evaluate_data(self):
       #[general_knowledge_data,animals_data,arts_data,history_data,politics_data] = self.retrieve_values()
        data_list = self.retrieve_values()
        data_dict = {}
        data_remove = []
        for i in range(len(data_list)):
            print(f" i = {i}, data = {data_list[i]}, data_list = {data_list}")
            if data_list[i] != []:
                data_list[i] = data_list[i][0]
                average = sum(data_list[i])/len(data_list[i])
                data_dict[self.category_conversion[i]] = average
                i+=1
            else:
                i+=1

            
    

        

        # for i in range(len(self.category_conversion)):
        #     try:
        #         average = sum(data_list[i])/len(data_list[i])
        #         data_dict[self.category_conversion[i]] = average
        #         i+=1
        #     except ZeroDivisionError as e:
        #         i+=1
        print(data_dict)
        return data_dict


           

