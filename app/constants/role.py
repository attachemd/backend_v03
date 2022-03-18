class Role:
    """
    Constants for the various roles scoped in the application ecosystem
    """

    GUEST = {
        "name": "GUEST",
        "description": "A Guest Client",
    }
    CLIENT_ADMIN = {
        "name": "CLIENT_ADMIN",
        "description": "Primary Administrator/Superuser For an Client",
    }

    CLIENT_MANAGER = {
        "name": "CLIENT_MANAGER",
        "description": "Day to Day Administrator of Events For an Client",
    }
    ADMIN = {
        "name": "ADMIN",
        "description": "Admin of Application Ecosystem",
    }
    SUPER_ADMIN = {
        "name": "SUPER_ADMIN",
        "description": "Super Administrator of Application Ecosystem",
    }
