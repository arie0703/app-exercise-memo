from flask import Blueprint, request, make_response, jsonify
from models import Template, TemplateSchema
import json

# ルーティング設定
template_router = Blueprint('template_router', __name__)

@template_router.route('/templates', methods=['GET'])
def getTemplate():

    templates = Template.getTemplate()
    template_schema = TemplateSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'templates': template_schema.dump(templates)
    }))

@template_router.route('/templates/create', methods=['POST'])

def createTemplate():

    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    templateData = json.loads(jsonData)

    template = Template.createTemplate(templateData)
    template_schema = TemplateSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'template': template
    }))

@template_router.route('/templates/delete/<int:id>', methods=['POST'])
def deleteTemplate(id):

    deleted_id = Template.deleteTemplate(id)

    return make_response(jsonify({
        'code': 200,
        'id': deleted_id
    }))