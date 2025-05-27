"""change court locate column type

Revision ID: 252fda7accdc
Revises: 6dc9a0c284fe
Create Date: 2025-05-22 15:26:19.798086

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '252fda7accdc'
down_revision: Union[str, None] = '6dc9a0c284fe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("""
    ALTER TABLE plays
    ALTER COLUMN court_locate TYPE TEXT;
    """)
    pass


def downgrade() -> None:
    op.execute("""
    ALTER TABLE games
    ALTER COLUMN plays TYPE character;
    """)
    pass
