from app import create_app, db
from app.Model.models import Post

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Post': Post}

@app.before_first_request
def initDB(*args, **kwargs):
    db.create_all()
    # if Tag.query.count() == 0:
    #     tags = ['funny','inspiring', 'true-story', 'heartwarming', 'friendship']
    #     for t in tags:
    #         db.session.add(Tag(name=t))
    #     db.session.commit()

if __name__ == "__main__":
    app.run(debug=True)