from flask import Flask, render_template
app = Flask(__name__)
products = [
    {
        "name": "Crochet Sunflower",
        "price": "₹249",
        "image": "sunflower.jpg"
    },
    {
        "name": "Crochet Minion",
        "price": "₹249",
        "image": "minion.jpg"
    },
    {
        "name": "Crochet Penguin",
        "price": "₹229",
        "image": "penguin.jpg"
    },
    {   "name": "Crochet Sunflower Pot",
        "price": "₹299",
        "image": "sunflowerpot.jpg" 
    },
    {   "name": "Crochet Bouquet",
        "price": "₹499",
        "image": "bouquet.jpg"
    },
    {   "name": "Crochet WhiteFlower SnapClip",
        "price": "₹99",
        "image": "snapclip.jpg"
    },
    {   "name": "Crochet PinkFlower SnapClip",
        "price": "₹79",
        "image": "snapclip2.jpg"
    },
    {   "name": "Crochet Rose SnapClip",
        "price": "₹79",
        "image": "snapclip3.jpg"
    },
    {   "name": "Crochet sunflower SnapClip",
        "price": "₹79",
        "image": "sunflower snapclip.jpg"
    }
]
@app.route('/')
def home():
    return render_template("index.html", products=products)
@app.route("/order", methods=["POST"])
def order():
    name = request.form["customer_name"]
    product = request.form["product"]

    return f"""
    <h1>Order Placed Successfully 🎉</h1>
    <h2>Thank You {name}</h2>
    <p>Your order for <b>{product}</b> has been received.</p>
    <a href="/">Back to Home</a>
    """
if __name__ == "__main__":
    app.run(debug=True)