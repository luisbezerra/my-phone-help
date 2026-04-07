"""
Create a Django superuser. Non-interactive if env vars are set:

  DJANGO_SUPERUSER_USERNAME
  DJANGO_SUPERUSER_PASSWORD
  DJANGO_SUPERUSER_EMAIL (optional)
"""
import os
import sys

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from django.contrib.auth import get_user_model


def main() -> int:
    User = get_user_model()
    username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
    password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
    email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "")

    if not username or not password:
        print(
            "Set DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD.\n"
            "Optional: DJANGO_SUPERUSER_EMAIL",
            file=sys.stderr,
        )
        return 1

    if User.objects.filter(username=username).exists():
        print(f"User '{username}' already exists.")
        return 0

    User.objects.create_superuser(
        username=username,
        email=email or f"{username}@localhost",
        password=password,
    )
    print(f"Superuser '{username}' created.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
