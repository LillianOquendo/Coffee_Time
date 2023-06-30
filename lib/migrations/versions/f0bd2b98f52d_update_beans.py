"""update beans

Revision ID: f0bd2b98f52d
Revises: 
Create Date: 2023-06-29 23:05:50.382686

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f0bd2b98f52d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('coffees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('roast', sa.String(), nullable=True),
    sa.Column('coarse_vs_fine', sa.Boolean(), nullable=True),
    sa.Column('price', sa.Numeric(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('locations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('location', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('beans',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bean_type', sa.String(), nullable=True),
    sa.Column('location', sa.Integer(), nullable=True),
    sa.Column('flavor_profile', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['location'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('shops',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('shop_name', sa.String(), nullable=True),
    sa.Column('shop_location_id', sa.Integer(), nullable=True),
    sa.Column('rating', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['shop_location_id'], ['locations.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shops')
    op.drop_table('beans')
    op.drop_table('locations')
    op.drop_table('coffees')
    # ### end Alembic commands ###
