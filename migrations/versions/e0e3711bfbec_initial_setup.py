"""initial setup

Revision ID: e0e3711bfbec
Revises: 
Create Date: 2017-03-22 21:16:23.284653

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0e3711bfbec'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carpools',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('from_place', sa.String(length=120), nullable=True),
    sa.Column('to_place', sa.String(length=120), nullable=True),
    sa.Column('leave_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('return_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('max_riders', sa.Integer(), nullable=True),
    sa.Column('driver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['people.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('riders',
    sa.Column('person_id', sa.Integer(), nullable=True),
    sa.Column('carpool_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['carpool_id'], ['carpools.id'], ),
    sa.ForeignKeyConstraint(['person_id'], ['people.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('riders')
    op.drop_table('carpools')
    op.drop_table('people')
    # ### end Alembic commands ###