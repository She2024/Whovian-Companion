from init import db

library_episode_association = db.Table('library_episode_association',
    db.Column('library_id', db.Integer, db.ForeignKey('libraries.id')),
    db.Column('episode_id', db.Integer, db.ForeignKey('episodes.id'))
)