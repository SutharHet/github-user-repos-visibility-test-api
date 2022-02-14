# procedure
procedure_query = (
  "CREATE PROCEDURE get_info () "
  "BEGIN "
  "SELECT * FROM test_table WHERE id = 3; "
  "SELECT * FROM test_table WHERE name = het; "
  "END"
)

in_procedure_query = (
  "CREATE PROCEDURE get_info (IN n1 int) "
  "BEGIN "
  "SELECT * FROM test_table WHERE id = n1; "
  "END"
)

out_procedure_query = (
  "CREATE PROCEDURE get_info (OUT n1 varchar(10)) "
  "BEGIN "
  "SELECT name INTO n1 FROM test_table WHERE id = 3; "
  "END"
)
in_out_procedure_query = (
  "CREATE PROCEDURE get_info (IN i1 int, OUT n1 varchar(10)) "
  "BEGIN "
  "SELECT name INTO n1 FROM test_table WHERE id = i1; "
  "END"
)
inout_procedure_query = (
  "CREATE PROCEDURE get_info (INOUT i1 int) "
  "BEGIN "
  "SELECT age INTO i1 FROM test_table WHERE id = i1; "
  "END"
)

# trigger
before_insert = (
  "CREATE TRIGGER before_insert_msg "
  "BEFORE INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('Before Insert message'); "
  "END"
)

after_insert = (
  "CREATE TRIGGER after_insert_msg "
  "AFTER INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('After Insert message'); "
  "END"
)

before_update = (
  "CREATE TRIGGER before_update_msg "
  "BEFORE INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('Before Update message'); "
  "END"
)

after_update = (
  "CREATE TRIGGER after_update_msg "
  "AFTER INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('After Update message'); "
  "END"
)

before_delete = (
  "CREATE TRIGGER before_delete_msg "
  "BEFORE INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('Before delete message'); "
  "END"
)

after_delete = (
  "CREATE TRIGGER after_delete_msg "
  "AFTER INSERT ON test_table FOR EACH ROW "
  "BEGIN "
  "INSERT INTO trigger_msgs VALUES ('After delete message'); "
  "END"
)
