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
    
    # Performance statistics
    win_rate = db.Column(db.Float, nullable=False, default=50.0)
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
            'damage': self.damage,
            'durability': self.durability,
            'crowd_control': self.crowd_control,
            'mobility': self.mobility,
            'difficulty': self.difficulty,
            'win_rate': self.win_rate,
            'profit_factor': self.profit_factor,
            'max_drawdown': self.max_drawdown,
            'max_consecutive_loss': self.max_consecutive_loss,
            'strengths': [s.text for s in self.strengths],
            'weaknesses': [w.text for w in self.weaknesses],
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
    
    # Attribute preferences
    damage = db.Column(db.Integer, nullable=False, default=5)
    durability = db.Column(db.Integer, nullable=False, default=5)
    crowd_control = db.Column(db.Integer, nullable=False, default=5)
    mobility = db.Column(db.Integer, nullable=False, default=5)
    difficulty = db.Column(db.Integer, nullable=False, default=5)
    
    # Statistic preferences
    win_rate_importance = db.Column(db.Integer, nullable=False, default=5)
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
            'damage': self.damage,
            'durability': self.durability,
            'crowd_control': self.crowd_control,
            'mobility': self.mobility,
            'difficulty': self.difficulty,
            'win_rate_importance': self.win_rate_importance,
            'profit_factor_importance': self.profit_factor_importance,
            'max_drawdown_importance': self.max_drawdown_importance,
            'max_consecutive_loss_importance': self.max_consecutive_loss_importance,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }