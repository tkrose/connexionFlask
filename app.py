from flask import Flask, render_template
import connexion

#Create the application instance
app = connexion.App(__name__, specification_dir='./')

#Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

#Create a URL route in our application for "/"
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)