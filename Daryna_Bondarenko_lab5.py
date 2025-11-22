from flask import Flask, render_template, session, redirect, url_for, request

app = Flask(__name__)
app.secret_key = "lab5_secret_key" 

BOOKS = [
    {
        "id": 1,
        "title": "Птахи та інші оповідання",
        "author": "Дафна Дю Мор’є",
        "price": 350,
        "rating": 4.9,
        "image": "book1.jpg"
    },
    {
        "id": 2,
        "title": "Гордість і упередження",
        "author": "Джейн Остін",
        "price": 300,
        "rating": 4.9,
        "image": "book2.jpg"
    },
    {
        "id": 3,
        "title": "Нічний споглядач",
        "author": "Трейсі Сьєрра",
        "price": 231,
        "rating": 4.8,
        "image": "book3.jpg"
    },
    {
        "id": 4,
        "title": "Дарлінґи",
        "author": "Ханна Маккінон",
        "price": 315,
        "rating": 4.5,
        "image": "book4.jpg"
    },
    {
        "id": 5,
        "title": "Іліада",
        "author": "Гомер",
        "price": 455,
        "rating": 5.0,
        "image": "book5.jpg"
    },
    {
        "id": 6,
        "title": "Щоденник мандрівного кота",
        "author": "Хіро Арікава",
        "price": 430,
        "rating": 4.9,
        "image": "book6.jpeg"
    },
    {
        "id": 7,
        "title": "Воно",
        "author": "Стівен Кінг",
        "price": 430,
        "rating": 4.9,
        "image": "book7.jpg"
    },
    {
        "id": 8,
        "title": "Перетворення",
        "author": "Ф. Кафка",
        "price": 335,
        "rating": 5.0,
        "image": "book8.jpg"
    },
    {
        "id": 9,
        "title": "Сад Гетсиманський",
        "author": "Іван Багряний",
        "price": 425,
        "rating": 5.0,
        "image": "book9.jpg"
    },
    {
        "id": 10,
        "title": "Дракула",
        "author": "Брем Стокер",
        "price": 465,
        "rating": 5.0,
        "image": "book10.jpg"
    },
]

@app.context_processor
def inject_cart_count():
    cart = session.get("cart", [])
    return {"cart_count": len(cart)}


def get_cart_books():
    cart_ids = session.get("cart", [])
    return [book for book in BOOKS if book["id"] in cart_ids]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/books")
def books():
    return render_template("books.html", books=BOOKS)

@app.route("/cart")
def cart():
    cart_books = get_cart_books()
    total_price = sum(book["price"] for book in cart_books)
    return render_template("cart.html", books=cart_books, total_price=total_price)


@app.route("/add-to-cart/<int:book_id>", methods=["POST"])
def add_to_cart(book_id):
    cart = session.get("cart", [])
    if book_id not in cart:
        cart.append(book_id)
    session["cart"] = cart
    return redirect(request.referrer or url_for("books"))


@app.route("/remove-from-cart/<int:book_id>", methods=["POST"])
def remove_from_cart(book_id):
    cart = session.get("cart", [])
    if book_id in cart:
        cart.remove(book_id)
    session["cart"] = cart
    return redirect(url_for("cart"))

@app.route("/authors")
def authors():
    return render_template("authors.html")


if __name__ == "__main__":
    app.run(debug=True)


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
