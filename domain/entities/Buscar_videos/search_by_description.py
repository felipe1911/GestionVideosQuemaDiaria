
from .invoker_comand_query import InvokerCommandQuery

def search_by_description(query_description):
    sarch_course_invoker = InvokerCommandQuery(1,query_description)
    sarch_course_invoker.execute_command()