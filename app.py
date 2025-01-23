from flask import Flask, request, jsonify
from Final_me_testing_Copy1 import memory_rag_chain  # Import chatbot function

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_request():
    # Parse user input from the POST request
    user_input = request.json.get("question", "")  # Expecting {"question": "your query"} in the request body

    if not user_input:
        return jsonify({"error": "No question provided"}), 400

    # Process the user input using your chatbot logic
    try:
        response = memory_rag_chain(user_input)
        return jsonify({"response": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
