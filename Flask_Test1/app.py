"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask

import pyodbc

DATABASE_CONFIG ={
    'Driver': 'ODBC Driver 17 for SQL Server',
    'Server': 'msu-chemometrics1.database.windows.net',
    'Database': 'spectrums',
    'UID': 'ruslixag',
    'Password': 'Ruslix1996'
}

def getConnection():
    connection = pyodbc.connect('''DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'''.format(
        DATABASE_CONFIG['Driver'],
        DATABASE_CONFIG['Server'],
        DATABASE_CONFIG['Database'],
        DATABASE_CONFIG['UID'],
        DATABASE_CONFIG['Password']))
    return connection 

app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/')
def hello():
    """Renders a sample page."""
    res = ''
    try:
        connection = getConnection()
        cur = connection.cursor()
        cur.execute('select * from [dbo].[SC1_Measurement];')
        rows = cur.fetchall()

        res = ''
        for idx, row in enumerate(rows):
            res += 'Row {}: {}<br>'.format(idx,row)
    except Exception as ee:
        print('Error:',ee)
    finally:
        connection.close()

    return '''<H1>Hello World!</H1><br>''' + res

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
