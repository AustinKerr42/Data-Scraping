import MySQLdb

def insertToTable(table, events):
    #connect to db
    # Hostname: account->website->manage->databases->under the database server column->ex. '50.62.209.147:3306'
    #   ->use everything before the ':'
    db = MySQLdb.connect("50.62.209.147","AustinK","secondOne2", "Events")

    #setup cursor
    cursor = db.cursor()

    #insert to table
    try:
        for event in events:
            cursor.execute("INSERT INTO "  + table + " VALUES (%s,%s,%s,%s,%s)",(event[0],event[1],event[2],event[3],event[4]))
            db.commit()
    except:     
        db.rollback()

    #show table
    cursor.execute("SELECT * FROM " + table + ";")

    print cursor.fetchall()

    db.close()
    return True