"""Coefficient update

Revision ID: 543406305359
Revises: 143b1f846edf
Create Date: 2023-02-01 23:16:16.831439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '543406305359'
down_revision = '143b1f846edf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_coefficient')
    with op.batch_alter_table('coefficient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('result', sa.String(), nullable=False))
        batch_op.drop_column('Result')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('coefficient', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Result', sa.VARCHAR(), nullable=False))
        batch_op.drop_column('result')

    op.create_table('_alembic_tmp_coefficient',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('event_id', sa.INTEGER(), nullable=False),
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('BK', sa.VARCHAR(), nullable=False),
    sa.Column('coefficient', sa.VARCHAR(), nullable=False),
    sa.Column('result', sa.VARCHAR(), nullable=False),
    sa.ForeignKeyConstraint(['event_id'], ['event.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
