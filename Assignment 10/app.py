from flask import Flask, jsonify

app = Flask(__name__)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


@app.route("/prime_number/<int:number>")
def prime_number(number):
    return jsonify({
        "Number": number,
        "isPrime": is_prime(number)
    })


airports = {
    "LFLL": {
        "name": "Lyon Saint-Exupery Airport",
        "city": "Lyon",
        "country": "FR"
    },
    "KJFK": {
        "name": "John F. Kennedy International Airport",
        "city": "New York",
        "country": "US"
    }
}


@app.route("/airport/<icao>")
def get_airport(icao):
    airport = airports.get(icao.upper())

    if airport:
        return jsonify({
            "icao": icao.upper(),
            "name": airport["name"],
            "city": airport["city"],
            "country": airport["country"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)