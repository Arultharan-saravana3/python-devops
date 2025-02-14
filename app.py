from flask import Flask, render_template, request
from flasgger import Swagger
from utils import calculate_bmi, calculate_bmr

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def index():
    """
    Page d'accueil
    ---
    responses:
      200:
        description: Page d'accueil avec le formulaire de calcul.
    """
    return render_template('index.html', bmi=None, bmr=None)

@app.route('/calculate', methods=['POST'])
def calculate():
    """
    Calcule le BMI et le BMR
    Cette route reçoit les données d'un formulaire et retourne le BMI et le BMR calculés.
    ---
    parameters:
      - name: weight
        in: formData
        type: number
        required: true
        description: Poids en kg.
      - name: height
        in: formData
        type: number
        required: true
        description: Taille en cm.
      - name: age
        in: formData
        type: number
        required: true
        description: Âge en années.
      - name: gender
        in: formData
        type: string
        required: true
        description: Genre ("male" ou "female").
    responses:
      200:
        description: Page affichant le BMI et le BMR calculés.
    """
    weight = float(request.form['weight'])
    height = float(request.form['height']) / 100  # conversion de cm en m pour le BMI
    age = int(request.form['age'])
    gender = request.form['gender']
    
    bmi = calculate_bmi(height, weight)
    bmr = calculate_bmr(height * 100, weight, age, gender)  # la hauteur doit être en cm pour le BMR
    
    return render_template('index.html', bmi=round(bmi, 2), bmr=round(bmr, 2))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
