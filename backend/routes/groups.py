from flask import Blueprint, jsonify
from sqlalchemy import select

from backend import db
from backend.models.group import Group, GroupSchema

groups_bp = Blueprint("groups", __name__, url_prefix="/groups")
group_schema = GroupSchema()


@groups_bp.route("", methods=["GET"])
def get_all_groups():
    # style 1.X
    # groups = Group.query.all()

    # style 2.0
    groups = db.session.scalars(select(Group)).all()
    return jsonify(group_schema.dump(groups, many=True))
