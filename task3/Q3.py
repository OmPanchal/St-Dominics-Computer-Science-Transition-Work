from utils import input_until_right


def times_tables(tables_of=3):
	until = input_until_right("Final term: ", "invalid type, please try again", int)

	for i in range(until + 1):
		print(f"{i} × {tables_of} = {i * tables_of}")


tables_of = input_until_right("I would like the times tables of: ", "invalid type for the tables, must be either float or int", float)

times_tables(tables_of)

