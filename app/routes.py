from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.models import User, Task, Project
from app.schemas import UserSchema, TaskSchema, ProjectSchema
from app import db

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

user_schema = UserSchema()
task_schema = TaskSchema()
project_schema = ProjectSchema()

class UserRegistration(Resource):
    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {'message': 'Username already exists'}, 400
        
        new_user = User(username=data['username'], email=data['email'])
        new_user.set_password(data['password'])
        db.session.add(new_user)
        db.session.commit()
        
        return user_schema.dump(new_user), 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and user.check_password(data['password']):
            access_token = create_access_token(identity=user.id)
            return {'access_token': access_token}, 200
        return {'message': 'Invalid credentials'}, 401

class TaskList(Resource):
    @jwt_required()
    def get(self):
        tasks = Task.query.all()
        return task_schema.dump(tasks, many=True), 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_task = Task(**data)
        db.session.add(new_task)
        db.session.commit()
        return task_schema.dump(new_task), 201

class TaskResource(Resource):
    @jwt_required()
    def get(self, task_id):
        task = Task.query.get_or_404(task_id)
        return task_schema.dump(task), 200

    @jwt_required()
    def put(self, task_id):
        task = Task.query.get_or_404(task_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(task, key, value)
        db.session.commit()
        return task_schema.dump(task), 200

    @jwt_required()
    def delete(self, task_id):
        task = Task.query.get_or_404(task_id)
        db.session.delete(task)
        db.session.commit()
        return '', 204

class ProjectList(Resource):
    @jwt_required()
    def get(self):
        projects = Project.query.all()
        return project_schema.dump(projects, many=True), 200

    @jwt_required()
    def post(self):
        data = request.get_json()
        new_project = Project(**data)
        db.session.add(new_project)
        db.session.commit()
        return project_schema.dump(new_project), 201

class ProjectResource(Resource):
    @jwt_required()
    def get(self, project_id):
        project = Project.query.get_or_404(project_id)
        return project_schema.dump(project), 200

    @jwt_required()
    def put(self, project_id):
        project = Project.query.get_or_404(project_id)
        data = request.get_json()
        for key, value in data.items():
            setattr(project, key, value)
        db.session.commit()
        return project_schema.dump(project), 200

    @jwt_required()
    def delete(self, project_id):
        project = Project.query.get_or_404(project_id)
        db.session.delete(project)
        db.session.commit()
        return '', 204

api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(TaskList, '/tasks')
api.add_resource(TaskResource, '/tasks/<int:task_id>')
api.add_resource(ProjectList, '/projects')
api.add_resource(ProjectResource, '/projects/<int:project_id>')