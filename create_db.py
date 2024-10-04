from project.app import app, db

if __name__ == "__main__":
    with app.app_context():
        # create the database and the db table
        db.create_all()

        # commit the changes
        db.session.commit()