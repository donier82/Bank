import sqlite3

conn = sqlite3.connect("BankofKyrgyzstan.db")
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS clients(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               name VARCHAR (50) NOT NULL,
               sur_name VARCHAR (50) NOT NULL,
               age INT DEFAULT 0,
               adress TEXT DEFAULT 'w',          
               email TEXT NOT NULL ,               
               balance INT DEFAULT 0              
               )""")



class Geeks:
    def __init__(self):
        self.name = None
        self.sur_name = None
        self.age = 0
        self.adress = None
        self.email = None
        self.balance = 0.0
   

    def register(self):
        user_name = input("Введите имя: ")
        user_sur_name = input("Фамилию: ")
        user_age = float(input("Введите возраст: "))
        user_adress = input("Введите адрес: ")
        user_email = input("Введите почту: ")
        
    
        cur.execute(f"SELECT email FROM clients WHERE email = '{user_email}'")
        client = cur.fetchone()
    
        if client:
            print("Вас уже добавили в табель")
        else:
            cur.execute(f"""INSERT INTO clients
                        (name,sur_name,age,adress,email)
                        VALUES ('{user_name}', '{user_sur_name}', {user_age}, '{user_adress}','{user_email}')""")
        
        
        conn.commit() 


   

    def debut_balance(self):
       
        user_balance=float(input('Введите сумму вклада: '))
        cur.execute(f"SELECT balance FROM clients WHERE balance={user_balance}")
        clients = cur.fetchone()

        if clients:
                cur.execute("""UPDATE clients SET 
                       user_balance = ? WHERE balance = ?""", (balance))
                balance=balance+user_balance
                
                
                
               
                conn.commit()
        else:
            print('не добавились')
            
    def credit_balance(self):
      
        user_balance=float(input('Введите сумму снятие: '))
        cur.execute(f"SELECT balance FROM clients WHERE balance={user_balance}")
        clients = cur.fetchone()

        if clients:
                if balance>=user_balance:
                    balance=balance-user_balance
                    cur.execute("""UPDATE clients SET 
                        user_balance = ? WHERE balance = ?""", (user_balance))
                
               
                conn.commit()
                
                
               
        else:
            print('недостаточно средст для снятие.')

    def all_client(self):
        cur.execute("SELECT * FROM clients")
        clients = cur.fetchall()
        print(clients)

    def main(self):
        while True:
            
            print("выберите действие: ")
            print("0-выйти, 1-регистрация, 2-добавить в баланс, 3-снятие со счета, 4-посмотрет все данные")
            command = int(input(": "))
            if command == 0:
                break
            elif command == 1:
                self.register()
            elif command == 2:
                self.debut_balance()
            elif command == 3:
                self.credit_balance()
            elif command == 4:
                self.all_client()
          
pult=Geeks()
pult.main()
