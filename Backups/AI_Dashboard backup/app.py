from flask import Flask, render_template, request, jsonify
import os
from chatbot_teacher_assistant import handle_teacher_assistant
from chatbot_question_maker import handle_question_maker
from chatbot_document_analysis import handle_document_analysis

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teacher_assistant', methods=['GET', 'POST'])
def teacher_assistant():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        response = handle_teacher_assistant(user_input)
        return jsonify({'response': response})
    return render_template('chat_teacher_assistant.html')

@app.route('/question_maker', methods=['GET', 'POST'])
def question_maker():
    if request.method == 'POST':
        user_input = request.json.get('user_input')
        response = handle_question_maker(user_input)
        return jsonify({'response': response})
    return render_template('chat_question_maker.html')

@app.route('/document_analysis', methods=['GET', 'POST'])
def document_analysis():
    if request.method == 'POST':
        user_input = request.form.get('user_input', '')
        file = request.files.get('file', None)
        file_path = None
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            try:
                file.save(file_path)
            except Exception as e:
                return jsonify({'response': f"Error saving file: {e}"})
        try:
            response = handle_document_analysis(file_path, user_input)
        except Exception as e:
            return jsonify({'response': f"Error handling document analysis: {e}"})
        return jsonify({'response': response})
    return render_template('chat_document_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)