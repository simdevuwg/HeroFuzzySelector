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

# Initialize the app with extensions
db.init_app(app)

# Create database tables if they don't exist
with app.app_context():
    db.create_all()
    
    # Import database manager here to avoid circular imports
    from database_manager import create_initial_data, get_hero_by_id, get_heroes_by_role, get_all_heroes, get_all_roles
    
    # Populate database with initial data if it's empty
    create_initial_data()

@app.route("/")
def index():
    """Render the main page with hero selection form"""
    roles = get_all_roles()
    heroes = get_all_heroes()
    return render_template("index.html", roles=roles, heroes=heroes)

@app.route("/admin")
def admin():
    """Render the admin page for managing the hero database"""
    from database_manager import get_all_heroes
    
    # Get query parameters for messages
    message = request.args.get("message")
    message_type = request.args.get("type", "info")
    
    # Get all heroes from database
    heroes = get_all_heroes()
    
    return render_template(
        "admin.html", 
        heroes=heroes, 
        message=message, 
        message_type=message_type
    )

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

# Database CRUD API Endpoints

@app.route("/api/heroes/<int:hero_id>", methods=["GET"])
def api_get_hero(hero_id):
    """API endpoint to get a specific hero"""
    from database_manager import get_hero_by_id
    
    hero = get_hero_by_id(hero_id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    return jsonify(hero)

@app.route("/api/heroes", methods=["POST"])
def api_add_hero():
    """API endpoint to add a new hero"""
    from database_manager import add_hero
    
    hero_data = request.json
    if not hero_data:
        return jsonify({"error": "No data provided"}), 400
    
    # Validate required fields
    required_fields = ["name", "role"]
    for field in required_fields:
        if field not in hero_data:
            return jsonify({"error": f"Missing required field: {field}"}), 400
    
    # Add hero to database
    result = add_hero(hero_data)
    if not result:
        return jsonify({"error": "Failed to add hero"}), 500
    
    return jsonify(result), 201

@app.route("/api/heroes/<int:hero_id>", methods=["PUT"])
def api_update_hero(hero_id):
    """API endpoint to update a hero"""
    from database_manager import update_hero, get_hero_by_id
    
    # Check if hero exists
    hero = get_hero_by_id(hero_id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    hero_data = request.json
    if not hero_data:
        return jsonify({"error": "No data provided"}), 400
    
    # Update hero in database
    result = update_hero(hero_id, hero_data)
    if not result:
        return jsonify({"error": "Failed to update hero"}), 500
    
    return jsonify(result)

@app.route("/api/heroes/<int:hero_id>", methods=["DELETE"])
def api_delete_hero(hero_id):
    """API endpoint to delete a hero"""
    from database_manager import delete_hero, get_hero_by_id
    
    # Check if hero exists
    hero = get_hero_by_id(hero_id)
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    # Delete hero from database
    result = delete_hero(hero_id)
    if not result:
        return jsonify({"error": "Failed to delete hero"}), 500
    
    return jsonify({"success": True, "message": f"Hero {hero_id} deleted successfully"})
