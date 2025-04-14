"""
This module contains the fuzzy logic implementation for the MLBB hero recommendation system.
"""
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import logging

# Create universals for each hero attribute
def create_fuzzy_system():
    """Create and return the fuzzy control system for hero evaluation"""
    
    # Input variables (attributes)
    damage = ctrl.Antecedent(np.arange(0, 11, 1), 'damage')
    durability = ctrl.Antecedent(np.arange(0, 11, 1), 'durability')
    crowd_control = ctrl.Antecedent(np.arange(0, 11, 1), 'crowd_control')
    mobility = ctrl.Antecedent(np.arange(0, 11, 1), 'mobility')
    difficulty = ctrl.Antecedent(np.arange(0, 11, 1), 'difficulty')
    
    # Output variable
    suitability = ctrl.Consequent(np.arange(0, 101, 1), 'suitability')
    
    # Auto-generate fuzzy membership functions
    damage.automf(3, names=['low', 'medium', 'high'])
    durability.automf(3, names=['low', 'medium', 'high'])
    crowd_control.automf(3, names=['low', 'medium', 'high'])
    mobility.automf(3, names=['low', 'medium', 'high'])
    difficulty.automf(3, names=['easy', 'medium', 'hard'])
    
    # Define membership functions for output
    suitability['low'] = fuzz.trimf(suitability.universe, [0, 0, 50])
    suitability['medium'] = fuzz.trimf(suitability.universe, [25, 50, 75])
    suitability['high'] = fuzz.trimf(suitability.universe, [50, 100, 100])
    
    # Define fuzzy rules for tank role
    rule1 = ctrl.Rule(durability['high'] & crowd_control['high'], suitability['high'])
    rule2 = ctrl.Rule(durability['high'] & crowd_control['medium'], suitability['medium'])
    rule3 = ctrl.Rule(durability['medium'] & crowd_control['high'], suitability['medium'])
    rule4 = ctrl.Rule(durability['low'] | crowd_control['low'], suitability['low'])
    
    # Define fuzzy rules for fighter role
    rule5 = ctrl.Rule(damage['medium'] & durability['medium'], suitability['medium'])
    rule6 = ctrl.Rule(damage['high'] & durability['medium'], suitability['high'])
    rule7 = ctrl.Rule(damage['medium'] & durability['high'], suitability['high'])
    rule8 = ctrl.Rule(damage['low'] & durability['low'], suitability['low'])
    
    # Define fuzzy rules for assassin role
    rule9 = ctrl.Rule(damage['high'] & mobility['high'], suitability['high'])
    rule10 = ctrl.Rule(damage['high'] & mobility['medium'], suitability['medium'])
    rule11 = ctrl.Rule(damage['medium'] & mobility['high'], suitability['medium'])
    rule12 = ctrl.Rule(damage['low'] | mobility['low'], suitability['low'])
    
    # Define fuzzy rules for mage role
    rule13 = ctrl.Rule(damage['high'] & crowd_control['medium'], suitability['high'])
    rule14 = ctrl.Rule(damage['high'] & crowd_control['low'], suitability['medium'])
    rule15 = ctrl.Rule(damage['medium'] & crowd_control['high'], suitability['high'])
    rule16 = ctrl.Rule(damage['low'] & crowd_control['low'], suitability['low'])
    
    # Define fuzzy rules for marksman role
    rule17 = ctrl.Rule(damage['high'] & durability['low'], suitability['high'])
    rule18 = ctrl.Rule(damage['medium'] & mobility['medium'], suitability['medium'])
    rule19 = ctrl.Rule(damage['high'] & mobility['high'], suitability['high'])
    rule20 = ctrl.Rule(damage['low'], suitability['low'])
    
    # Define fuzzy rules for support role
    rule21 = ctrl.Rule(crowd_control['high'] & durability['medium'], suitability['high'])
    rule22 = ctrl.Rule(crowd_control['medium'] & mobility['high'], suitability['high'])
    rule23 = ctrl.Rule(crowd_control['medium'] & mobility['medium'], suitability['medium'])
    rule24 = ctrl.Rule(crowd_control['low'] & durability['low'], suitability['low'])
    
    # Define general rules for all roles
    rule25 = ctrl.Rule(difficulty['hard'] & damage['high'], suitability['medium'])
    rule26 = ctrl.Rule(difficulty['easy'] & mobility['high'], suitability['high'])
    rule27 = ctrl.Rule(difficulty['medium'] & durability['medium'] & crowd_control['medium'], suitability['medium'])
    
    # Create control system
    hero_ctrl = ctrl.ControlSystem([
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
        rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
        rule21, rule22, rule23, rule24, rule25, rule26, rule27
    ])
    
    return ctrl.ControlSystemSimulation(hero_ctrl)

def evaluate_hero(hero, preferences):
    """
    Evaluate a hero using fuzzy logic based on user preferences.
    
    Args:
        hero (dict): The hero data.
        preferences (dict): User preferences for hero attributes.
        
    Returns:
        dict: Evaluation results.
    """
    try:
        # Create fuzzy control system
        hero_eval = create_fuzzy_system()
        
        # Set inputs
        hero_eval.input['damage'] = hero["damage"]
        hero_eval.input['durability'] = hero["durability"]
        hero_eval.input['crowd_control'] = hero["crowd_control"]
        hero_eval.input['mobility'] = hero["mobility"]
        hero_eval.input['difficulty'] = hero["difficulty"]
        
        # Compute result
        hero_eval.compute()
        suitability_score = hero_eval.output['suitability']
        
        # Calculate preference match (weighted by user preferences)
        pref_scores = []
        if preferences:
            for attr in ["damage", "durability", "crowd_control", "mobility", "difficulty"]:
                # Calculate match % by taking the difference and normalizing
                attr_match = 100 - (abs(preferences[attr] - hero[attr]) / 10 * 100)
                pref_scores.append(attr_match)
        
        preference_match = sum(pref_scores) / len(pref_scores) if pref_scores else 0
        
        # Calculate final score as weighted average of suitability and preference match
        final_score = 0.6 * suitability_score + 0.4 * preference_match
        
        # Prepare detailed evaluation results
        evaluation = {
            "suitability_score": round(suitability_score, 2),
            "preference_match": round(preference_match, 2),
            "final_score": round(final_score, 2),
            "attributes": {
                "damage": hero["damage"],
                "durability": hero["durability"],
                "crowd_control": hero["crowd_control"],
                "mobility": hero["mobility"],
                "difficulty": hero["difficulty"]
            },
            "strengths": hero["strengths"],
            "weaknesses": hero["weaknesses"]
        }
        
        return evaluation
    
    except Exception as e:
        logging.error(f"Error evaluating hero {hero['name']}: {str(e)}")
        return {
            "error": f"Failed to evaluate hero: {str(e)}",
            "suitability_score": 0,
            "preference_match": 0,
            "final_score": 0
        }

def get_hero_recommendations(heroes, preferences):
    """
    Get hero recommendations based on user preferences.
    
    Args:
        heroes (list): List of heroes to evaluate.
        preferences (dict): User preferences for hero attributes.
        
    Returns:
        list: Sorted list of hero recommendations.
    """
    recommendations = []
    
    for hero in heroes:
        try:
            evaluation = evaluate_hero(hero, preferences)
            recommendations.append({
                "hero": hero,
                "evaluation": evaluation
            })
        except Exception as e:
            logging.error(f"Error getting recommendation for {hero['name']}: {str(e)}")
    
    # Sort recommendations by final score (descending)
    return sorted(recommendations, key=lambda x: x["evaluation"]["final_score"], reverse=True)
