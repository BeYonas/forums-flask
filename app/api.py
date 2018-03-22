from flask import request, jsonify, redirect, url_for
from app import app, post_store, models


@app.route("/api/topic/all")
def api_topic_get_all():
    posts = [post.__dict__() for post in post_store.get_all()]
    return jsonify(posts)


@app.route("/api/topic/add", methods=["POST"])
def api_topic_create():
    request_data = request.get_json()
    new_post = models.Post(request_data["title"], request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__())


@app.route("/api/topic/<int:post_id>", methods=["GET"])
def api_topic_read(post_id):
    post_to_read = post_store.get_by_id(post_id)
    return jsonify(post_to_read.__dict__())


@app.route("/api/topic/delete/<int:post_id>")
def api_topic_delete(post_id):
    post_store.delete(post_id)
    return redirect(url_for("/home"))


@app.route("/api/topic/edit/<int:post_id>", methods=["GET", "POST"])
def api_topic_update(post_id):
    post_to_edit = post_store.get_by_id(post_id)
    if request.method == "POST":
        request_data = request.get_json()
        post_to_edit.title = request_data["title"]
        post_to_edit.content = request_data["content"]
    return jsonify(post_to_edit.__dict__())

