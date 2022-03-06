import pymysql as db

def insertCarbonPrice(price, diff):
    connection = connectDB()
    cursor= connection.cursor(buffered=True)
    cursor.callproc('insert_carbon',[price, diff])
    connection.commit()
    disconnectDB(connection)
    return

def insertSaltPrice(price, diff):
    connection = connectDB()
    cursor = connection.cursor(buffered=True)
    cursor.callproc('insert_salt',[price, diff])
    connection.commit()
    disconnectDB(connection)
    return

def getLatestCarbonFromDB():
    connection = connectDB()
    cursor= connection.cursor()
    cursor.callproc('get_latest_carbon')
    result = cursor.fetchall()
    for r in result:
        if r is not None:
            disconnectDB(connection)
            return r
    else: 
        disconnectDB(connection)
        #hack for none handle :/
        return [0, 0, 0, 0]


def getLatestSaltFromDB():
    connection = connectDB()
    cursor= connection.cursor()
    cursor.callproc('get_latest_salt')
    result = cursor.fetchall()
    for r in result:
        if r is not None:
            disconnectDB(connection)
        return r
    else: 
        disconnectDB(connection)
        #hack for none handle :/
        return [0, 0, 0, 0]
    

def connectDB():
    connection = db.connect(host="localhost", port=3306, user="root", password="Th3B3llJar", database="carbon_market_schema")
    if connection is not None:
        print('db connected')
        return connection

def disconnectDB(connection):
    if connection is not None:
        connection.close()
    return
