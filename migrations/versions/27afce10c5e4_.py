"""empty message

Revision ID: 27afce10c5e4
Revises: 3d631b755b30
Create Date: 2023-01-19 21:57:59.193711

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27afce10c5e4'
down_revision = '3d631b755b30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('article_tag_association',
    sa.Column('article_id', sa.Integer(), nullable=False),
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['article_id'], ['articles.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tags.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('article_tag_association')
    op.drop_table('tags')
    # ### end Alembic commands ###