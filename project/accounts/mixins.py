from .models import UserProfile


class CreateUserProfileInstanceIfUserIsAuthenticated:
    def get(self, *args, **kwargs):
        user = self.request.user if self.request.user.is_authenticated else None
        if user and not UserProfile.objects.filter(user=user).exists():
            UserProfile.objects.create(user=user)
        return super().get(*args, **kwargs)