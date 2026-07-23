from persistence.json_storage import JsonStorage

from core.settings import settings

from models.tarifa import Tarifa

from repositories.base.base_repository import BaseRepository
from repositories.base.repository_config import RepositoryConfig


class TarifaRepository(BaseRepository[Tarifa]):

    def __init__(self):

        super().__init__(

            RepositoryConfig(

                storage=JsonStorage(
                    settings.DATA_PATH / "tarifas.json"
                ),

                key="tarifas",

                model=Tarifa

            )
        )