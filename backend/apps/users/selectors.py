from .models import User


def get_user_by_id(user_id: int) -> User:
    return User.objects.get(id=user_id)


def get_user_by_email(email: str) -> User:
    return User.objects.get(email=email)


def list_users():
    return User.objects.all()
