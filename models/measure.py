#!/usr/bin/python
""" holds class Place"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float

class Measure(BaseModel, Base):
    """Representation of Place """
    if models.storage_t == 'db':
        __tablename__ = 'measures'
        first_name = Column(String(60), nullable=False)
        last_name = Column(String(60), nullable=False)
        e_measure = Column(Float, nullable=True, default=0.0)
        p_measure = Column(Float, nullable=True, default=0.0)
        lm_measure = Column(Float, nullable=True, default=0.0)
        tm_measure = Column(Float, nullable=True, default=0.0)
        lh_measure = Column(Float, nullable=True, default=0.0)
        c_measure = Column(Float, nullable=True, default=0.0)
        b_measure = Column(Float, nullable=True, default=0.0)
        tc_measure = Column(Float, nullable=True, default=0.0)
        g_measure = Column(Float, nullable=True, default=0.0)
        lj_measure = Column(Float, nullable=True, default=0.0)
        lp_measure = Column(Float, nullable=True, default=0.0)
        description = Column(String(128), nullable=True, default="No Description")
        image_url = Column(String(128), nullable=True)
    else:
        first_name = ""
        last_name = ""
        e_measure = 0.0
        p_measure = 0.0
        lm_measure = 0.0
        tm_measure = 0.0
        lh_measure = 0.0
        c_measure = 0.0
        b_measure = 0.0
        tc_measure = 0.0
        g_measure = 0.0
        lj_measure = 0.0
        lp_measure = 0.0
        description = ""

    def __init__(self, *args, **kwargs):
        """initializes Place"""
        super().__init__(*args, **kwargs)
