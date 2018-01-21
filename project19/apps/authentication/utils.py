

# check authenticated user
# for passed test login and register url
def check_user_auth(user):
    return True if not user.is_authenticated() else False