from flask import Flask

app = Flask(__name__)
import socket

def get_ip_address():
    try:
        # Get the hostname
        host_name = socket.gethostname()
        
        # Get the IP address associated with the hostname
        ip_address = socket.gethostbyname(host_name)
        
        return ip_address

    except socket.error as e:
        print(f"Error: {e}")
        return None

# Call the function and print the result
ip_address = get_ip_address()

if ip_address:
    print(f"IP Address: {ip_address}")
else:
    print("Unable to retrieve the IP address.")

# Endpoint 1
@app.route('/')
def home():
    return 'Welcome to the home page!'

# Endpoint 2
@app.route('/about')
def about():
    return 'This is the about page.'

# Endpoint 3
@app.route('/contact')
def contact():
    return 'You can contact us at contact@example.com.'

# Endpoint 4
@app.route('/products')
def products():
    return 'Here is a list of products.'

# Endpoint 5
@app.route('/api/data')
def api_data():
    return '{"data": "This is sample data from the API."}'

if __name__ == '__main__':
    # Run the app on port 8000
    app.run(debug=True, port=8000)
