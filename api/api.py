import flask
import json
import level as l
from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class ExpModel(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    exp = db.Column(db.Integer, nullable=True)
    ballL = db.Column(db.Integer, nullable=True)
    ballW = db.Column(db.Integer, nullable=True)
    highScore = db.Column(db.Integer, nullable=True)
    shooterL = db.Column(db.Integer, nullable=True)
    shooterW = db.Column(db.Integer, nullable=True)
    typeW = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"id({id})"


db.create_all()

add_ARGS = reqparse.RequestParser()
add_ARGS.add_argument(
    "Add", type=int, help="Args for \"add\" is incorrect", required=True)
add_ARGS.add_argument(
    "Type", type=str, help="Args for \"Type\" is incorrect", required=True)

all_ARGS = reqparse.RequestParser()
all_ARGS.add_argument(
    "Type", type=str, help="Args for \"Type\" is incorrect", required=True)

resource_fields = {
    'id': fields.String,
    "exp": fields.Integer,
    "ballL": fields.Integer,
    "ballW": fields.Integer,
    "highScore": fields.Integer,
    "shooterL": fields.Integer,
    "shooterW": fields.Integer,
    "typeW": fields.Integer
}


class level(Resource):
    @marshal_with(resource_fields)
    def get(self, id_Discord):
        args = all_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        return result

    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, exp=args["Add"])
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.exp += args["Add"]
        except:
            result.exp = args['Add']
        db.session.commit()
        return result


class ballW(Resource):
    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, ballW=1)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.ballW += 1
        except:
            result.ballW = 1
        db.session.commit()
        return result


class ballL(Resource):
    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, ballL=1)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.ballL += 1
        except:
            result.ballL = 1
        db.session.commit()
        return result


class shooterW(Resource):
    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, shooterW=1)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.shooterW += 1
        except:
            result.shooterW = 1
        db.session.commit()
        return result


class shooterL(Resource):
    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, shooterL=1)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.shooterL += 1
        except:
            result.shooterL = 1
        db.session.commit()
        return result


class highScore(Resource):
    @marshal_with(resource_fields)
    def get(self, id_Discord):
        args = all_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        return result

    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, highScore=args["Add"])
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        result.highScore = args["Add"]
        db.session.commit()
        return result


class type(Resource):
    @marshal_with(resource_fields)
    def get(self, id_Discord):
        args = all_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        return result

    @marshal_with(resource_fields)
    def put(self, id_Discord):
        args = add_ARGS.parse_args()
        result = ExpModel.query.filter_by(id=id_Discord).first()
        if not result:
            result = ExpModel(id=id_Discord, typeW=1)
            db.session.add(result)
            db.session.commit()
            return result
            abort()
        try:
            result.typeW += args["Add"]
        except:
            result.typeW = args["Add"]
        db.session.commit()
        return result


class lb(Resource):
    @marshal_with(resource_fields)
    def get(self, type):
        if type == "exp":
            result = db.session.query(func.max(ExpModel.exp))
        if type == "ballW":
            result = ExpModel.query.order_by(ballW).limit(1)
        if type == "shooterW":
            result = ExpModel.query.order_by(shooterW).limit(1)
        if type == "typeW":
            result = ExpModel.query.order_by(typeW).limit(1)
        if not result:
            abort('No one has played')
        return result


api.add_resource(level, "/level/<string:id_Discord>")
api.add_resource(ballW, "/ballW/<string:id_Discord>")
api.add_resource(ballL, "/ballL/<string:id_Discord>")
api.add_resource(shooterW, "/shooterW/<string:id_Discord>")
api.add_resource(shooterL, "/shooterL/<string:id_Discord>")
api.add_resource(highScore, "/highScore/<string:id_Discord>")
api.add_resource(type, "/type/<string:id_Discord>")
api.add_resource(lb, "/lb/<string:type>")

if __name__ == '__main__':
    app.run(debug=True)
