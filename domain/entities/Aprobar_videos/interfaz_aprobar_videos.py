from .load_data_command import LoadDataCommand

def interfaz_aprobar_videos(moderator):
    db_data = LoadDataCommand('domain\database\database_courses.json').execute()
    moderator.check_and_approve_videos(db_data)