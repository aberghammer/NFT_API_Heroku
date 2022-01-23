# main.py
from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

@app.route('/<id>')
def ring(id):
    attributes = []
    _add_attribute(attributes, "followers", 300000, id, display_type='boost_number')

    return jsonify({
        'name': "unrevealed",
        "description": "unrevealed",
        "image": request.url_root + url_for( 'static', filename='preview.gif'),
        "external_url": "..",
        "attributes": attributes,
    })


def _add_attribute(existing, attribute_name, options, token_id, display_type=None):
    trait = {
        'trait_type': attribute_name,
        'value': options
    }
    if display_type:
        trait['display_type'] = display_type
    existing.append(trait)

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run()