"""add roles

Revision ID: e4f4cd1251f8
Revises: 09d6bf15c64c
Create Date: 2023-01-12 14:28:23.000407

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4f4cd1251f8'
down_revision = '09d6bf15c64c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('roles_users',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('active', sa.Boolean(), nullable=True))
        batch_op.drop_index('ix_user_role')
        batch_op.drop_column('role')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role', sa.VARCHAR(length=10), nullable=True))
        batch_op.create_index('ix_user_role', ['role'], unique=False)
        batch_op.drop_column('active')

    op.drop_table('roles_users')
    op.drop_table('role')
    # ### end Alembic commands ###
