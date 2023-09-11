from nltk.chat.util import Chat
q1=r'(.*) your name (.*) company'
a1=['my name is jayendra sharma']
q2=r'what is your age'
a2=['my name age is mei ku btau']
qa_pair=[
    [q1,a1], [q2,a2],
]
cb=Chat(qa_pair)

from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def home():

    text='hi'
    global cb
    if request.args.get('q')!=None:
        que=request.args.get('q')
        text=cb.respond(que)
        if text==None:
            text='unkown'
    return render_template('/chatbot.html',resp=text)

@app.route('/new',methods=['GET'])
def new():
    return "<html><h1> awesome</h1></html>"

app.run(debug=True)

# {{}}= templates tag
# {%%}=any value
# <h1>chatty chater</h1>
        #<p>this is a simple chatbot app</p>
        
        #<form>
            #<label> enter the name </label>
            #<input type="text" name="q">
            #<input type="submit" value="ask">
        #</form>