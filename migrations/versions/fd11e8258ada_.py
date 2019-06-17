"""empty message

Revision ID: fd11e8258ada
Revises: 780739b227a7
Create Date: 2019-06-17 12:54:47.000418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd11e8258ada'
down_revision = '780739b227a7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('log_stakeholder',
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('stakeholder_person', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_username', sa.String(length=64), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('user_username')
    )
    op.create_index(op.f('ix_log_stakeholder_date'), 'log_stakeholder', ['date'], unique=False)
    op.create_index(op.f('ix_log_stakeholder_stakeholder_person'), 'log_stakeholder', ['stakeholder_person'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_log_stakeholder_stakeholder_person'), table_name='log_stakeholder')
    op.drop_index(op.f('ix_log_stakeholder_date'), table_name='log_stakeholder')
    op.drop_table('log_stakeholder')
    # ### end Alembic commands ###
