import requests
from flask import jsonify
from flask import Flask, render_template, request

OMDB_API_KEY = '1cc488d6'

app = Flask(__name__)

book1 = [
         {"title": "Inception", "book": "Book 1", "page": 1, "slot":1},
         {"title": "The Dark Knight", "book": "Book 1", "page": 1, "slot":2},
         {"title": "Interstellar", "book": "Book 1", "page": 1, "slot":3},
         {"title": "Dunkirk", "book": "Book 1", "page": 1, "slot":4},
         {"title": "Tenet", "book": "Book 1", "page": 2, "slot":1}
         ]
book2 = [
         {"title": "The Matrix", "book": "Book 2", "page": 1, "slot":1},
         {"title": "seven", "book": "Book 2", "page": 1, "slot":2},
         {"title": "eight", "book": "Book 2", "page": 1, "slot":3},
         {"title": "nine", "book": "Book 2", "page": 1, "slot":4},
         {"title": "ten", "book": "Book 2", "page": 2, "slot":1}
         ]
book3 = [
         {"title": "eleven", "book": "Book 3", "page": 1, "slot":1},
         {"title": "twelve", "book": "Book 3", "page": 1, "slot":2},
         {"title": "thirteen", "book": "Book 3", "page": 1, "slot":3},
         {"title": "fourteen", "book": "Book 3", "page": 1, "slot":4},
         {"title": "fifteen", "book": "Book 3", "page": 2, "slot":1}
         ]
book4 = [
            {"title": "sixteen", "book": "Book 4", "page": 1, "slot":1},
            {"title": "seventeen", "book": "Book 4", "page": 1, "slot":2},
            {"title": "eighteen", "book": "Book 4", "page": 1, "slot":3},
            {"title": "nineteen", "book": "Book 4", "page": 1, "slot":4},
            {"title": "twenty", "book": "Book 4", "page": 2, "slot":1}
        ]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check():
    data = request.json
    item = data.get('item', '').strip().lower()
    all_books = book1 + book2 + book3 + book4
    for dvd in all_books:
        if dvd["title"].lower() == item:
            # Fetch OMDb info
            omdb_url = f"http://www.omdbapi.com/?t={dvd['title']}&apikey={OMDB_API_KEY}"
            omdb_response = requests.get(omdb_url, timeout = 5)
            omdb_data = omdb_response.json()
            # Prepare result
            result = {
                'location': f'{dvd["book"]}, Page {dvd["page"]}, Slot {dvd["slot"]}',
                'omdb': {
                    'Title': omdb_data.get('Title', 'N/A'),
                    'Year': omdb_data.get('Year', 'N/A'),
                    'Rated': omdb_data.get('Rated', 'N/A'),
                    'Released': omdb_data.get('Released', 'N/A'),
                    'Runtime': omdb_data.get('Runtime', 'N/A'),
                    'Genre': omdb_data.get('Genre', 'N/A'),
                    'Director': omdb_data.get('Director', 'N/A'),
                    'Actors': omdb_data.get('Actors', 'N/A'),
                    'Plot': omdb_data.get('Plot', 'N/A'),
                    'Ratings': omdb_data.get('Ratings', []),
                    'Poster': omdb_data.get('Poster', '')
                }
            }
            return jsonify(result)
    return jsonify({'result': 'Not found. Try checking the title or manually checking the books.'})
if __name__ == '__main__':
    app.run(debug=True)
