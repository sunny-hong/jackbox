#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

game_stages = [
    {
        'stage_id': 1,
        'question': u'What is the best thing that happened this year?',
        'answers':[
            {'player_id':1, 'player_answer':u'Haikyuu new season came out.'},
            {'player_id':2, 'player_answer':u'Celebrating our anniversary. '},
            {'player_id':3, 'player_answer':u'Skiing on a weekday!'}
        ],
        'has_question': True,
        'has_answers': True
    },
    {
        'stage_id': 2,
        'question': None,
        'answers': [],
        'has_question': False,
        'has_answers':False
    },
    {
        'stage_id': 3,
        'question': None,
        'answers': [],
        'has_question': False,
        'has_answers':False
    }
]

@app.route('/api/v1.0/stages', methods = ['POST'])
# @app.errorhandler(404)

# @app.route('/api/v1.0/<int:stage_id>', methods = ['GET']))
# def get_game_stages(stage_id):
#     stage = [stage for stage in game_stages if stage['stage_id'] == stage_id]
#     if len(stage) == 0:
#         abort(404)
#     return jsonify({'game_stage': stage[0]})
#
# def not_found(error):
#     return make_response(jsonify({'error':'Not found'}), 404)


def create_stage():
    if not request.json or not 'question' in request.json:
        abort(400)
    stage = {
        'stage_id': game_stages[-1]['stage_id'] + 1,
        'question': request.json['question'],
        'has_question':True,
        'has_answers':False,
        'answers':None
    }
    game_stages.append(stage)
    return jsonify({'stage':game_stages}), 201

if __name__ == '__main__':
    app.run(debug=True)
