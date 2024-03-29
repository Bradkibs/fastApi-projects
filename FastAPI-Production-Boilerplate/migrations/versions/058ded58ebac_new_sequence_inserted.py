"""new sequence inserted

Revision ID: 058ded58ebac
Create Date: 2023-10-20 10:58:56.846654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '058ded58ebac'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(sa.text("CREATE SEQUENCE id_seq START 100000000000;"))
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), sa.Sequence('id_seq'), autoincrement=True, nullable=False, server_default=sa.text("nextval('id_seq'::regClass)")),
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('email', sa.Unicode(length=255), nullable=False),
    sa.Column('password', sa.Unicode(length=255), nullable=False),
    sa.Column('phone_number', sa.Unicode(length=20), nullable=False),
    sa.Column('location', sa.Unicode(length=255), nullable=False),
    sa.Column('role', sa.Enum('admin', 'user', 'customer_service', name='user_roles'), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('username', sa.Unicode(length=255), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='user_emails'),
    sa.UniqueConstraint('id', name='user_ids'),
    sa.UniqueConstraint('username', name='user_usernames'),
    sa.UniqueConstraint('uuid', name='user_uuids')
    )
    op.create_table('tasks',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('uuid', sa.UUID(), nullable=False),
    sa.Column('title', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('is_completed', sa.Boolean(), nullable=False),
    sa.Column('task_author_id', sa.BigInteger(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['task_author_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('uuid', name='task_uuids')
    )

    # ### end Alembic commands ###

def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('id', 'users')
    op.drop_constraint('uuid', 'users')
    op.drop_constraint('user_name', 'users')
    op.drop_constraint('email', 'users')
    op.drop_constraint('uuid', 'tasks')
    op.drop_table('tasks')
    op.drop_table('users')
    # ### end Alembic commands ###
