"""
This module contains the hero data for Mobile Legends Bang Bang.
"""

# Define heroes with their attributes and roles
HEROES = [
    # Tanks
    {
        "id": "1",
        "name": "Tigreal",
        "role": "Tank",
        "damage": 3,
        "durability": 8,
        "crowd_control": 9,
        "mobility": 4,
        "difficulty": 2,
        "win_rate": 52.3,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 25,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses
        "strengths": ["Excellent crowd control", "High durability", "Good initiator"],
        "weaknesses": ["Low damage output", "Vulnerable to CC", "Limited mobility"],
        "description": "A reliable tank with strong crowd control abilities and initiating potential."
    },
    {
        "id": "2",
        "name": "Minotaur",
        "role": "Tank",
        "damage": 4,
        "durability": 9,
        "crowd_control": 8,
        "mobility": 3,
        "difficulty": 4,
        "win_rate": 49.7,  # Win rate percentage
        "profit_factor": 1.1,  # Profit factor (win value / loss value)
        "max_drawdown": 30,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["High durability", "AoE crowd control", "Team healing"],
        "weaknesses": ["Rage-dependent ultimate", "Poor mobility", "Weak early game"],
        "description": "A durable tank with potent area crowd control when enraged."
    },
    {
        "id": "3",
        "name": "Johnson",
        "role": "Tank",
        "damage": 5,
        "durability": 9,
        "crowd_control": 7,
        "mobility": 8,
        "difficulty": 7,
        "win_rate": 57.6,  # Win rate percentage
        "profit_factor": 1.4,  # Profit factor (win value / loss value)
        "max_drawdown": 19,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["Unique transport ultimate", "Good durability", "Surprise initiations"],
        "weaknesses": ["Skill-shot dependent", "Long cooldowns", "Predictable patterns"],
        "description": "A tank who transforms into a car, providing team transport and surprise initiations."
    },
    {
        "id": "4",
        "name": "Khufra",
        "role": "Tank",
        "damage": 5,
        "durability": 8,
        "crowd_control": 9,
        "mobility": 6,
        "difficulty": 6,
        "win_rate": 57.7,  # Win rate percentage
        "profit_factor": 1.3,  # Profit factor (win value / loss value)
        "max_drawdown": 15,  # Maximum drawdown percentage
        "max_consecutive_loss": 6,  # Maximum consecutive losses,
        "strengths": ["Counter to dash skills", "Multiple CC abilities", "Good engage"],
        "weaknesses": ["Requires good positioning", "Skill-dependent", "Needs follow-up"],
        "description": "An aggressive tank who excels at locking down mobile enemies."
    },
    {
        "id": "5",
        "name": "Atlas",
        "role": "Tank",
        "damage": 4,
        "durability": 8,
        "crowd_control": 10,
        "mobility": 5,
        "difficulty": 8,
        "win_rate": 46.8,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 24,  # Maximum drawdown percentage
        "max_consecutive_loss": 5,  # Maximum consecutive losses,
        "strengths": ["Game-changing ultimate", "Multiple CC skills", "Good team fight presence"],
        "weaknesses": ["Ultimate can be difficult to land", "Dependent on team follow-up", "Limited damage"],
        "description": "A deep sea tank with powerful area crowd control abilities."
    },
    
    # Fighters
    {
        "id": "6",
        "name": "Chou",
        "role": "Fighter",
        "damage": 7,
        "durability": 6,
        "crowd_control": 7,
        "mobility": 8,
        "difficulty": 9,
        "win_rate": 49.0,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 29,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["Versatile build paths", "Strong CC", "High mobility"],
        "weaknesses": ["Skill-dependent", "Needs precise timing", "Falls off late game"],
        "description": "A versatile fighter with high mobility and crowd control potential."
    },
    {
        "id": "7",
        "name": "X.Borg",
        "role": "Fighter",
        "damage": 8,
        "durability": 7,
        "crowd_control": 5,
        "mobility": 6,
        "difficulty": 5,
        "win_rate": 49.0,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 23,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["Sustained AoE damage", "Armor mechanic", "Good team fight presence"],
        "weaknesses": ["Vulnerable when armor breaks", "Ultimate cooldown dependent", "Poor against burst"],
        "description": "A fighter with unique armor mechanics and strong area damage."
    },
    {
        "id": "8",
        "name": "Badang",
        "role": "Fighter",
        "damage": 7,
        "durability": 6,
        "crowd_control": 8,
        "mobility": 5,
        "difficulty": 6,
        "win_rate": 55.3,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 20,  # Maximum drawdown percentage
        "max_consecutive_loss": 6,  # Maximum consecutive losses,
        "strengths": ["Wall stun combo", "Strong ultimate", "Good burst potential"],
        "weaknesses": ["Combo dependent", "Limited mobility", "Vulnerable to CC"],
        "description": "A fighter who excels at pinning enemies against walls for heavy damage."
    },
    {
        "id": "9",
        "name": "Paquito",
        "role": "Fighter",
        "damage": 9,
        "durability": 6,
        "crowd_control": 6,
        "mobility": 7,
        "difficulty": 8,
        "win_rate": 49.7,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 21,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["High burst damage", "Enhanced skills mechanic", "Good mobility"],
        "weaknesses": ["Combo dependent", "Skill-intensive", "Falls off late game"],
        "description": "A boxer fighter with combo skills and high burst damage potential."
    },
    {
        "id": "10",
        "name": "Yu Zhong",
        "role": "Fighter",
        "damage": 7,
        "durability": 8,
        "crowd_control": 6,
        "mobility": 6,
        "difficulty": 7,
        "win_rate": 56.3,  # Win rate percentage
        "profit_factor": 1.3,  # Profit factor (win value / loss value)
        "max_drawdown": 31,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["Sustain through lifesteal", "Good AoE damage", "Strong ultimate"],
        "weaknesses": ["Vulnerable to anti-heal", "Skill cooldown dependent", "Can be kited"],
        "description": "A sustain fighter who transforms into a dragon for enhanced abilities."
    },
    
    # Assassins
    {
        "id": "11",
        "name": "Lancelot",
        "role": "Assassin",
        "damage": 9,
        "durability": 3,
        "crowd_control": 1,
        "mobility": 10,
        "difficulty": 10,
        "win_rate": 46.2,  # Win rate percentage
        "profit_factor": 1.1,  # Profit factor (win value / loss value)
        "max_drawdown": 31,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["High burst damage", "Excellent mobility", "Immunity frames"],
        "weaknesses": ["Very skill dependent", "Fragile", "Weak against tanky teams"],
        "description": "A highly mobile assassin with fast burst damage and immunity frames."
    },
    {
        "id": "12",
        "name": "Gusion",
        "role": "Assassin",
        "damage": 10,
        "durability": 2,
        "crowd_control": 1,
        "mobility": 8,
        "difficulty": 10,
        "win_rate": 53.8,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 19,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["Extremely high burst", "Dagger reset mechanic", "Good mobility"],
        "weaknesses": ["Complex combos", "Very skill dependent", "Weak late game"],
        "description": "A dagger-wielding assassin with complex combos and high burst potential."
    },
    {
        "id": "13",
        "name": "Hayabusa",
        "role": "Assassin",
        "damage": 8,
        "durability": 3,
        "crowd_control": 1,
        "mobility": 9,
        "difficulty": 9,
        "win_rate": 50.9,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 21,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["Split push potential", "Target isolation", "Untargetable ultimate"],
        "weaknesses": ["Single target focus", "Shadow dependent", "Countered by grouping"],
        "description": "A ninja assassin who excels at isolating and eliminating single targets."
    },
    {
        "id": "14",
        "name": "Ling",
        "role": "Assassin",
        "damage": 9,
        "durability": 2,
        "crowd_control": 3,
        "mobility": 10,
        "difficulty": 9,
        "win_rate": 50.0,  # Win rate percentage
        "profit_factor": 1.0,  # Profit factor (win value / loss value)
        "max_drawdown": 23,  # Maximum drawdown percentage
        "max_consecutive_loss": 6,  # Maximum consecutive losses,
        "strengths": ["Wall-jumping mobility", "High burst", "Evasive potential"],
        "weaknesses": ["Energy dependent", "Fragile", "Weak early game"],
        "description": "An assassin who can walk on walls and deliver devastating critical strikes."
    },
    {
        "id": "15",
        "name": "Fanny",
        "role": "Assassin",
        "damage": 8,
        "durability": 4,
        "crowd_control": 2,
        "mobility": 10,
        "difficulty": 10,
        "win_rate": 48.6,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 17,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Unique cable mobility", "High damage potential", "Map control"],
        "weaknesses": ["Extremely skill dependent", "Energy hungry", "Counter-picked easily"],
        "description": "A cable-swinging assassin with unique mobility and high skill ceiling."
    },
    
    # Mages
    {
        "id": "16",
        "name": "Lunox",
        "role": "Mage",
        "damage": 9,
        "durability": 3,
        "crowd_control": 4,
        "mobility": 6,
        "difficulty": 7,
        "win_rate": 46.2,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 28,  # Maximum drawdown percentage
        "max_consecutive_loss": 5,  # Maximum consecutive losses,
        "strengths": ["Chaos/Order mechanic", "Burst and sustained options", "Immunity skill"],
        "weaknesses": ["Position dependent", "Mana hungry", "Limited CC"],
        "description": "A mage with dual Chaos and Order powers offering different playstyles."
    },
    {
        "id": "17",
        "name": "Kagura",
        "role": "Mage",
        "damage": 9,
        "durability": 3,
        "crowd_control": 7,
        "mobility": 7,
        "difficulty": 10,
        "win_rate": 53.2,  # Win rate percentage
        "profit_factor": 1.3,  # Profit factor (win value / loss value)
        "max_drawdown": 28,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["Umbrella mechanic", "High skill ceiling", "Purify effect"],
        "weaknesses": ["Complex combos", "Position dependent", "Requires practice"],
        "description": "A complex mage with an umbrella that offers versatile combos and effects."
    },
    {
        "id": "18",
        "name": "Pharsa",
        "role": "Mage",
        "damage": 10,
        "durability": 2,
        "crowd_control": 5,
        "mobility": 5,
        "difficulty": 6,
        "win_rate": 57.9,  # Win rate percentage
        "profit_factor": 1.4,  # Profit factor (win value / loss value)
        "max_drawdown": 20,  # Maximum drawdown percentage
        "max_consecutive_loss": 4,  # Maximum consecutive losses,
        "strengths": ["Long-range damage", "Bird form mobility", "AoE damage"],
        "weaknesses": ["Channeling ultimate", "Fragile", "Vulnerable when ulting"],
        "description": "A mage who can transform into a bird and deal massive long-range damage."
    },
    {
        "id": "19",
        "name": "Valir",
        "role": "Mage",
        "damage": 8,
        "durability": 4,
        "crowd_control": 8,
        "mobility": 5,
        "difficulty": 5,
        "win_rate": 55.6,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 28,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Strong CC", "Knockback effects", "Good zoning"],
        "weaknesses": ["Skill-shot dependent", "Limited mobility", "Falls off late"],
        "description": "A fire mage with strong crowd control and zoning capabilities."
    },
    {
        "id": "20",
        "name": "Cecilion",
        "role": "Mage",
        "damage": 10,
        "durability": 2,
        "crowd_control": 5,
        "mobility": 3,
        "difficulty": 6,
        "win_rate": 53.1,  # Win rate percentage
        "profit_factor": 1.0,  # Profit factor (win value / loss value)
        "max_drawdown": 17,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Scaling damage", "Long range", "Infinite scaling mechanic"],
        "weaknesses": ["Mana hungry early", "Limited mobility", "Weak early game"],
        "description": "A vampire mage with stacking damage mechanic and powerful late game."
    },
    
    # Marksmen
    {
        "id": "21",
        "name": "Granger",
        "role": "Marksman",
        "damage": 9,
        "durability": 3,
        "crowd_control": 1,
        "mobility": 6,
        "difficulty": 6,
        "win_rate": 55.6,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 33,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["High burst damage", "Good early game", "Mobility from skills"],
        "weaknesses": ["Reload mechanic", "Limited attack speed scaling", "Skill dependent"],
        "description": "A marksman with high physical burst damage and a musical theme."
    },
    {
        "id": "22",
        "name": "Claude",
        "role": "Marksman",
        "damage": 8,
        "durability": 2,
        "crowd_control": 1,
        "mobility": 8,
        "difficulty": 7,
        "win_rate": 56.8,  # Win rate percentage
        "profit_factor": 1.3,  # Profit factor (win value / loss value)
        "max_drawdown": 26,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["AoE basic attacks", "High mobility", "Stealth option"],
        "weaknesses": ["Item dependent", "Fragile", "Weak early game"],
        "description": "A nimble marksman who uses a monkey companion and deals AoE damage."
    },
    {
        "id": "23",
        "name": "Wanwan",
        "role": "Marksman",
        "damage": 9,
        "durability": 2,
        "crowd_control": 4,
        "mobility": 9,
        "difficulty": 8,
        "win_rate": 45.4,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 26,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Weakness point mechanic", "Immunity ultimate", "High mobility"],
        "weaknesses": ["Weak early game", "Requires hitting weak points", "Fragile"],
        "description": "An agile marksman who targets enemy weaknesses and has an immunity-granting ultimate."
    },
    {
        "id": "24",
        "name": "Brody",
        "role": "Marksman",
        "damage": 10,
        "durability": 4,
        "crowd_control": 3,
        "mobility": 5,
        "difficulty": 5,
        "win_rate": 50.4,  # Win rate percentage
        "profit_factor": 1.4,  # Profit factor (win value / loss value)
        "max_drawdown": 24,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["High damage per shot", "Stack mechanic", "Good early game"],
        "weaknesses": ["Slow attack speed", "Limited mobility", "Skill-shot dependent"],
        "description": "A marksman with high damage per shot but slower attack speed."
    },
    {
        "id": "25",
        "name": "Beatrix",
        "role": "Marksman",
        "damage": 10,
        "durability": 3,
        "crowd_control": 2,
        "mobility": 5,
        "difficulty": 9,
        "win_rate": 46.4,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 27,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["Multiple weapon options", "Versatile playstyle", "Strong early game"],
        "weaknesses": ["Complex weapon switching", "Limited late game", "Requires practice"],
        "description": "A marksman who can switch between four different weapons with unique effects."
    },
    
    # Supports
    {
        "id": "26",
        "name": "Angela",
        "role": "Support",
        "damage": 5,
        "durability": 2,
        "crowd_control": 6,
        "mobility": 4,
        "difficulty": 5,
        "win_rate": 49.9,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 28,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Ally attachment ultimate", "Global presence", "Good healing"],
        "weaknesses": ["Fragile", "Dependent on allies", "Limited solo potential"],
        "description": "A support who can attach to allies and provide healing and shields."
    },
    {
        "id": "27",
        "name": "Estes",
        "role": "Support",
        "damage": 4,
        "durability": 3,
        "crowd_control": 3,
        "mobility": 3,
        "difficulty": 2,
        "win_rate": 51.3,  # Win rate percentage
        "profit_factor": 1.4,  # Profit factor (win value / loss value)
        "max_drawdown": 26,  # Maximum drawdown percentage
        "max_consecutive_loss": 2,  # Maximum consecutive losses,
        "strengths": ["Best healer", "Team sustain", "Easy to use"],
        "weaknesses": ["Countered by anti-heal", "No hard CC", "Limited damage"],
        "description": "The premier healing support with strong team sustain capabilities."
    },
    {
        "id": "28",
        "name": "Diggie",
        "role": "Support",
        "damage": 5,
        "durability": 3,
        "crowd_control": 7,
        "mobility": 4,
        "difficulty": 6,
        "win_rate": 52.9,  # Win rate percentage
        "profit_factor": 1.3,  # Profit factor (win value / loss value)
        "max_drawdown": 34,  # Maximum drawdown percentage
        "max_consecutive_loss": 6,  # Maximum consecutive losses,
        "strengths": ["CC immunity ultimate", "Anti-dive", "CC options"],
        "weaknesses": ["Team dependent", "Limited damage", "Situational pick"],
        "description": "A support who counters crowd control with his ultimate and provides utility."
    },
    {
        "id": "29",
        "name": "Mathilda",
        "role": "Support",
        "damage": 6,
        "durability": 4,
        "crowd_control": 6,
        "mobility": 9,
        "difficulty": 7,
        "win_rate": 46.4,  # Win rate percentage
        "profit_factor": 1.2,  # Profit factor (win value / loss value)
        "max_drawdown": 24,  # Maximum drawdown percentage
        "max_consecutive_loss": 3,  # Maximum consecutive losses,
        "strengths": ["High mobility", "Shield mechanic", "Transport ultimate"],
        "weaknesses": ["Needs coordination", "Skill-shot dependent", "Limited healing"],
        "description": "A fairy support with high mobility and ally transport capabilities."
    },
    {
        "id": "30",
        "name": "Rafaela",
        "role": "Support",
        "damage": 5,
        "durability": 3,
        "crowd_control": 5,
        "mobility": 7,
        "difficulty": 3,
        "win_rate": 57.6,  # Win rate percentage
        "profit_factor": 0.9,  # Profit factor (win value / loss value)
        "max_drawdown": 21,  # Maximum drawdown percentage
        "max_consecutive_loss": 5,  # Maximum consecutive losses,
        "strengths": ["Team movement speed", "Healing", "Easy to use"],
        "weaknesses": ["Fragile", "Limited damage", "Outscaled late game"],
        "description": "An angelic support with healing and movement speed boosts for the team."
    }
]

def get_all_heroes():
    """Return all heroes in the database"""
    return HEROES

def get_hero_by_id(hero_id):
    """Return a hero by ID"""
    for hero in HEROES:
        if hero["id"] == hero_id:
            return hero
    return None

def get_heroes_by_role(role):
    """Return all heroes with a specific role"""
    return [hero for hero in HEROES if hero["role"] == role]

def get_all_roles():
    """Return all unique roles"""
    return sorted(list(set(hero["role"] for hero in HEROES)))
