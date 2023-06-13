"""auto-vote

Revision ID: ad5a3b3be5b0
Revises: f0dac97e87eb
Create Date: 2023-06-10 14:55:38.551660

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad5a3b3be5b0'
down_revision = 'f0dac97e87eb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_numer', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'phone_numer')
    # ### end Alembic commands ###