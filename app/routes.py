from app import app
from .forms import LoginForm
from flask import render_template, request
import requests


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html.j2')

@app.route('/pokemonsearch', methods = ['GET', 'POST'])
def pokemonsearch():
    if request.method == 'POST':
        pokemon = request.form.get('pokemon')
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        if response.ok:
            pokedex = {
                "name":response.json()['forms'][0]['name'],
                "ability":response.json()['abilities'][0]['ability']['name'],
                "base_xp":response.json()['base_experience'],
                "sprite": response.json()['sprites']['front_shiny']
            }
            return render_template('pokemonsearch.html.j2', stats = pokedex)
        else:
            error_string = "Page isn't working. "
            return render_template('pokemonsearch.html.j2', error = error_string,)
    return render_template('pokemonsearch.html.j2')
           
#jinja form day2
@app.route('/pokesearch', methods=['GET', 'POST'])
def pokesearch():
    form = LoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        #We will do the login stuff
        pokemon = request.form.get('pokemon').lower()
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
        response = requests.get(url)
        if response.ok:
            pokedex = {
                "name":response.json()['forms'][0]['name'],
                "ability":response.json()['abilities'][0]['ability']['name'],
                "base_xp":response.json()['base_experience'],
                "sprite": response.json()['sprites']['front_shiny']
            }
            return render_template('pokesearch.html.j2', stats = pokedex)
        else:
            error_string = "Page isn't working. "
            return render_template('pokesearch.html.j2', error = error_string, form = form)
    return render_template('pokesearch.html.j2', form = form)




# pokemon_search('poliwag')

# my_fighters= ['flareon', 'pachirisu', 'jirachi', 'roselia', 'aurorus']