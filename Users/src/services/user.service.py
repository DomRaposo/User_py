from ..domain.models.user import User
from ..repository.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository):
        
        self.user_repo = user_repo
        
    def create_user(self, id: int, name: str, email: str)-> User:
        new_user = User()

        self.user_repo.create(new_user)

        return new_user
