from flask import Blueprint, render_template

error_bp = Blueprint('error_bp', __name__, template_folder='templates')

@error_bp.app_errorhandler(404)
def not_found_error(error):
    print(error)
    return render_template('404.html', error=error, title="Error"), 404