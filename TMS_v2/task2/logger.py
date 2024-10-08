import logging

logger = logging.getLogger(__name__)

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    # Log authentication attempt
    logger.info(f"User {username} attempted to log in with password {password}")
    
    # Authenticate user
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        logger.info(f"User {username} logged in successfully")
    else:
        logger.warning(f"Invalid login attempt for user {username}")