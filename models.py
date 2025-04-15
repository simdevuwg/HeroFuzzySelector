"""
Database models for MLBB Hero Selector.
"""
from datetime import datetime
from database import db

class Hero(db.Model):
    """Hero model for storing hero data."""
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    role = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    
    # Basic attributes
    damage = db.Column(db.Integer, nullable=False, default=5)
    durability = db.Column(db.Integer, nullable=False, default=5)
    crowd_control = db.Column(db.Integer, nullable=False, default=5)
    mobility = db.Column(db.Integer, nullable=False, default=5)
    difficulty = db.Column(db.Integer, nullable=False, default=5)
    
    # Additional attributes
    defense_overall = db.Column(db.Integer, nullable=False, default=5)
    offense_overall = db.Column(db.Integer, nullable=False, default=5)
    skill_effect_overall = db.Column(db.Integer, nullable=False, default=5)
    difficulty_overall = db.Column(db.Integer, nullable=False, default=5)
    movement_spd = db.Column(db.Integer, nullable=False, default=5)
    magic_defense = db.Column(db.Integer, nullable=False, default=5)
    mana = db.Column(db.Integer, nullable=False, default=5)
    hp_regen = db.Column(db.Integer, nullable=False, default=5)
    physical_atk = db.Column(db.Integer, nullable=False, default=5)
    physical_defense = db.Column(db.Integer, nullable=False, default=5)
    hp = db.Column(db.Integer, nullable=False, default=5)
    attack_speed = db.Column(db.Integer, nullable=False, default=5)
    mana_regen = db.Column(db.Integer, nullable=False, default=5)
    
    # Performance statistics
    win_rate = db.Column(db.Float, nullable=False, default=50.0)
    pick_rate = db.Column(db.Float, nullable=False, default=5.0)
    ban_rate = db.Column(db.Float, nullable=False, default=1.0)
    profit_factor = db.Column(db.Float, nullable=False, default=1.0)
    max_drawdown = db.Column(db.Float, nullable=False, default=20.0)
    max_consecutive_loss = db.Column(db.Integer, nullable=False, default=3)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    strengths = db.relationship("HeroStrength", back_populates="hero", cascade="all, delete-orphan")
    weaknesses = db.relationship("HeroWeakness", back_populates="hero", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Hero(name='{self.name}', role='{self.role}')>"
    
    def to_dict(self):
        """Convert hero object to dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'description': self.description,
            
            # Basic attributes
            'damage': self.damage,
            'durability': self.durability,
            'crowd_control': self.crowd_control,
            'mobility': self.mobility,
            'difficulty': self.difficulty,
            
            # Additional attributes
            'defense_overall': self.defense_overall,
            'offense_overall': self.offense_overall,
            'skill_effect_overall': self.skill_effect_overall,
            'difficulty_overall': self.difficulty_overall,
            'movement_spd': self.movement_spd,
            'magic_defense': self.magic_defense,
            'mana': self.mana,
            'hp_regen': self.hp_regen,
            'physical_atk': self.physical_atk,
            'physical_defense': self.physical_defense,
            'hp': self.hp,
            'attack_speed': self.attack_speed,
            'mana_regen': self.mana_regen,
            
            # Performance statistics
            'win_rate': self.win_rate,
            'pick_rate': self.pick_rate,
            'ban_rate': self.ban_rate,
            'profit_factor': self.profit_factor,
            'max_drawdown': self.max_drawdown,
            'max_consecutive_loss': self.max_consecutive_loss,
            
            # Relationships
            'strengths': [s.text for s in self.strengths],
            'weaknesses': [w.text for w in self.weaknesses],
            
            # Metadata
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }


class HeroStrength(db.Model):
    """Model for storing hero strengths."""
    __tablename__ = 'hero_strengths'
    
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    
    # Relationship
    hero = db.relationship("Hero", back_populates="strengths")
    
    def __repr__(self):
        return f"<HeroStrength(hero_id={self.hero_id}, text='{self.text}')>"


class HeroWeakness(db.Model):
    """Model for storing hero weaknesses."""
    __tablename__ = 'hero_weaknesses'
    
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    
    # Relationship
    hero = db.relationship("Hero", back_populates="weaknesses")
    
    def __repr__(self):
        return f"<HeroWeakness(hero_id={self.hero_id}, text='{self.text}')>"


class UserPreference(db.Model):
    """Model for storing user preferences."""
    __tablename__ = 'user_preferences'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(100), nullable=True)  # Optional, for future user authentication
    role = db.Column(db.String(50), nullable=True)
    
    # Basic attribute preferences
    damage = db.Column(db.Integer, nullable=False, default=5)
    durability = db.Column(db.Integer, nullable=False, default=5)
    crowd_control = db.Column(db.Integer, nullable=False, default=5)
    mobility = db.Column(db.Integer, nullable=False, default=5)
    difficulty = db.Column(db.Integer, nullable=False, default=5)
    
    # Additional attribute preferences
    defense_overall_importance = db.Column(db.Integer, nullable=False, default=5)
    offense_overall_importance = db.Column(db.Integer, nullable=False, default=5)
    skill_effect_overall_importance = db.Column(db.Integer, nullable=False, default=5)
    difficulty_overall_importance = db.Column(db.Integer, nullable=False, default=5)
    movement_spd_importance = db.Column(db.Integer, nullable=False, default=5)
    magic_defense_importance = db.Column(db.Integer, nullable=False, default=5)
    mana_importance = db.Column(db.Integer, nullable=False, default=5)
    hp_regen_importance = db.Column(db.Integer, nullable=False, default=5)
    physical_atk_importance = db.Column(db.Integer, nullable=False, default=5)
    physical_defense_importance = db.Column(db.Integer, nullable=False, default=5)
    hp_importance = db.Column(db.Integer, nullable=False, default=5)
    attack_speed_importance = db.Column(db.Integer, nullable=False, default=5)
    mana_regen_importance = db.Column(db.Integer, nullable=False, default=5)
    
    # Statistic preferences
    win_rate_importance = db.Column(db.Integer, nullable=False, default=5)
    pick_rate_importance = db.Column(db.Integer, nullable=False, default=5)
    ban_rate_importance = db.Column(db.Integer, nullable=False, default=5)
    profit_factor_importance = db.Column(db.Integer, nullable=False, default=5)
    max_drawdown_importance = db.Column(db.Integer, nullable=False, default=5)
    max_consecutive_loss_importance = db.Column(db.Integer, nullable=False, default=5)
    
    # Metadata
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<UserPreference(id={self.id}, role='{self.role}')>"
    
    def to_dict(self):
        """Convert preference object to dictionary."""
        return {
            'id': self.id,
            'role': self.role,
            
            # Basic attribute preferences
            'damage': self.damage,
            'durability': self.durability,
            'crowd_control': self.crowd_control,
            'mobility': self.mobility,
            'difficulty': self.difficulty,
            
            # Additional attribute preferences
            'defense_overall_importance': self.defense_overall_importance,
            'offense_overall_importance': self.offense_overall_importance,
            'skill_effect_overall_importance': self.skill_effect_overall_importance,
            'difficulty_overall_importance': self.difficulty_overall_importance,
            'movement_spd_importance': self.movement_spd_importance,
            'magic_defense_importance': self.magic_defense_importance,
            'mana_importance': self.mana_importance,
            'hp_regen_importance': self.hp_regen_importance,
            'physical_atk_importance': self.physical_atk_importance,
            'physical_defense_importance': self.physical_defense_importance,
            'hp_importance': self.hp_importance,
            'attack_speed_importance': self.attack_speed_importance,
            'mana_regen_importance': self.mana_regen_importance,
            
            # Statistic preferences
            'win_rate_importance': self.win_rate_importance,
            'pick_rate_importance': self.pick_rate_importance,
            'ban_rate_importance': self.ban_rate_importance,
            'profit_factor_importance': self.profit_factor_importance,
            'max_drawdown_importance': self.max_drawdown_importance,
            'max_consecutive_loss_importance': self.max_consecutive_loss_importance,
            
            # Metadata
            'created_at': self.created_at.isoformat() if self.created_at else None
        }