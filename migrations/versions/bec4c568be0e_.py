"""empty message

Revision ID: bec4c568be0e
Revises: 
Create Date: 2019-09-06 08:53:32.082459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bec4c568be0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=120), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('logstakeholder',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('stakeholder_person', sa.String(length=120), nullable=True),
    sa.Column('organisation', sa.String(length=120), nullable=True),
    sa.Column('stance', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=120), nullable=True),
    sa.Column('keypoints', sa.String(length=120), nullable=True),
    sa.Column('bpier', sa.String(length=120), nullable=True),
    sa.Column('meeting', sa.String(length=120), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_logstakeholder_keypoints'), 'logstakeholder', ['keypoints'], unique=False)
    op.create_index(op.f('ix_logstakeholder_organisation'), 'logstakeholder', ['organisation'], unique=False)
    op.create_index(op.f('ix_logstakeholder_stakeholder_person'), 'logstakeholder', ['stakeholder_person'], unique=False)
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=140), nullable=True),
    sa.Column('location', sa.String(length=140), nullable=True),
    sa.Column('date', sa.String(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_post_timestamp'), 'post', ['timestamp'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_post_timestamp'), table_name='post')
    op.drop_table('post')
    op.drop_index(op.f('ix_logstakeholder_stakeholder_person'), table_name='logstakeholder')
    op.drop_index(op.f('ix_logstakeholder_organisation'), table_name='logstakeholder')
    op.drop_index(op.f('ix_logstakeholder_keypoints'), table_name='logstakeholder')
    op.drop_table('logstakeholder')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###