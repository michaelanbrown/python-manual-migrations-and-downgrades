"""Renaming students to scholars

Revision ID: 4821e537eef7
Revises: 791279dd0760
Create Date: 2024-10-31 16:07:58.713342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4821e537eef7'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
