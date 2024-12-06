"""Add pdf_file to Course model

Revision ID: bb777789c6d1
Revises: 5e90169b1ccf
Create Date: 2024-12-05 23:01:38.227883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb777789c6d1'
down_revision = '5e90169b1ccf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.add_column(sa.Column('pdf_file', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('course', schema=None) as batch_op:
        batch_op.drop_column('pdf_file')

    # ### end Alembic commands ###