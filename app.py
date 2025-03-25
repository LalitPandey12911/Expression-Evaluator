from flask import Flask, render_template, request, jsonify
from utils.conversion import (
    infix_to_postfix, infix_to_prefix, postfix_to_infix, prefix_to_infix,
    evaluate_postfix, evaluate_prefix, evaluate_infix
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    data = request.json
    expression = data.get('expression')
    conversion_type = data.get('conversion_type')

    conversion_methods = {
        "infix_to_postfix": infix_to_postfix,
        "infix_to_prefix": infix_to_prefix,
        "postfix_to_infix": postfix_to_infix,
        "prefix_to_infix": prefix_to_infix
    }

    if conversion_type in conversion_methods:
        result_data = conversion_methods[conversion_type](expression)
        return jsonify(result_data)  # Includes steps
    else:
        return jsonify({"result": "Conversion type not implemented.", "steps": []})

@app.route('/evaluate', methods=['POST'])
def evaluate():
    data = request.json
    expression = data.get('expression')
    eval_type = data.get('eval_type')

    eval_methods = {
        "postfix": evaluate_postfix,
        "prefix": evaluate_prefix,
        "infix": evaluate_infix
    }

    if eval_type in eval_methods:
        try:
            result_data = eval_methods[eval_type](expression)
            return jsonify(result_data)  # Includes steps
        except Exception as e:
            return jsonify({"result": f"Error: {str(e)}", "steps": []})
    else:
        return jsonify({"result": "Evaluation type not implemented.", "steps": []})

if __name__ == '__main__':
    app.run(debug=True)
