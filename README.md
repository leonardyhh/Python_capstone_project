# p4da-capstone-api
This is Algoritma's Python for Data Analysis Capstone Project. This project aims to create a simple API to fetch data from Heroku Server. 

As a Data Scientist, we demand data to be accessible. And as a data owner, we are careful with our data. As the answer, data owner create an API for anyone who are granted access to the data to collect them. In this capstone project, we will create Flask Application as an API and deploy it to Heroku Web Hosting. 
___
Data yang digunakan:  
chinook.db  

Environtments:   
python  
pandas  
flask  
gunicorn  
sqlite3  

Goals:  
Berhasil membuat Flask APP yang berfungsi sebagai API yang memberikan data dalam format JSON  
Berhasil membuat minimal 2 endpoint statis (atau lebih) dan 1 endpoint dinamis(atau lebih) menggunakan routing  
Berhasil melakukan deployment Flask APP ke Heroku  

Here's the list of its endpoints: 
```
1. /data/get/<data_name> , method = GET
getting customers detail with their invoices

2. /data/get/artist/<data_name>/<name> , method = GET
get artist, and their albums detail
return all <data_name> where the value is equal to artist name
  
3. /data/get/genre/<data_name>/<value> , method = GET
Return all <data_name> where the value is equal to <value>(genre)

4. /data/get/email/<data_name>/<email> , method = GET
Return all <data_name> where the value is equal to <email>

5. /data/get/track/<data_name> , method = GET
return all <data_name>
```

If you want to try it, you can access (copy-paste it) : 
- https://python-capstone-project.herokuapp.com/data/get/chinook.db
- https://python-capstone-project.herokuapp.com/data/get/artist/chinook.db/Accept
- https://python-capstone-project.herokuapp.com/data/get/genre/chinook.db/Jazz
- https://python-capstone-project.herokuapp.com/data/get/email/chinook.db/bjorn.hansen@yahoo.no
- https://python-capstone-project.herokuapp.com/data/get/track/chinook.db
- and so on, just follow the endpoint's pattern