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
    
    # Input variables (basic attributes)
    damage = ctrl.Antecedent(np.arange(0, 11, 1), 'damage')
    durability = ctrl.Antecedent(np.arange(0, 11, 1), 'durability')
    crowd_control = ctrl.Antecedent(np.arange(0, 11, 1), 'crowd_control')
    mobility = ctrl.Antecedent(np.arange(0, 11, 1), 'mobility')
    difficulty = ctrl.Antecedent(np.arange(0, 11, 1), 'difficulty')
    
    # Input variables (additional attributes)
    defense_overall = ctrl.Antecedent(np.arange(0, 11, 1), 'defense_overall')
    offense_overall = ctrl.Antecedent(np.arange(0, 11, 1), 'offense_overall')
    skill_effect_overall = ctrl.Antecedent(np.arange(0, 11, 1), 'skill_effect_overall')
    difficulty_overall = ctrl.Antecedent(np.arange(0, 11, 1), 'difficulty_overall')
    movement_spd = ctrl.Antecedent(np.arange(0, 11, 1), 'movement_spd')
    magic_defense = ctrl.Antecedent(np.arange(0, 11, 1), 'magic_defense')
    physical_atk = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_atk')
    physical_defense = ctrl.Antecedent(np.arange(0, 11, 1), 'physical_defense')
    
    # Input variables (statistical attributes)
    win_rate = ctrl.Antecedent(np.arange(40, 61, 1), 'win_rate')
    pick_rate = ctrl.Antecedent(np.arange(0, 21, 1), 'pick_rate')
    ban_rate = ctrl.Antecedent(np.arange(0, 21, 1), 'ban_rate')
    profit_factor = ctrl.Antecedent(np.arange(0.5, 2.1, 0.1), 'profit_factor')
    max_drawdown = ctrl.Antecedent(np.arange(0, 51, 1), 'max_drawdown')
    max_consecutive_loss = ctrl.Antecedent(np.arange(0, 11, 1), 'max_consecutive_loss')
    
    # Output variable
    suitability = ctrl.Consequent(np.arange(0, 101, 1), 'suitability')
    
    # Auto-generate fuzzy membership functions for basic attributes
    damage.automf(3, names=['low', 'medium', 'high'])
    durability.automf(3, names=['low', 'medium', 'high'])
    crowd_control.automf(3, names=['low', 'medium', 'high'])
    mobility.automf(3, names=['low', 'medium', 'high'])
    difficulty.automf(3, names=['easy', 'medium', 'hard'])
    
    # Auto-generate fuzzy membership functions for additional attributes
    defense_overall.automf(3, names=['low', 'medium', 'high'])
    offense_overall.automf(3, names=['low', 'medium', 'high'])
    skill_effect_overall.automf(3, names=['weak', 'medium', 'strong'])
    difficulty_overall.automf(3, names=['easy', 'medium', 'hard'])
    movement_spd.automf(3, names=['slow', 'medium', 'fast'])
    magic_defense.automf(3, names=['low', 'medium', 'high'])
    physical_atk.automf(3, names=['low', 'medium', 'high'])
    physical_defense.automf(3, names=['low', 'medium', 'high'])
    
    # Define membership functions for statistical attributes
    win_rate['low'] = fuzz.trimf(win_rate.universe, [40, 45, 50])
    win_rate['medium'] = fuzz.trimf(win_rate.universe, [45, 50, 55])
    win_rate['high'] = fuzz.trimf(win_rate.universe, [50, 55, 60])
    
    profit_factor['poor'] = fuzz.trimf(profit_factor.universe, [0.5, 0.7, 0.9])
    profit_factor['average'] = fuzz.trimf(profit_factor.universe, [0.8, 1.0, 1.2])
    profit_factor['good'] = fuzz.trimf(profit_factor.universe, [1.1, 1.5, 2.0])
    
    max_drawdown['small'] = fuzz.trimf(max_drawdown.universe, [0, 15, 25])
    max_drawdown['medium'] = fuzz.trimf(max_drawdown.universe, [20, 30, 40])
    max_drawdown['large'] = fuzz.trimf(max_drawdown.universe, [35, 45, 50])
    
    max_consecutive_loss['few'] = fuzz.trimf(max_consecutive_loss.universe, [0, 2, 4])
    max_consecutive_loss['moderate'] = fuzz.trimf(max_consecutive_loss.universe, [3, 5, 7])
    max_consecutive_loss['many'] = fuzz.trimf(max_consecutive_loss.universe, [6, 8, 10])
    
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
    
    # Define rules for additional attributes
    rule28 = ctrl.Rule(defense_overall['high'] & physical_defense['high'], suitability['high'])
    rule29 = ctrl.Rule(offense_overall['high'] & physical_atk['high'], suitability['high'])
    rule30 = ctrl.Rule(skill_effect_overall['strong'], suitability['high'])
    rule31 = ctrl.Rule(movement_spd['fast'] & mobility['high'], suitability['high'])
    rule32 = ctrl.Rule(magic_defense['high'] & physical_defense['high'], suitability['high'])
    rule33 = ctrl.Rule(defense_overall['low'] & physical_defense['low'], suitability['low'])
    rule34 = ctrl.Rule(offense_overall['low'] & physical_atk['low'], suitability['low'])
    rule35 = ctrl.Rule(movement_spd['slow'] & mobility['low'], suitability['low'])
    
    # Define rules for statistical factors
    rule36 = ctrl.Rule(win_rate['high'] & profit_factor['good'], suitability['high'])
    rule37 = ctrl.Rule(win_rate['high'] & max_drawdown['small'], suitability['high'])
    rule38 = ctrl.Rule(win_rate['medium'] & profit_factor['average'], suitability['medium'])
    rule39 = ctrl.Rule(win_rate['low'] & max_drawdown['large'], suitability['low'])
    rule40 = ctrl.Rule(profit_factor['good'] & max_consecutive_loss['few'], suitability['high'])
    rule41 = ctrl.Rule(profit_factor['poor'] & max_consecutive_loss['many'], suitability['low'])
    rule42 = ctrl.Rule(max_drawdown['small'] & max_consecutive_loss['few'], suitability['high'])
    rule43 = ctrl.Rule(max_drawdown['large'] & max_consecutive_loss['many'], suitability['low'])
    
    # Create control system
    hero_ctrl = ctrl.ControlSystem([
        rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9, rule10,
        rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20,
        rule21, rule22, rule23, rule24, rule25, rule26, rule27, rule28, rule29, rule30,
        rule31, rule32, rule33, rule34, rule35
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
        
        # Set inputs for basic attributes
        hero_eval.input['damage'] = hero["damage"]
        hero_eval.input['durability'] = hero["durability"]
        hero_eval.input['crowd_control'] = hero["crowd_control"]
        hero_eval.input['mobility'] = hero["mobility"]
        hero_eval.input['difficulty'] = hero["difficulty"]
        
        # Set inputs for statistical attributes
        hero_eval.input['win_rate'] = hero["win_rate"]
        hero_eval.input['profit_factor'] = hero["profit_factor"]
        hero_eval.input['max_drawdown'] = hero["max_drawdown"]
        hero_eval.input['max_consecutive_loss'] = hero["max_consecutive_loss"]
        
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
            "statistics": {
                "win_rate": hero["win_rate"],
                "profit_factor": hero["profit_factor"],
                "max_drawdown": hero["max_drawdown"],
                "max_consecutive_loss": hero["max_consecutive_loss"]
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
