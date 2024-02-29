from flask import Flask, url_for, request, redirect

# Use name of current module (__name__) as argument.
app = Flask(__name__)

# function defining a dynamically added routing entry
def dynamical_routing_test():
   return f'Dynamically added route<br><a href={ url_for("hello_world") }>take me home</a>'

# adding dynamically a new route
app.add_url_rule('/dynamic', 'dynamic_route', dynamical_routing_test)

# home --> form to login
@app.route('/')
def hello_world():
    VERSION = 40
    content = f'''
      <html>
        <body>     
          <h1>{ VERSION }</h1>
          <form action = { url_for("login") } method = "post">
            <p>Enter Name:</p>
            <p><input type = "text" name = "user_name" /></p>
            <p><input type = "submit" value = "submit" /></p>
          </form>     
        <p><a href={ url_for("dynamic_route") }>dynamic link</a></p>
        </body>
      </html>
'''
    return content

# login action --> redirect to success
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['user_name']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success', name=user))

# show success and allow to go to home
@app.route('/success/<name>')
def success(name):
    return f'Welcome {name} <p><a href={ url_for("hello_world") }>take me home</a></p>'



if __name__ == '__main__':
	app.run()
