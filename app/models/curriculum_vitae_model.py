from sqlalchemy import Column, Integer, String, Text, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class CurriculumVitae(Base):
    __tablename__ = "curriculum_vitae"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), index=True)
    email = Column(String(100), unique=True, index=True, nullable=False)

    # Personal Info
    phone_number = Column(String(20), nullable=True)
    linkedin_url = Column(String(100), nullable=True)
    github_url = Column(String(100), nullable=True)
    summary = Column(Text, nullable=True)

    # Skills - This could be a separate table if you want to normalize it
    skills = Column(Text, nullable=True)

    # Education
    education = relationship("Education", back_populates="cv")

    # Work Experience
    work_experience = relationship("WorkExperience", back_populates="cv")

    # Projects
    projects = relationship("Project", back_populates="cv")


class Education(Base):
    __tablename__ = "education"

    id = Column(Integer, primary_key=True, index=True)
    institution = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    cv_id = Column(Integer, ForeignKey('curriculum_vitae.id'))

    cv = relationship("CurriculumVitae", back_populates="education")


class WorkExperience(Base):
    __tablename__ = "work_experience"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String(100), nullable=False)
    position = Column(String(100), nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    cv_id = Column(Integer, ForeignKey('curriculum_vitae.id'))

    cv = relationship("CurriculumVitae", back_populates="work_experience")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    cv_id = Column(Integer, ForeignKey('curriculum_vitae.id'))

    cv = relationship("CurriculumVitae", back_populates="projects")
