from ..auth import bp

@bp.route('/login')
def login():
    return 'login'