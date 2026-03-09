import openai
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

openai.api_key = "YOUR_API_KEY"

book_data = {
    "title": "",
    "chapters": []
}

block_content = {}  # För att spara genererade block

@app.route('/')
def index():
    return render_template('index.html', book=book_data, block_content=block_content)

@app.route('/set_title', methods=['POST'])
def set_title():
    book_data['title'] = request.form['title']
    return redirect(url_for('index'))

@app.route('/add_chapter', methods=['POST'])
def add_chapter():
    chapter_name = request.form['chapter_name']
    if chapter_name:
        book_data['chapters'].append({'name': chapter_name, 'blocks': []})
    return redirect(url_for('index'))

@app.route('/add_block/<int:chapter_id>', methods=['POST'])
def add_block(chapter_id):
    block_name = request.form['block_name']
    block_rules = request.form['block_rules']
    if block_name:
        book_data['chapters'][chapter_id]['blocks'].append({
            'name': block_name,
            'rules': block_rules
        })
    return redirect(url_for('index'))

@app.route('/generate/<int:chapter_id>/<int:block_id>')
def generate(chapter_id, block_id):
    chapter = book_data['chapters'][chapter_id]
    block = chapter['blocks'][block_id]
    prompt = (
        f"Skriv blocket '{block['name']}' i kapitlet '{chapter['name']}' med följande regler: {block['rules']}. "
        f"Boktitel: {book_data['title']}. Anpassa stil, tempo och format enligt reglerna."
    )

    response = openai.ChatCompletion.create(
        model="gpt-4-turbo",
        messages=[
            {"role": "system", "content": "Du är en erfaren svensk författare."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1200,
        temperature=0.7
    )
    text = response.choices[0].message['content']
    block_content[f"{chapter_id}_{block_id}"] = text
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
