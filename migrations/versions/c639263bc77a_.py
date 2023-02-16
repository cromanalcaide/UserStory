"""empty message

Revision ID: c639263bc77a
Revises: 557e8f558a36
Create Date: 2023-02-16 18:39:15.064424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c639263bc77a'
down_revision = '557e8f558a36'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('contact_forms', schema=None) as batch_op:
        batch_op.drop_constraint('contact_forms_user_id_fkey', type_='foreignkey')
        batch_op.drop_column('user_id')

    with op.batch_alter_table('event_guests', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(length=120), nullable=True))

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=360),
               nullable=True)

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('avatar_url', sa.String(length=300), nullable=True))
        batch_op.add_column(sa.Column('accept_news', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('accept_news')
        batch_op.drop_column('avatar_url')

    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.alter_column('image',
               existing_type=sa.VARCHAR(length=360),
               nullable=False)

    with op.batch_alter_table('event_guests', schema=None) as batch_op:
        batch_op.drop_column('email')

    with op.batch_alter_table('contact_forms', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('contact_forms_user_id_fkey', 'user', ['user_id'], ['id'])

    # ### end Alembic commands ###
