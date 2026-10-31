from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee"
    },
    {
        "id": 3,
        "title": "1984",
        "author": "George Orwell"
    }
]

@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:book_id>', methods=['GET'])
def get_books_from_id(book_id):
    for book in books:
        if book.get('id') == book_id:
            return jsonify(book)

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book_updated = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == book_id:
            books[index].update(book_updated)
            
    return jsonify(
        {
            'message': 'Livro alterado com sucesso!',
            'book': books[index]
        }
    )    

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(
        {
            'message': 'Livro adicionado com sucesso!',
            'book': new_book
        }
    )

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    for index, book in enumerate(books):
        if book.get('id') == book_id:
            books.pop(index)

        return jsonify(
            {
                'message': 'Livro deletado com sucesso!',
                'book': books[index]
            }
        )

app.run(port=3000, host='localhost', debug=True)