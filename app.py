from flask import Flask, request, render_template 
  
# Flask constructor
app = Flask(__name__)   
  
# A decorator used to tell the application
# which URL is associated function
@app.route('/', methods =["GET", "POST"])
def gfg():
    return 'Hhhh'
if __name__ == '__main__':
    app.run(debug=True)