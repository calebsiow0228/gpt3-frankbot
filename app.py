from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from frankbot import ask, append_interaction_to_chat_log
app = Flask(__name__)
# if for some reason your conversation with Jabe gets weird, change the secret key
app.config['SECRET_KEY'] = 'Gp57Dkjq7uOAP2j'
@app.route('/frankbot', methods=['POST'])
def frank():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
    chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)
if __name__ == '__main__':
 app.run(debug=True)