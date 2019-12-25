from flask import Flask, jsonify
from bot import bot

@app.route('/healthcheck')
def any():
    result = bot.get_me()

    if result:
        return jsonify(result)
    return jsonify({'result': None})


