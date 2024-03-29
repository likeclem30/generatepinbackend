from datetime import datetime
from generatepins_backend.app import create_app
from generatepins_backend.models import GeneratepinModel


if __name__ == '__main__':
    application = create_app()
    application.app_context().push()

    # Create some test data
    test_data = [
        # username, timestamp, text
        ('bruce', "1111", datetime.now()),
        ('stephen', "1111", datetime.now()),
    ]
    for username, pin, expiry_time in test_data:
        user = GeneratepinModel(username=username, pin=pin, expiry_time=expiry_time)
        application.db.session.add(user)

    application.db.session.commit()
