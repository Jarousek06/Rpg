from flask import Flask, render_template, abort, url_for

app = Flask(__name__, static_folder='static')

rooms = {
    1: {"title": "Start", "image": "images/dm-start.png", "text": "Vstup do dungeonu.", "options": [("Jít do chodby A", 2)]},
    2: {"title": "Chodba A", "image": "images/dm-chodba-a.png", "text": "Temná chodba.", "options": [("Směr blok A", 3), ("Směr křižovatka A", 4)]},
    3: {"title": "Blok A", "image": "images/dm-blok-a.png", "text": "Zatarzené pole (blok).", "options": [("Vrať se", 2), ("Obejít a dál", 5)]},
    4: {"title": "Křižovatka A", "image": "images/dm-krizovatka-a.png", "text": "Rozcestí A.", "options": [("Křižovatka B", 6), ("Křižovatka C", 7)]},
    5: {"title": "Chodba B", "image": "images/dm-chodba-b.png", "text": "Pokračuješ chodbou.", "options": [("Dál k cíli", 8)]},
    6: {"title": "Křižovatka B", "image": "images/dm-krizovatka-b.png", "text": "Rozcestí B.", "options": [("Zpět", 2), ("Dál", 8)]},
    7: {"title": "Křižovatka C", "image": "images/dm-krizovatka-c.png", "text": "Rozcestí C.", "options": [("Dál", 8)]},
    8: {"title": "Cíl", "image": "images/dm-konec.png", "text": "Našel jsi konec/poklad.", "options": [("Začít znovu", 1)]},
    9: {"title": "Souboj", "image": "images/dm-souboj-a.png", "text": "Nepřítel!", "options": [("Utéct", 2), ("Vyhrát a jít dál", 8)]},
    10: {"title": "Blok B/C", "image": "images/dm-blok-b.png", "text": "Další bloky.", "options": [("Dál", 2), ("Alternativně", 3)]},
    11: {"title": "Blok C", "image": "images/dm-blok-c.png", "text": "Zatarzeno jinak.", "options": [("Zpět", 2)]},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dungeon/<int:room_id>')
def dungeon(room_id):
    room = rooms.get(room_id)
    if not room:
        abort(404)
    return render_template('dungeon.html', room=room, room_id=room_id)

if __name__ == '__main__':
    app.run(debug=True)