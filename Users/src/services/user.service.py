from ..domain.models.user import User
from ..repository.user_repository import UserRepository

<<<<<<< HEAD
class UserService:
    def __init__(self, user_repo: UserRepository):
        
        self.user_repo = user_repo
        
    def create_user(self, id: int, name: str, email: str)-> User:
        new_user = User(id = id, name = name, email = email)
=======

class UserService:
    def __init__(self, user_repo: UserRepository):

        self.user_repo = user_repo

    def create_user(self, id: int, name: str, email: str) -> User:
        new_user = User(id=id, name=name, email=email)
>>>>>>> origin/master

        self.user_repo.create(new_user)

        return new_user

    def get_user(self, user_id: int) -> User | None:
        user_data = self.user_repo.find_by_id(user_id)

        if user_data:
            return User(**user_data)
        else:
            return None

<<<<<<< HEAD



          
=======
    def update_user(self, id: int, name: str, email: str) -> bool:
        existing_user = self.get_user(id)

        if not existing_user:
            return False

    updated_user = User(id=id, name=name, email=email)

    return self.user_repo.update(updated_user) 


>>>>>>> origin/master
