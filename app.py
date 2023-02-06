from flask import Flask, render_template, flash, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import PetForm



app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///adoption_agency"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False

debug = DebugToolbarExtension(app)

connect_db(app)


@app.route('/')
def show_home():
    """displays home page"""
    pets = Pet.query.all()
    return render_template('home.html',pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def add_pet_form():
    """add a new pet"""
    form = PetForm()
    
    if form.validate_on_submit():
        
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,species=species,photo_url=photo_url,age=age,notes=notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>/details')
def show_pet_details(pet_id):
    """displays pet details"""
    pet = Pet.query.get(pet_id)
    return render_template('pet_details.html', pet=pet)



@app.route('/<int:pet_id>/edit', methods=["GET", "POST"])
def edit_pet(pet_id):
    """display and process pet edit form"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)
   
    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        db.session.commit()
        return redirect('/')
    else:
        return render_template("edit_pet_form.html", form=form)



