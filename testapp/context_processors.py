from .models import User

def user_context(request):
    user = None
    user_id = request.session.get('user_id')
    if user_id:
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            user = None
    return {'current_user': user}
