"""add foreign key to Review

Revision ID: 49970a454ea6
Revises: 51169b924c35
Create Date: 2024-06-06 10:09:42.509740

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '49970a454ea6'
down_revision = '51169b924c35'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reviews', sa.Column('employee_id', sa.Integer(), nullable=True))
    op.create_foreign_key(op.f('fk_reviews_employee_id_employees'), 'reviews', 'employees', ['employee_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('fk_reviews_employee_id_employees'), 'reviews', type_='foreignkey')
    op.drop_column('reviews', 'employee_id')
    # ### end Alembic commands ###
