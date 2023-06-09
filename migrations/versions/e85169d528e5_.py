"""empty message

Revision ID: e85169d528e5
Revises: 
Create Date: 2023-03-30 23:05:16.051462

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e85169d528e5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('group_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('membership_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('transaction_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('transaction_split_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'transaction_splits', ['transaction_split_id'], ['id'])
        batch_op.create_foreign_key(None, 'memberships', ['membership_id'], ['id'])
        batch_op.create_foreign_key(None, 'groups', ['group_id'], ['id'])
        batch_op.create_foreign_key(None, 'transactions', ['transaction_id'], ['id'])
        batch_op.create_foreign_key(None, 'users', ['user_id'], ['id'])

    with op.batch_alter_table('transaction_splits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('member_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint('transaction_splits_user_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'memberships', ['member_id'], ['id'])
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('transaction_splits', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('transaction_splits_user_id_fkey', 'users', ['user_id'], ['id'])
        batch_op.drop_column('member_id')

    with op.batch_alter_table('log_entries', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('transaction_split_id')
        batch_op.drop_column('transaction_id')
        batch_op.drop_column('membership_id')
        batch_op.drop_column('group_id')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
