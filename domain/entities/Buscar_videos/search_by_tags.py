from .invoker_comand_query import InvokerCommandQuery

def search_by_tags(query_tags):
    sarch_course_invoker = InvokerCommandQuery(2,query_tags)
    sarch_course_invoker.execute_command()