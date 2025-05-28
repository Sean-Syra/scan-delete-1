from app import create_app, db
from app.models import User
from werkzeug.security import generate_password_hash

app = create_app()

# Create an admin user
def create_admin():
    with app.app_context():
        db.create_all()
        
        # Check if admin already exists
        admin = User.query.filter_by(email='admin@example.com').first()
        if not admin:
            admin = User(
                email='admin@example.com',
                name='Admin',
                password=generate_password_hash('admin123', method='sha256')
            )
            db.session.add(admin)
            db.session.commit()

if __name__ == '__main__':
    create_admin()
    app.run(debug=True)