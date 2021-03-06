"""empty message

Revision ID: 6358d92bf2a9
Revises: 1c766eb89efa
Create Date: 2021-12-23 20:28:45.142116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6358d92bf2a9'
down_revision = '1c766eb89efa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('category_id', sa.Integer(), nullable=True))
    op.add_column('blog', sa.Column('content', sa.Text(), nullable=False))
    op.alter_column('blog', 'author',
               existing_type=sa.VARCHAR(length=40),
               nullable=False)
    op.create_foreign_key(None, 'blog', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'blog', type_='foreignkey')
    op.alter_column('blog', 'author',
               existing_type=sa.VARCHAR(length=40),
               nullable=True)
    op.drop_column('blog', 'content')
    op.drop_column('blog', 'category_id')
    # ### end Alembic commands ###
