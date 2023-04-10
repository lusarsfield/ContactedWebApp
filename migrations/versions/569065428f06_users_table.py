"""users table

Revision ID: 569065428f06
Revises: 3f6a17cda9c3
Create Date: 2023-04-10 11:49:57.735762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '569065428f06'
down_revision = '3f6a17cda9c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('company_me', sa.String(length=140), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('company_me')

    # ### end Alembic commands ###