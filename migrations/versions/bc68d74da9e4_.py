"""empty message

Revision ID: bc68d74da9e4
Revises: a74e961fb61c
Create Date: 2021-11-23 03:58:11.824779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc68d74da9e4'
down_revision = 'a74e961fb61c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('obra',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=255), nullable=False),
    sa.Column('editora', sa.String(length=255), nullable=True),
    sa.Column('foto', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('titulo')
    )
    op.create_table('autor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=255), nullable=False),
    sa.Column('obra_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['obra_id'], ['obra.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nome')
    )
    op.drop_table('autores')
    op.drop_table('obras')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('obras',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('obras_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('editora', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('foto', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='obras_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('autores',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('obras_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['obras_id'], ['obras.id'], name='autores_obras_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='autores_pkey')
    )
    op.drop_table('autor')
    op.drop_table('obra')
    # ### end Alembic commands ###
