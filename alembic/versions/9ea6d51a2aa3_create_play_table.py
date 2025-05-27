"""create play table

Revision ID: 9ea6d51a2aa3
Revises: 
Create Date: 2025-04-19 13:45:31.994868

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9ea6d51a2aa3'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

    CREATE TABLE IF NOT EXISTS plays (
        id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
        player UUID NOT NULL,
        game UUID NOT NULL,
        court_locate character NOT NULL,
        free_throw int,
        failure_free_throw int,
        two_points int,
        failure_two_points int,
        tree_points int,
        failure_tree_points int,
        assistances int,
        steals int,
        rebounds int,
        blocks int,
        falts int,
        turnovers int,
        created_at TIMESTAMP DEFAULT NOW()
    );
    """)
    pass


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS plays;")
