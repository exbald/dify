"""update upload_files.source_url

Revision ID: f4d7ce70a7ca
Revises: 93ad8c19c40b
Create Date: 2024-11-01 05:40:03.531751

"""
from alembic import op
import models as models
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'f4d7ce70a7ca'
down_revision = '93ad8c19c40b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('upload_files', schema=None) as batch_op:
        batch_op.alter_column('source_url',
               existing_type=sa.VARCHAR(length=255),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("''::character varying"))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('upload_files', schema=None) as batch_op:
        batch_op.alter_column('source_url',
               existing_type=sa.TEXT(),
               type_=sa.VARCHAR(length=255),
               existing_nullable=False,
               existing_server_default=sa.text("''::character varying"))

    # ### end Alembic commands ###