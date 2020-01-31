from flask import Flask, request 
app = Flask(__name__) 

@app.route('/json', methods=['POST']) 
def json_exmp():
    
    req = request.get_json(force=True) # melakukan parsing data json, menyimpannya sebagai dictionary
    
    name = req['name']
    age = req['age']
    address = req['address']
    
    return (f'''Hello {name}, your age is {age}, and your address in {address}
            ''')

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000