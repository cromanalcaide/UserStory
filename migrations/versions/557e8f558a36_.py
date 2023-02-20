"""empty message

Revision ID: 557e8f558a36
Revises: 18f750befa51
Create Date: 2023-02-16 10:29:07.645962

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '557e8f558a36'
down_revision = '18f750befa51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contact_forms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('message', sa.Text(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.VARCHAR(length=80),
               type_=sa.String(length=220),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=220),
               type_=sa.VARCHAR(length=80),
               existing_nullable=False)

    op.drop_table('contact_forms')
    # ### end Alembic commands ###