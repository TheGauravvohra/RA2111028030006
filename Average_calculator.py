from flask import Flask, jsonify

app = Flask(__name__)

def fetch_numbers(numberid):
    return [1, 3, 5, 7]  

def process_and_store_numbers(numbers):
    pass  

def calculate_average():
    numbers = fetch_numbers(123)  
    if numbers:
        return sum(numbers) / len(numbers)
    else:
        return None

def construct_response():
    numbers = fetch_numbers(123)  
    avg = calculate_average()
    
    response = {
        'windowPrevState': [],
        'windowCurrState': numbers,
        'numbers': numbers,
        'avg': avg
    }
    return response

@app.route('/numbers/<int:numberid>', methods=['GET'])
def calculate_average_endpoint(numberid):
    numbers = fetch_numbers(numberid)
    if numbers:
        process_and_store_numbers(numbers)
        response = construct_response()
        return jsonify(response)
    else:
        return jsonify({'error': 'Failed to fetch numbers'}), 500

if __name__ == '__main__':
    app.run(debug=True)
