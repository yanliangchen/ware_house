
from backend.myBluePrint.ericic.model.JsonMappingModel import JsonMappingModel as JsonMappingModel
from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION

class jsonmappingApiDao:
    @classmethod
    def select_json_mapping(cls, dc_id):
        db_session = SESSION()
        try:
            _data = db_session.query(JsonMappingModel).filter(JsonMappingModel.id == dc_id).all()
            return  _data

        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()