from flask import Blueprint, request, make_response, jsonify
from models import Menu, MenuSchema
import json

# ルーティング設定
menu_router = Blueprint('menu_router', __name__)

@menu_router.route('/menus', methods=['GET'])
def getMenu():

    menus = Menu.getMenu()
    menu_schema = MenuSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'menus': menu_schema.dump(menus)
    }))

@menu_router.route('/menus/template_id=<int:template_id>', methods=['GET'])
def getSetMenu(template_id):
    menus = Menu.getSetMenu(template_id)
    menu_schema = MenuSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'menus': menu_schema.dump(menus)
    }))

@menu_router.route('/menus/create', methods=['POST'])

def createMenu():

    # jsonデータを取得する
    jsonData = json.dumps(request.json)
    menuData = json.loads(jsonData)

    menu = Menu.createMenu(menuData)
    menu_schema = MenuSchema(many=True)

    return make_response(jsonify({
        'code': 200,
        'menu': menu
    }))