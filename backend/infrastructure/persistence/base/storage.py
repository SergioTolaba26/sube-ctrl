from __future__ import annotations

import json
from pathlib import Path


class Storage:

    def __init__(
        self,
        file_path,
    ):
        self.file_path = Path(file_path)

    def load(
        self,
    ):

        if not self.file_path.exists():
            return []

        try:

            with self.file_path.open(
                "r",
                encoding="utf-8",
            ) as archivo:

                return json.load(
                    archivo,
                )

        except json.JSONDecodeError:

            return []
    def save(
        self,
        data,
    ):

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        temporal = self.file_path.with_suffix(
            self.file_path.suffix + ".tmp"
        )

        with temporal.open(
            "w",
            encoding="utf-8",
        ) as archivo:

            json.dump(
                data,
                archivo,
                ensure_ascii=False,
                indent=4,
            )

        temporal.replace(
            self.file_path,
        )