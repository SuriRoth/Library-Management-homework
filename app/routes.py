from flask import Flask, request, jsonify

app = Flask(__name__)

library = []

@app.route('/library', methods=['GET'])
def getLibrary():
    return jsonify(library), 200

@app.route('/library/<int:libraryID>', methods=['GET'])
def getLibraries(libraryID):
    lib = next((lib for lib in library if lib['id'] == libraryID), None)
    if lib:
        return jsonify(lib), 200
    return jsonify({'error': 'Library not found'}), 404

@app.route('/library', methods=['POST'])
def postLibrary():
    newLibrary = request.get_json()

    # Validation
    if not isinstance(newLibrary.get('name'), str):
        return jsonify({'error': 'Invalid name'}), 400
    if not isinstance(newLibrary.get('books'), dict):
        return jsonify({'error': 'Invalid books'}), 400
    if not isinstance(newLibrary.get('members'), list):
        return jsonify({'error': 'Invalid members'}), 400

    newLibrary['id'] = len(library) + 1
    library.append(newLibrary)
    return jsonify(newLibrary), 201

@app.route('/library/<int:libraryID>', methods=['PUT'])
def updateLibrary(libraryID):
    lib = next((lib for lib in library if lib['id'] == libraryID), None)
    if lib:
        updateData = request.get_json()

        # Validation
        if 'name' in updateData and not isinstance(updateData.get('name'), str):
            return jsonify({'error': 'Invalid name'}), 400
        if 'books' in updateData and not isinstance(updateData.get('books'), dict):
            return jsonify({'error': 'Invalid books'}), 400
        if 'members' in updateData and not isinstance(updateData.get('members'), list):
            return jsonify({'error': 'Invalid members'}), 400

        lib.update(updateData)
        return jsonify(lib), 200
    return jsonify({'error': 'Library not found'}), 404

@app.route('/library/<int:libraryID>', methods=['DELETE'])
def deleteLibrary(libraryID):
    global library
    library = [lib for lib in library if lib['id'] != libraryID] 
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
     
     
@app.route('/books', methods=['POST'])
def addBook():
    newBook = request.get_json()
    # Validate the incoming data for the book
    if not isinstance(newBook.get('ISBN'), str):
        return jsonify({'error': 'Invalid ISBN'}), 400
    # Add the book to the library
    library.append(newBook)
    return jsonify(newBook), 201


@app.route('/books/<string:ISBN>', methods=['DELETE'])
def removeBook(ISBN):
    global library
    library = [book for book in library if book.get('ISBN') != ISBN]
    return '', 204


@app.route('/books/<string:ISBN>', methods=['GET'])
def viewBook(ISBN):
    book = next((book for book in library if book.get('ISBN') == ISBN), None)
    if book:
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404


@app.route('/books/<string:ISBN>', methods=['PUT'])
def updateBook(ISBN):
    book = next((book for book in library if book.get('ISBN') == ISBN), None)
    if book:
        updateData = request.get_json()
        # Validate and update book details
        book.update(updateData)
        return jsonify(book), 200
    return jsonify({'error': 'Book not found'}), 404


@app.route('/members', methods=['POST'])
def addMember():
    newMember = request.get_json()
    # Validate the incoming data for the member
    if not isinstance(newMember.get('ID'), int):
        return jsonify({'error': 'Invalid ID'}), 400
    # Add the member to the library
    library.append(newMember)
    return jsonify(newMember), 201



@app.route('/members/<int:memberID>', methods=['DELETE'])
def removeMember(memberID):
    global library
    library = [member for member in library if member.get('ID') != memberID]
    return '', 204