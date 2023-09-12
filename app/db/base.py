# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.curriculum_vitae_model import (  # noqa
    CurriculumVitae,
    Education,
    Project,
    WorkExperience,
)
