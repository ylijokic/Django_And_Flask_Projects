from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

# from database_setup import Team, Venue, Base

from datetime import datetime
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pinball-league.db'
db = SQLAlchemy(app)

class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    city = db.Column(db.String(250), nullable=False)
    state = db.Column(db.String(250), nullable=False)

class Team(db.Model):
    __tablename__ = 'team'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    # home_venue_id = Column(Integer, ForeignKey('venue.id'))

# Route to Home Page
@app.route("/")
def index():
    return render_template("index.html")

# Route to Get Teams and Create new Team
@app.route("/teams", methods=['GET', 'POST'])
def teams():
    if request.method == 'POST':
        team_name = request.form['name']
        new_team = Team(name=team_name)
        db.session.add(new_team)
        db.session.commit()
        return redirect('teams')
    else:
        teams = db.session.query(Team).all()
        return render_template("teams.html", teams=teams)

@app.route("/teams/delete/<int:team_id>")
def delete_team(team_id):
    team = db.session.query(Team).filter_by(id=team_id).one()
    db.session.delete(team)
    db.session.commit()
    return redirect('/teams')

# Route to Get Venue and Create new Venue
@app.route("/venues", methods=['GET', 'POST'])
def venues():
    if request.method == 'POST':
        venue_name = request.form['name']
        venue_address = request.form['address']
        venue_city = request.form['city']
        venue_state = request.form['state']
        new_venue = Venue(name=venue_name, address=venue_address, city=venue_city, state=venue_state)
        db.session.add(new_venue)
        db.session.commit()
        return redirect('venues')
    else:
        venues = db.session.query(Venue).all()
        return render_template("venues.html", venues=venues)

@app.route("/venues/delete/<int:venue_id>")
def delete_venue(venue_id):
    venue = db.session.query(Venue).filter_by(id=venue_id).one()
    db.session.delete(venue)
    db.session.commit()
    return redirect('/venues')

if __name__ == "__main__":
    app.run(debug=True)