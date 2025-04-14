"""
Database service functions for MLBB Hero Selector.
This module provides functions to interact with the database.
"""
import logging
from sqlalchemy.exc import SQLAlchemyError
from app import db
from models import Hero, HeroStrength, HeroWeakness, UserPreference

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_all_heroes_from_db():
    """
    Get all heroes from database.
    
    Returns:
        list: List of hero dictionaries.
    """
    try:
        heroes = Hero.query.all()
        return [hero.to_dict() for hero in heroes]
    except SQLAlchemyError as e:
        logger.error(f"Database error when getting all heroes: {str(e)}")
        return []

def get_heroes_by_role_from_db(role):
    """
    Get heroes by role from database.
    
    Args:
        role (str): Hero role to filter by.
        
    Returns:
        list: List of hero dictionaries matching the role.
    """
    try:
        heroes = Hero.query.filter_by(role=role).all()
        return [hero.to_dict() for hero in heroes]
    except SQLAlchemyError as e:
        logger.error(f"Database error when getting heroes by role: {str(e)}")
        return []

def get_hero_by_id_from_db(hero_id):
    """
    Get a hero by ID from database.
    
    Args:
        hero_id (int): Hero ID to retrieve.
        
    Returns:
        dict: Hero dictionary or None if not found.
    """
    try:
        hero = Hero.query.get(hero_id)
        return hero.to_dict() if hero else None
    except SQLAlchemyError as e:
        logger.error(f"Database error when getting hero by ID: {str(e)}")
        return None

def get_all_roles_from_db():
    """
    Get all unique roles from database.
    
    Returns:
        list: List of unique role strings.
    """
    try:
        roles = db.session.query(Hero.role).distinct().all()
        return [role[0] for role in roles]
    except SQLAlchemyError as e:
        logger.error(f"Database error when getting all roles: {str(e)}")
        return []

def add_hero_to_db(hero_data):
    """
    Add a new hero to the database.
    
    Args:
        hero_data (dict): Hero data dictionary.
        
    Returns:
        dict: Added hero dictionary or None if failed.
    """
    try:
        # Create new hero
        strengths = hero_data.pop('strengths', [])
        weaknesses = hero_data.pop('weaknesses', [])
        
        new_hero = Hero(**hero_data)
        
        # Add strengths
        for strength in strengths:
            new_hero.strengths.append(HeroStrength(text=strength))
        
        # Add weaknesses
        for weakness in weaknesses:
            new_hero.weaknesses.append(HeroWeakness(text=weakness))
        
        # Add to database
        db.session.add(new_hero)
        db.session.commit()
        
        return new_hero.to_dict()
    
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error when adding hero: {str(e)}")
        return None

def update_hero_in_db(hero_id, hero_data):
    """
    Update an existing hero in the database.
    
    Args:
        hero_id (int): ID of hero to update.
        hero_data (dict): Updated hero data dictionary.
        
    Returns:
        dict: Updated hero dictionary or None if failed.
    """
    try:
        hero = Hero.query.get(hero_id)
        if not hero:
            return None
        
        # Update strengths if provided
        if 'strengths' in hero_data:
            strengths = hero_data.pop('strengths')
            # Clear existing strengths
            HeroStrength.query.filter_by(hero_id=hero_id).delete()
            # Add new strengths
            for strength in strengths:
                hero.strengths.append(HeroStrength(text=strength))
        
        # Update weaknesses if provided
        if 'weaknesses' in hero_data:
            weaknesses = hero_data.pop('weaknesses')
            # Clear existing weaknesses
            HeroWeakness.query.filter_by(hero_id=hero_id).delete()
            # Add new weaknesses
            for weakness in weaknesses:
                hero.weaknesses.append(HeroWeakness(text=weakness))
        
        # Update other attributes
        for key, value in hero_data.items():
            if hasattr(hero, key):
                setattr(hero, key, value)
        
        db.session.commit()
        return hero.to_dict()
    
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error when updating hero: {str(e)}")
        return None

def delete_hero_from_db(hero_id):
    """
    Delete a hero from the database.
    
    Args:
        hero_id (int): ID of hero to delete.
        
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        hero = Hero.query.get(hero_id)
        if not hero:
            return False
        
        db.session.delete(hero)
        db.session.commit()
        return True
    
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error when deleting hero: {str(e)}")
        return False

def save_user_preference(preference_data):
    """
    Save user preference to database.
    
    Args:
        preference_data (dict): User preference data.
        
    Returns:
        dict: Saved preference dictionary or None if failed.
    """
    try:
        new_preference = UserPreference(**preference_data)
        db.session.add(new_preference)
        db.session.commit()
        return new_preference.to_dict()
    
    except SQLAlchemyError as e:
        db.session.rollback()
        logger.error(f"Database error when saving user preference: {str(e)}")
        return None

def get_user_preference(preference_id):
    """
    Get user preference by ID.
    
    Args:
        preference_id (int): Preference ID to retrieve.
        
    Returns:
        dict: Preference dictionary or None if not found.
    """
    try:
        preference = UserPreference.query.get(preference_id)
        return preference.to_dict() if preference else None
    
    except SQLAlchemyError as e:
        logger.error(f"Database error when getting user preference: {str(e)}")
        return None