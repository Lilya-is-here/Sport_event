"""User update

Revision ID: d85d1f02e977
Revises: b59f8401da01
Create Date: 2023-01-22 11:39:58.484379

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd85d1f02e977'
down_revision = 'b59f8401da01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_role_id_role', type_='foreignkey')
        batch_op.drop_column('role_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('role_id', sa.INTEGER(), nullable=True))
        batch_op.create_foreign_key('fk_user_role_id_role', 'role', ['role_id'], ['id'])

    # ### end Alembic commands ###
