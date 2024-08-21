from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Index

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Dump20240820.db'

db = SQLAlchemy(app)

class book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), nullable=True, unique=True)
    
class borrowedbooks(db.Model):
    borrow_id = db.Column(db.Integer, nullable=False, primary_key=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), nullable=False,unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False, unique=True)
    return_date = db.Column(db.Date, nullable=True)
    
class ebook(db.Model):
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False, primary_key=True)
    file_format = db.Column(db.String(45), nullable=True)
    
    __table_args__ = (
        Index('book_id_index', 'book_id'),
    )
    
class joinlibrarybooks(db.Model):
    library_book_id = db.Column(db.Integer, nullable=False, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey('library.library_id'), nullable=False, unique=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False, unique=True)
    copies = db.Column(db.Integer, nullable=True)
    
class joinlibrarymembers(db.Model):
    library_member_id = db.Column(db.Integer, nullable=False, unique=True, primary_key=True)
    library_id = db.Column(db.Integer, db.ForeignKey('library.library_id'), nullable=False, unique=True)
    member_id = db.Column(db.Integer, db.ForeignKey('members.member_id'), nullable=False, unique=True)
    
class members(db.Model):
    member_id = db.Column(db.Integer, nullable=False, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    
class library(db.Model):
    library_id = db.Column(db.Integer, nullable=False, autoincrement=True, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    
    
with app.app_context():
    db.create_all()