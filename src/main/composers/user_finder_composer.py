from src.infra.db.repositories.users_repository import UsersRepository
from src.data.use_cases.user_finder import UserFinder
from src.presentation.controllers.user_finder_controller import UserFinderController

def user_finder_composer():
    repository = UsersRepository()
    use_case = UserFinder(repository)
    controller = UserFinderController(use_case)

    return controller.handle
