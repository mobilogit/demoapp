from flask import Flask, render_template, request, redirect, url_for
import time
from math import sqrt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

  if request.method == 'POST':
    seconds = request.form.get('seconds')
    duration = '---'
    if seconds.isdigit():
      return redirect(url_for('loop', seconds=seconds))
  else:
    seconds = 3
    duration = request.args.get('duration')
    if not duration:
       duration = '---'

  content = f'''
    <html>
      <body>     
        <h1>CPU LOAD</h1>
        <p>Last execution took {duration} seconds</p> 
        <form action = { url_for("index") } method = "post">
          <p>Enter number of seconds:</p>
          <p><input type = "text" name = "seconds" value="{seconds}" /></p>
          <p><input type = "submit" value = "submit" /></p>
        </form>     
      </body>
    </html>
'''

  return content
  

@app.route('/loop/<seconds>')
def loop(seconds):
    start = time.time()
    while time.time() - start < int(seconds):
        value = sqrt(64*64*64*64*64)

    end = time.time()
    duration = round(end - start, 2)
    return redirect(url_for('index', duration=duration))


if __name__ == '__main__':
    app.run(debug=True)
