"""users table

Revision ID: 4235759ed878
Revises: 7cc07b7ca47f
Create Date: 2022-01-02 10:32:24.945384

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4235759ed878'
down_revision = '7cc07b7ca47f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('nome', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('cognome', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_user_cognome'), 'user', ['cognome'], unique=False)
    op.create_index(op.f('ix_user_nome'), 'user', ['nome'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_nome'), table_name='user')
    op.drop_index(op.f('ix_user_cognome'), table_name='user')
    op.drop_column('user', 'cognome')
    op.drop_column('user', 'nome')
    # ### end Alembic commands ###