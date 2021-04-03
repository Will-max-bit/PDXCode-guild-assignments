from flask import Flask, render_template, request
import random
import string


def pass_gen(length):
    chars = list(string.ascii_letters + string.digits)
    y = 0
    out_lst = []
    while y < length:
        out_lst.append(random.choice(chars))
        y +=1
    return "".join(out_lst)

app = Flask('pass_gen')

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form['pass_gen'])
        password = pass_gen(length)
        pass_len = len(password)
    return render_template('index.html', password=password, pass_len=pass_len) 






app.run()