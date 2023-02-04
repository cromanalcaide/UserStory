"""empty message

Revision ID: ad1f6ba6ddf4
Revises: 5c15b8881b1e
Create Date: 2023-02-04 09:10:01.151304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ad1f6ba6ddf4'
down_revision = '5c15b8881b1e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('user_phone_key', 'user', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('user_phone_key', 'user', ['phone'])
    # ### end Alembic commands ###