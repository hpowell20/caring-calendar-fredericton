from flask import Blueprint, jsonify

import logging
import random

logger = logging.getLogger(__name__)
blueprint = Blueprint('fact', __name__)

FACTS = ['A flock of crows is known as a murder',
         'If you lift a kangaroo''s tail off the ground it can''t hop',
         'Bananas are curved because they grow towards the sun',
         'Recycling one glass jar saves enough energy to watch television for 3 hours',
         'The Titanic was the first ship to use the S.O.S signal',
         'An apple, potato, and onion all taste the same if you eat them with your nose plugged']


@blueprint.route('/facts/random')
def get_random_fact():
    index = random.randint(0, len(FACTS) - 1)
    random_fact = FACTS[index]

    return jsonify({'random_fact': random_fact})
