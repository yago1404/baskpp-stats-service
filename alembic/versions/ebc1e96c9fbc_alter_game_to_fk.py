"""alter game to FK

Revision ID: ebc1e96c9fbc
Revises: 252fda7accdc
Create Date: 2025-05-28 09:07:29.325313

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ebc1e96c9fbc'
down_revision: Union[str, None] = '252fda7accdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute('''
               ALTER TABLE plays
                   ADD CONSTRAINT fk_plays_game
                       FOREIGN KEY (game)
                           REFERENCES games (id);
               ''')
    pass


def downgrade() -> None:
    op.execute('''
               ALTER TABLE plays
                   DROP CONSTRAINT fk_plays_game;
               ''')
    pass
