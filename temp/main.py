from flask import *
app=Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        search=request.form['query']
        return redirect(f"/{search}")
    return render_template('index.html')


@app.route('/<userreq>',methods=['GET', 'POST'])
def recommend(userreq):
    if request.method == "POST":
        search=request.form['query']
        return redirect(f"/{search}")
    results='''<div class="flip-card">
      <div class="flip-card-inner">
        <div class="flip-card-front">
          <img src="https://images.gr-assets.com/books/1255292027m/6969361.jpg" alt="Avatar" style="width:300px;height:300px;">
        </div>
        <div class="flip-card-back">
          <h4>2 States: The Story of My Marriage</h4>
          <p>by Chetan Bhagat</p>
        </div>
      </div>
    </div>'''
    with open("templates/results.html", "w") as fo:
        fo.write(results)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000,debug=True)