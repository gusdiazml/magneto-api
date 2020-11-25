from main import db

class Dna(db.Model):

    __tablename__ = "dna"

    id = db.Column(db.Integer, primary_key=True)
    sequences = db.Column(db.JSON)
    is_mutant = db.Column(db.Boolean)
    created_date = db.Column(db.DateTime)
    updated_date = db.Column(db.DateTime)

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_stats():
        return db.session.query(Dna.is_mutant, db.func.count(Dna.is_mutant)).group_by(Dna.is_mutant).all()