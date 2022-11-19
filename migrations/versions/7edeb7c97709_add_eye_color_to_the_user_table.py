"""add eye color to the user table

Revision ID: 7edeb7c97709
Revises: 
Create Date: 2022-10-08 19:57:16.749530

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7edeb7c97709'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('eye_color', sa.String(length=30), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'eye_color')
    # ### end Alembic commands ###