"""Add customer foreign key to orders

Revision ID: ef9b7d56840b
Revises: 
Create Date: 2024-10-02 23:00:08.309723

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ef9b7d56840b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(None, 'customers', ['customer_id'], ['customer_id'])
        batch_op.drop_column('customer_name')
        batch_op.drop_column('customer_mobile')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('orders', schema=None) as batch_op:
        batch_op.add_column(sa.Column('customer_mobile', mysql.VARCHAR(length=15), nullable=False))
        batch_op.add_column(sa.Column('customer_name', mysql.VARCHAR(length=100), nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('customer_id')

    # ### end Alembic commands ###
