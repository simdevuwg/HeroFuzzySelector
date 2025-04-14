"""
Database models for MLBB Hero Selector.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Hero(Base):
    """Hero model for storing hero data."""
    __tablename__ = 'heroes'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)
    role = Column(String(50), nullable=False)
    description = Column(Text, nullable=True)
    
    # Basic attributes
    damage = Column(Integer, nullable=False, default=5)
    durability = Column(Integer, nullable=False, default=5)
    crowd_control = Column(Integer, nullable=False, default=5)
    mobility = Column(Integer, nullable=False, default=5)
    difficulty = Column(Integer, nullable=False, default=5)
    
    # Performance statistics
    win_rate = Column(Float, nullable=False, default=50.0)
    profit_factor = Column(Float, nullable=False, default=1.0)
    max_drawdown = Column(Float, nullable=False, default=20.0)
    max_consecutive_loss = Column(Integer, nullable=False, default=3)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    strengths = relationship("HeroStrength", back_populates="hero", cascade="all, delete-orphan")
    weaknesses = relationship("HeroWeakness", back_populates="hero", cascade="all, delete-orphan")
    
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


class HeroStrength(Base):
    """Model for storing hero strengths."""
    __tablename__ = 'hero_strengths'
    
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    text = Column(Text, nullable=False)
    
    # Relationship
    hero = relationship("Hero", back_populates="strengths")
    
    def __repr__(self):
        return f"<HeroStrength(hero_id={self.hero_id}, text='{self.text}')>"


class HeroWeakness(Base):
    """Model for storing hero weaknesses."""
    __tablename__ = 'hero_weaknesses'
    
    id = Column(Integer, primary_key=True)
    hero_id = Column(Integer, ForeignKey('heroes.id', ondelete='CASCADE'), nullable=False)
    text = Column(Text, nullable=False)
    
    # Relationship
    hero = relationship("Hero", back_populates="weaknesses")
    
    def __repr__(self):
        return f"<HeroWeakness(hero_id={self.hero_id}, text='{self.text}')>"


class UserPreference(Base):
    """Model for storing user preferences."""
    __tablename__ = 'user_preferences'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(String(100), nullable=True)  # Optional, for future user authentication
    role = Column(String(50), nullable=True)
    
    # Attribute preferences
    damage = Column(Integer, nullable=False, default=5)
    durability = Column(Integer, nullable=False, default=5)
    crowd_control = Column(Integer, nullable=False, default=5)
    mobility = Column(Integer, nullable=False, default=5)
    difficulty = Column(Integer, nullable=False, default=5)
    
    # Statistic preferences
    win_rate_importance = Column(Integer, nullable=False, default=5)
    profit_factor_importance = Column(Integer, nullable=False, default=5)
    max_drawdown_importance = Column(Integer, nullable=False, default=5)
    max_consecutive_loss_importance = Column(Integer, nullable=False, default=5)
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    
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