import records

def main():
    global db
    db = records.Database('sqlite:///pantry.db')
    stuff()

    # db.query('create table if not exists (key int )')

def stuff():
    db.query('drop table if exists foods')
    db.query('create table foods (key integer primary key autoincrement, name text, calories text, expiration_date text)')
    db_query('insert into foods (name, calories, expiration_date) values (:name, :calories, :expiration_date)', name = 'apple', calories = '95', expiration_date = 'tomorrow idk')
    # db.query('insert into foods (name, calories, expiration_date) values (:name, :calories, :expiration_date)', name = 'apple', calories = '95', expiration_date = 'tomorrow idk')
    stuff = db_query('select * from foods')
    # print(stuff.export('csv'))
    for r in stuff:
        print(r.key)

def db_query(query, fetchall = False, **params):
    conn = db.get_connection()
    return conn.query(query, fetchall, **params)

if __name__ == '__main__':
    main()
