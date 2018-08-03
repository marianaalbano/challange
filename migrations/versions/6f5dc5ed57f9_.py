"""empty message

Revision ID: 6f5dc5ed57f9
Revises: 
Create Date: 2018-08-03 12:52:38.076203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f5dc5ed57f9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quiz',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('response_time', sa.String(), nullable=False),
    sa.Column('category', sa.String(), nullable=False),
    sa.Column('dificulty', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )

    users = op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )

    op.bulk_insert(users,
                   [
                       {'id': 1,
                        'name':'Administrator',
                        'email': 'admin@challange.com.br',
                        'username':'admin',
                        'telefone':'1111111',
                        'password':'admin',
                        'admin':True},
                        {'id': 2,
                        'name':'User',
                        'email': 'user@challange.com.br',
                        'username':'user',
                        'telefone':'1111111',
                        'password':'user',
                        'admin':False}

                   ]
                   )

    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('questions', sa.String(), nullable=False),
    sa.Column('right_question', sa.String(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('questions_multiple',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question', sa.String(), nullable=False),
    sa.Column('option_1', sa.String(), nullable=False),
    sa.Column('option_2', sa.String(), nullable=False),
    sa.Column('option_3', sa.String(), nullable=False),
    sa.Column('option_4', sa.String(), nullable=False),
    sa.Column('right_question', sa.String(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    op.create_table('quiz_users',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('quiz_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['quiz_id'], ['quiz.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users_id', 'quiz_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quiz_users')
    op.drop_table('questions_multiple')
    op.drop_table('questions')
    op.drop_table('users')
    op.drop_table('quiz')
    # ### end Alembic commands ###
