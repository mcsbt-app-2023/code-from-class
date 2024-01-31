from flask import Flask, jsonify, request

translations = {
  "en": "hello",
  "es": "hola",
  "it": "ciao",
}

app = Flask(__name__)

@app.route("/translation/<language>")
def get_language(language):
    if language.lower() not in translations:
        return jsonify({"error": "translation not found"}), 404
    else:
        return jsonify({language.lower(): translations[language.lower()]}), 200
    

#{
#  "language": "fr",
#  "translation": "bonjour"
#}
@app.route("/translation", methods=["PUT"])
def create_translation():
    translation = request.get_json()

    translations[translation["language"]] = translation["translation"]

    return "Translation create", 201

app.run()