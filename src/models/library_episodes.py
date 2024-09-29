from init import db

library_episode_association = db.Table('library_episode_association',
    db.Column('library_id', db.Integer, db.ForeignKey('library.id')),
    db.Column('episode_id', db.Integer, db.ForeignKey('episode.id'))
)