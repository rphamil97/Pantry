import records

def setup():
    global db
    db = records.Database('sqlite:///pantry.db')
    db.query('create table if not exists food (key integer primary key autoincrement, name text, calories int, servings real, expiration_date text)')
    db.query('create table if not exists recipe (key integer primary key autoincrement, name text, portions real)')
    db.query('create table if not exists food_recipe(food_key int, recipe_key int, servings real, \
        foreign key (food_key) references food (key), foreign key (recipe_key) references recipe (key))')

def insert(table = None, **kwargs):
    if 'food' not in table and 'recipe' not in table:
        return

    name_str = ''
    value_str = ''
    for key in kwargs:
        name_str += key + ','
        value_str += ':' + key + ','

    name_str = name_str[:-1]
    value_str = value_str[:-1]

    db.query(f'insert into {table} ({name_str}) values ({value_str})', **kwargs)

def select(table = None, *args, **kwargs):
    if 'food' not in table and 'recipe' not in table:
        return

    # build param string
    param_str = ''
    if not args:
        # args is empty
        param_str = '*'
    else:
        for arg in args:
            param_str += arg + ','

        param_str = param_str[:-1]

    # execute query
    conn = db.get_connection()
    return conn.query(f'select {param_str} from {table}', False, **kwargs)

def main():
    setup()

    stuff = select('food')
    for row in stuff:
        print(row)

if __name__ == '__main__':
    main()
