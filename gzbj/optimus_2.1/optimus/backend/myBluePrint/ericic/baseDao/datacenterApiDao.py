from backend.common.loghandler import BDLog
from backend.Model.connection import SESSION
from backend.myBluePrint.ericic.model.dataCenterModel import DataCenterModel


class datacenterApiDao:
    @classmethod
    def select_instances(cls, limit, offset):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).limit(int(limit)).offset(
                int(offset)).all()
            count = db_session.query(DataCenterModel).count()
            return _data, count
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_instance(cls, dc_id):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).filter(DataCenterModel.id == dc_id).all()
            return _data
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()

    @classmethod
    def select_name_dc(cls, name):
        db_session = SESSION()
        try:
            _data = db_session.query(DataCenterModel).filter(DataCenterModel.name == name).all()
            return _data[0].name
        except Exception as e:
            BDLog.error(e)
        finally:
            db_session.close()
