from database import db, ma
from .menu import Menu

class Template(db.Model):
    __tablename__ = 'templates'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Template %r>' % self.name

    def getTemplate():

        template_list = db.session.query(Template).all()

        if template_list == None:
            return []
        else:
            return template_list

    def createTemplate(template):
        record = Template(
            title = template['title'],
        )

        db.session.add(record)
        db.session.commit()

        return Template

class TemplateSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Template
        fields = ('id', 'title')