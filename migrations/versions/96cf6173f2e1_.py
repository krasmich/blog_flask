"""empty message

Revision ID: 96cf6173f2e1
Revises: 67191bbf6435
Create Date: 2023-01-16 23:03:20.457681

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96cf6173f2e1'
down_revision = '67191bbf6435'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('authors')
    # ### end Alembic commands ###
