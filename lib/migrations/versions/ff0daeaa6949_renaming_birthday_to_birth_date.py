"""Renaming birthday to birth_date

Revision ID: ff0daeaa6949
Revises: 4821e537eef7
Create Date: 2024-10-31 16:17:22.492099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff0daeaa6949'
down_revision = '4821e537eef7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_column('birthday', 'birth_date')


def downgrade() -> None:
    op.rename_column('birth_date', 'birthday')
