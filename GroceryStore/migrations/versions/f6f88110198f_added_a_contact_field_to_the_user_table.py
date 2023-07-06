"""Added a contact field to the User table

Revision ID: f6f88110198f
Revises: 
Create Date: 2023-07-06 21:04:41.404478

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6f88110198f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.add_column(sa.Column('contact', sa.String(length=15), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('User', schema=None) as batch_op:
        batch_op.drop_column('contact')

    # ### end Alembic commands ###