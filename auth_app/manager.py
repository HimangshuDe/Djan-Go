from django.contrib.auth.base_user import BaseUserManager


# Since we are creating model with our custom fields so defined
# We also need to create a custom manager class to manage the model.
class CustomUserManager(BaseUserManager):
    # For creating users without admin privileges
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        # Abc.def@domain.com
        # After normalising it will be abc.def@domain.com
        email = self.normalize_email(
            email
        )  # Setting the email to lowercase, if not previously.
        user = self.model(email=email, **extra_fields)
        user.set_password(
            password
        )  # Setting passwords for the user but in encrypted form
        user.save()  # Saving all to our custom made model.
        return user

    # For creating superusers
    def create_superuser(self, email, password, **extra_fields):
        # extra fields for admin access
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, password, **extra_fields)
