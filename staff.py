import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="#Rupha2003",
            database="staff_management"
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

class Address:
    def __init__(self, address_line1, address_line2, state, country, postal_code):
        self.address_line1 = address_line1
        self.address_line2 = address_line2
        self.state = state
        self.country = country
        self.postal_code = postal_code

    def save(self, db):
        query = "INSERT INTO Address (address_line1, address_line2, state, country, postal_code) VALUES (%s, %s, %s, %s, %s)"
        values = (self.address_line1, self.address_line2, self.state, self.country, self.postal_code)
        db.cursor.execute(query, values)
        db.conn.commit()
        return db.cursor.lastrowid

class Staff:
    def __init__(self, full_name, age, gender, salary, address_id=None):
        self.full_name = full_name
        self.age = age
        self.gender = gender
        self.salary = salary
        self.address_id = address_id

    def save(self, db):
        query = "INSERT INTO Staff (full_name, age, gender, salary, address_id) VALUES (%s, %s, %s, %s, %s)"
        values = (self.full_name, self.age, self.gender, self.salary, self.address_id)
        db.cursor.execute(query, values)
        db.conn.commit()

    def update(self, db, staff_id):
        query = "UPDATE Staff SET full_name = %s, age = %s, gender = %s, salary = %s, address_id = %s WHERE staff_id = %s"
        values = (self.full_name, self.age, self.gender, self.salary, self.address_id, staff_id)
        db.cursor.execute(query, values)
        db.conn.commit()

    @staticmethod
    def delete(db, staff_id):
        query = "DELETE FROM Staff WHERE staff_id = %s"
        db.cursor.execute(query, (staff_id,))
        db.conn.commit()
    def join(db):
        query = """
        SELECT Staff.full_name, Staff.age, Staff.gender, Staff.salary, Address.address_line1, Address.address_line2,
               Address.state, Address.country, Address.postal_code
        FROM Staff
        INNER JOIN Address ON Staff.address_id = Address.address_id
        """
        db.cursor.execute(query)
        return db.cursor.fetchall()

    @staticmethod
    def search(db, full_name):
        query = "SELECT * FROM Staff WHERE full_name LIKE %s"
        db.cursor.execute(query, (f"%{full_name}%",))
        return db.cursor.fetchall()


def main():
    db = Database()

   
    address = Address("123 Main St", "Apt 4B", "Tamil Nadu", "India", "641016")
    address_id = address.save(db)

    
    staff = Staff("Rupha", 21, "Female", 55000.00, address_id)
    staff.save(db)

    staff_update = Staff("Rupha", 22, "Female", 58000.00, address_id)
    staff_update.update(db, 1)

    
    Staff.delete(db, 1)

    results = Staff.search(db, "Rupha")
    for result in results:
        print(result)
    r=Staff.join(db)
    for r1 in r:
        print(r)
        

if __name__ == "__main__":
    main()
    
    
