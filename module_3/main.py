from flask import Flask
import random 

app = Flask(__name__)
    
facts_list = ["Elon Musk mengklaim bahwa jejaring sosial dirancang untuk membuat kita tetap berada di dalam platform, sehingga kita menghabiskan waktu sebanyak mungkin untuk melihat konten.", 
            "Menurut sebuah penelitian yang dilakukan pada tahun 2018, lebih dari 50% orang berusia 18 hingga 34 tahun menganggap diri mereka ketergantungan pada ponsel pintar mereka.", 
            "Jejaring sosial memiliki sisi positif dan negatif, dan kita harus menyadari keduanya saat menggunakan platform ini.", 
            "Studi tentang kecanduan teknologi adalah salah satu bidang penelitian ilmiah modern yang paling relevan."]

element = ["+-/*!&$#?=@<>"]

@app.route("/")
def hello_world():
    return '<h1>Hello, Just Me!</h1>'

@app.route("/random_fact")
def facts():
    return f'<p>{random.choice(facts_list)}</p>'

@app.route("/element")
def gen_pass():
    element = "+-/*!&dknjfieba$#?=@<>,"
    password = ""
    for _ in range(8):
        password += random.choice(element)  
    return f'<p>{password}</p>'

app.run(debug=True)