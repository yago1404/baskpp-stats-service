"""create games table

Revision ID: 6dc9a0c284fe
Revises: 9ea6d51a2aa3
Create Date: 2025-04-19 14:02:48.965376

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6dc9a0c284fe'
down_revision: Union[str, None] = '9ea6d51a2aa3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
        CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
    
        CREATE TABLE IF NOT EXISTS games (
            id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
            team UUID NOT NULL,
            adversary TEXT NOT NULL,
            date_time TIMESTAMP NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute("""
        DROP TABLE IF EXISTS games;
    """)
