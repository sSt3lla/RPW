from main import bp

@bp.route('/')
def index():
    return 'main'