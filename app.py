from flask import Flask, request 
import pandas as pd 
import sqlite3
app = Flask(__name__) 

# mendapatkan keseluruhan data dari <data_name>
@app.route('/data/get/<data_name>', methods=['GET']) 
def get_data(data_name): 
    conn = sqlite3.connect("data/chinook.db")
    data = pd.read_sql_query("SELECT firstname, lastname, email, company, \
                                 invoiceid, invoicedate, billingcountry, total \
                                 FROM invoices \
                                 left join customers \
                                 on invoices.customerId = customers.customerId\
                                 WHERE Email LIKE '%@apple%'", conn)
    return (data.to_json())

@app.route('/data/get/artist/<data_name>', methods=['GET']) 
def get_data2(data_name): 
    conn = sqlite3.connect("data/chinook.db")
    data = pd.read_sql_query("SELECT tracks.*, albums.Title, genres.Name AS GenreName,\
                            artists.Name AS ArtistName \
                            FROM tracks \
                            LEFT JOIN albums \
                            ON albums.AlbumId=tracks.AlbumId \
                            LEFT JOIN genres \
                            ON genres.GenreId=tracks.GenreId \
                            LEFT JOIN artists \
                            ON artists.ArtistId=albums.ArtistId ", conn, index_col='TrackId')
    return (data.to_json())

@app.route('/data/get/genre/<data_name>/<value>', methods=['GET']) 
def get_genre(data_name, value): 
    conn = sqlite3.connect("data/chinook.db")
    data = pd.read_sql_query("SELECT tracks.*, albums.Title, genres.Name AS GenreName,\
                            artists.Name AS ArtistName \
                            FROM tracks \
                            LEFT JOIN albums \
                            ON albums.AlbumId=tracks.AlbumId \
                            LEFT JOIN genres \
                            ON genres.GenreId=tracks.GenreId \
                            LEFT JOIN artists \
                            ON artists.ArtistId=albums.ArtistId ", conn, index_col='TrackId')

    mask = data['GenreName'] == value
    data = data[mask]
    return (data.to_json())

# mendapatkan data dengan filter nilai <value> pada kolom <column>
@app.route('/data/get/equal/<data_name>/<column>/<value>', methods=['GET']) 
def get_data_equal(data_name, column, value): 
    conn = sqlite3.connect("data/chinook.db")
    data = pd.read_sql_query("SELECT c.Country, c.FirstName, c.LastName, invoices.Total, \
                           invoices.InvoiceDate \
                           FROM customers as c \
                           LEFT JOIN invoices \
                           ON c.CustomerId = invoices.CustomerId",conn)
    mask = data[column] == value
    data = data[mask]
    return (data.to_json())

if __name__ == '__main__':
    app.run(debug=True, port=5000) 