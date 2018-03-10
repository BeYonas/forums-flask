from flask import Flask
import dummy_data
import stores

app = Flask(__name__)

member_store = stores.MemberStore()
post_store = stores.PostStore()

from app import views

dummy_data.seed_stores(member_store, post_store)
