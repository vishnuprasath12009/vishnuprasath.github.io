from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>

<head>

<title>Biodata of Vishnu Prasath</title>

<style>

body{
    margin:0;
    background:white;
    font-family:Arial, sans-serif;
    color:#222;
}


.container{
    width:80%;
    margin:auto;
    padding:40px;
    text-align:center;
    animation:fade 2s;
}


@keyframes fade{
    from{
        opacity:0;
        transform:translateY(30px);
    }
    to{
        opacity:1;
        transform:translateY(0);
    }
}


.profile{
    width:180px;
    height:180px;
    border-radius:50%;
    object-fit:cover;
    border:5px solid #111;
    animation:float 3s infinite;
}


@keyframes float{
    50%{
        transform:translateY(-15px);
    }
}


h1{
    font-size:45px;
    color:#0b3d91;
}


.card{
    background:#f5f5f5;
    padding:25px;
    margin:25px auto;
    border-radius:20px;
    max-width:800px;
    box-shadow:0 5px 20px #aaa;
}


h2{
    color:#0b3d91;
}


.info{
    display:flex;
    justify-content:center;
    gap:30px;
    flex-wrap:wrap;
}


.box{
    background:white;
    padding:20px;
    border-radius:15px;
    width:200px;
    box-shadow:0 3px 10px #bbb;
}


.army{
    background:#111;
    color:white;
}


</style>

</head>


<body>


<div class="container">


<img class="profile"
src="/website/photo.jpg">


<h1>BIODATA OF VISHNU PRASATH</h1>


<div class="card">


<h2>About Me</h2>


<p>
Hi everyone, I am S. Vishnu Prasath from Tamil Nadu, Tirunelveli.
I am a Class 12 student studying at Amrita Vidyalayam, Kanyakumari
in the batch of 2026-2027.
</p>


<p>
I am different from many others because I have a clear goal:
to become an officer in the Indian Army and serve my nation.
</p>


</div>



<div class="info">


<div class="box">
<h3>Class</h3>
<p>12th</p>
</div>


<div class="box">
<h3>Height</h3>
<p>190 cm</p>
</div>


<div class="box">
<h3>Weight</h3>
<p>70 kg</p>
</div>


</div>



<div class="card army">


<h2>My Aim 🇮🇳</h2>

<p>
My dream is to become an Indian Army officer.
I believe in discipline, courage, dedication and service to the country.
</p>


</div>


</div>


</body>

</html>
"""


app.run(host="0.0.0.0", port=5000, debug=True)
