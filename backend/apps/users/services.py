from django.contrib.auth import get_user_model

User = get_user_model()


def create_user(*, email: str, username: str, password: str) -> User:
    user = User.objects.create_user(
        email=email,
        username=username,
        password=password,
    )
    return user


def update_user(user: User, **data) -> User:
    for field, value in data.items():
        setattr(user, field, value)

    user.save()
    return user
