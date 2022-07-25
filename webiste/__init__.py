from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # import blueprints
    from .webhooks import webhooks

    # register SMS & whatsapp blueprints
    app.register_blueprint(webhooks, url_prefix='/')

    return app
