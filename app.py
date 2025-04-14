import os
import logging
from flask import Flask, render_template, request, jsonify

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Create Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "mlbb_fuzzy_secret")

# Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_recycle": 300,
    "pool_pre_ping": True,
}

# Debug the database URL
logger.info(f"Database URL configured: {app.config['SQLALCHEMY_DATABASE_URI']}")

# Import these after app config to avoid circular imports
from database import db
from models import Hero, HeroStrength, HeroWeakness, UserPreference
from fuzzy_logic import evaluate_hero, get_hero_recommendations
from hero_data import get_hero_by_id, get_heroes_by_role, get_all_heroes, get_all_roles

# Initialize the app with extensions
db.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()

@app.route("/")
def index():
    """Render the main page with hero selection form"""
    roles = get_all_roles()
    heroes = get_all_heroes()
    return render_template("index.html", roles=roles, heroes=heroes)

@app.route("/evaluate", methods=["POST"])
def evaluate():
    """Process form data and evaluate hero using fuzzy logic"""
    try:
        # Get form data
        hero_id = request.form.get("hero_id")
        
        # Get attributes from form
        preferences = {
            "damage": float(request.form.get("damage", 5)),
            "durability": float(request.form.get("durability", 5)),
            "crowd_control": float(request.form.get("crowd_control", 5)),
            "mobility": float(request.form.get("mobility", 5)),
            "difficulty": float(request.form.get("difficulty", 5))
        }
        
        # Evaluate single hero if selected
        if hero_id:
            hero = get_hero_by_id(hero_id)
            if hero:
                result = evaluate_hero(hero, preferences)
                return render_template("results.html", 
                                      single_hero=hero, 
                                      evaluation=result)
            
        # Get role-based recommendations
        role = request.form.get("role")
        if role:
            heroes = get_heroes_by_role(role)
            recommendations = get_hero_recommendations(heroes, preferences)
            return render_template("results.html", 
                                  recommendations=recommendations, 
                                  role=role,
                                  preferences=preferences)
        
        # Default case if neither hero nor role is specified
        return render_template("index.html", 
                             error="Please select a hero or role for evaluation",
                             roles=get_all_roles(),
                             heroes=get_all_heroes())
    
    except Exception as e:
        logging.error(f"Error in evaluate: {str(e)}")
        return render_template("index.html", 
                             error=f"An error occurred: {str(e)}",
                             roles=get_all_roles(),
                             heroes=get_all_heroes())

@app.route("/api/heroes")
def api_heroes():
    """API endpoint to get heroes by role"""
    role = request.args.get("role")
    if role:
        heroes = get_heroes_by_role(role)
        return jsonify(heroes)
    return jsonify(get_all_heroes())

@app.route("/api/evaluate_hero/<hero_id>")
def api_evaluate_hero(hero_id):
    """API endpoint to evaluate a specific hero"""
    try:
        hero = get_hero_by_id(hero_id)
        if not hero:
            return jsonify({"error": "Hero not found"}), 404
        
        # Get preference parameters
        preferences = {
            "damage": float(request.args.get("damage", 5)),
            "durability": float(request.args.get("durability", 5)),
            "crowd_control": float(request.args.get("crowd_control", 5)),
            "mobility": float(request.args.get("mobility", 5)),
            "difficulty": float(request.args.get("difficulty", 5))
        }
        
        result = evaluate_hero(hero, preferences)
        return jsonify(result)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
